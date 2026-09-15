-- ============================================================================
-- National Digital Platform for Research, Policy Innovation, and Land Governance
-- Ministry of Rural Development - Department of Land Resources (DoLR)
-- PostgreSQL + pgvector Database Schema Specification
-- ============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "vector";      -- For semantic search embeddings
CREATE EXTENSION IF NOT EXISTS "pg_trgm";     -- For trigram fuzzy text search

-- Clean previous instances if needed
DROP TABLE IF EXISTS sync_logs CASCADE;
DROP TABLE IF EXISTS dispute_statistics CASCADE;
DROP TABLE IF EXISTS resource_citations CASCADE;
DROP TABLE IF EXISTS resources CASCADE;
DROP TABLE IF EXISTS taxonomies CASCADE;

-- 1. TAXONOMIES STREAM TABLE
CREATE TABLE taxonomies (
    id VARCHAR(64) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    name_hi VARCHAR(255) NOT NULL,
    description TEXT,
    icon_name VARCHAR(64),
    display_order INT DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. CORE RESOURCES TABLE
CREATE TABLE resources (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(512) NOT NULL,
    title_hi VARCHAR(512),
    taxonomy_stream VARCHAR(64) NOT NULL REFERENCES taxonomies(id) ON UPDATE CASCADE,
    document_type VARCHAR(64) NOT NULL, -- Act/Bill, Judgement, Policy Brief, Dataset, Academic Paper, Manual/Framework
    theme VARCHAR(128) NOT NULL,        -- Digital Cadastre, Land Acquisition, Forest Rights, Tenancy, Climate Resilience
    
    -- Geographic & Administrative Classification (LGD Standard)
    coverage_scope VARCHAR(32) NOT NULL DEFAULT 'National', -- National, State, District, Village
    state_ut VARCHAR(128),
    district VARCHAR(128),
    lgd_code VARCHAR(32),               -- Local Government Directory Code (Ministry of Panchayati Raj)
    ulpin VARCHAR(32),                  -- Unique Land Parcel Identification Number (Bhu-Aadhaar)
    
    -- Legal & Administrative Metadata
    legal_authority VARCHAR(255) NOT NULL, -- DoLR, Supreme Court of India, State Revenue Dept, Survey of India
    gazette_number VARCHAR(128),
    case_number VARCHAR(128),
    publication_date DATE NOT NULL,
    effective_date DATE,
    
    -- Content & AI Summarization
    abstract TEXT NOT NULL,
    abstract_hi TEXT,
    ai_executive_summary JSONB,          -- Key takeaways, implications, stakeholders, policy gaps
    full_text TEXT,
    original_language VARCHAR(32) DEFAULT 'English', -- English, Hindi, Marathi, Telugu, Odia, etc.
    translations JSONB,                 -- Multilingual translations for title & abstract
    
    -- OCR & Digital Preservation
    ocr_status VARCHAR(32) DEFAULT 'VERIFIED_SEARCHABLE', -- VERIFIED_SEARCHABLE, PENDING, MANUAL_REVIEW
    ocr_confidence NUMERIC(5, 2) DEFAULT 99.40,
    page_count INT DEFAULT 1,
    file_format VARCHAR(16) DEFAULT 'PDF',
    file_size_bytes BIGINT,
    file_url VARCHAR(1024),
    sha256_checksum VARCHAR(64) NOT NULL,
    
    -- Geospatial Cadastral Layer (GeoJSON)
    spatial_geojson JSONB,              -- Cadastral parcel / boundary GeoJSON representation
    has_spatial_layer BOOLEAN DEFAULT FALSE,
    
    -- Search & Vector Embeddings
    search_vector TSVECTOR,             -- Full text search index
    embedding vector(1536),             -- OpenAI text-embedding-3 / BGE semantic vector
    
    -- External Sync Provenance
    source_system VARCHAR(64) NOT NULL, -- e-Courts, data.gov.in, DoLR Gazette, API Setu, NIC
    source_id VARCHAR(255),
    last_synced_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Full-Text Search Vector Generation Function & Trigger
CREATE OR REPLACE FUNCTION update_resources_search_vector() RETURNS trigger AS $$
BEGIN
    NEW.search_vector :=
        setweight(to_tsvector('english', coalesce(NEW.title, '')), 'A') ||
        setweight(to_tsvector('english', coalesce(NEW.legal_authority, '')), 'B') ||
        setweight(to_tsvector('english', coalesce(NEW.theme, '')), 'B') ||
        setweight(to_tsvector('english', coalesce(NEW.document_type, '')), 'B') ||
        setweight(to_tsvector('english', coalesce(NEW.state_ut, '')), 'C') ||
        setweight(to_tsvector('english', coalesce(NEW.district, '')), 'C') ||
        setweight(to_tsvector('english', coalesce(NEW.lgd_code, '')), 'C') ||
        setweight(to_tsvector('english', coalesce(NEW.ulpin, '')), 'C') ||
        setweight(to_tsvector('english', coalesce(NEW.gazette_number, '')), 'C') ||
        setweight(to_tsvector('english', coalesce(NEW.case_number, '')), 'C') ||
        setweight(to_tsvector('english', coalesce(NEW.abstract, '')), 'D');
    RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_resources_search_vector
BEFORE INSERT OR UPDATE ON resources
FOR EACH ROW EXECUTE FUNCTION update_resources_search_vector();

-- Indexes for ultra-fast query execution
CREATE INDEX idx_resources_taxonomy ON resources (taxonomy_stream);
CREATE INDEX idx_resources_doctype ON resources (document_type);
CREATE INDEX idx_resources_theme ON resources (theme);
CREATE INDEX idx_resources_state ON resources (state_ut);
CREATE INDEX idx_resources_pub_date ON resources (publication_date DESC);
CREATE INDEX idx_resources_fts ON resources USING GIN(search_vector);
CREATE INDEX idx_resources_trgm_title ON resources USING GIN(title gin_trgm_ops);
-- HNSW Vector Index for Semantic Distance Search (Cosine)
-- CREATE INDEX idx_resources_embedding ON resources USING hnsw (embedding vector_cosine_ops);

-- 3. DISPUTE STATISTICS TABLE (e-Courts NJDG Ingestion)
CREATE TABLE dispute_statistics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    state_ut VARCHAR(128) NOT NULL,
    state_lgd_code VARCHAR(16),
    district VARCHAR(128),
    district_lgd_code VARCHAR(16),
    reporting_period VARCHAR(16) NOT NULL, -- e.g. '2025-Q4', '2026-M02'
    
    -- NJDG Core Civil Land Dispute Metrics
    total_active_disputes BIGINT NOT NULL DEFAULT 0,
    cases_filed_current_period INT NOT NULL DEFAULT 0,
    cases_disposed_current_period INT NOT NULL DEFAULT 0,
    disposal_rate_percentage NUMERIC(5, 2) NOT NULL DEFAULT 0.0,
    average_pendency_years NUMERIC(4, 2) NOT NULL DEFAULT 0.0,
    
    -- Sub-categorization
    title_ownership_disputes INT DEFAULT 0,
    rfctlarr_acquisition_disputes INT DEFAULT 0,
    tenancy_leasing_disputes INT DEFAULT 0,
    boundary_demarcation_disputes INT DEFAULT 0,
    tribal_land_alienation_disputes INT DEFAULT 0,
    
    -- Institutional Metrics
    fast_track_revenue_courts_active INT DEFAULT 0,
    bhu_aadhaar_seeding_percentage NUMERIC(5, 2) DEFAULT 0.0,
    reform_adoption_score NUMERIC(5, 2) DEFAULT 0.0, -- 0 - 100 benchmark
    
    ingested_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    source_feed VARCHAR(64) DEFAULT 'e-Courts NJDG v4.2'
);

CREATE INDEX idx_dispute_stats_state ON dispute_statistics (state_ut);
CREATE INDEX idx_dispute_stats_period ON dispute_statistics (reporting_period);

-- 4. EXTERNAL SYNC TELEMETRY LOGS (API Setu, data.gov.in, e-Courts, DoLR)
CREATE TABLE sync_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    endpoint_name VARCHAR(128) NOT NULL,
    endpoint_category VARCHAR(64) NOT NULL, -- e-Courts NJDG, data.gov.in OGD, DoLR Gazette, Bhu-Aadhaar ULPIN
    target_url VARCHAR(512) NOT NULL,
    sync_mode VARCHAR(32) NOT NULL DEFAULT 'SCHEDULED_BATCH', -- SCHEDULED_BATCH, MANUAL_TRIGGER, WEBHOOK
    status VARCHAR(32) NOT NULL,                             -- SUCCESS, DEGRADED, FAILED, RETRYING
    http_status_code INT,
    response_time_ms INT,
    records_harvested INT DEFAULT 0,
    records_updated INT DEFAULT 0,
    error_message TEXT,
    retry_count INT DEFAULT 0,
    triggered_by VARCHAR(64) DEFAULT 'SYSTEM_DAEMON',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_sync_logs_created_at ON sync_logs (created_at DESC);
CREATE INDEX idx_sync_logs_status ON sync_logs (status);

-- 5. INITIAL TAXONOMIES SEED
INSERT INTO taxonomies (id, name, name_hi, description, icon_name, display_order) VALUES
('policy-legislation', 'Policy & Legislation', 'नीति एवं विधान', 'National and State land reform acts, SVAMITVA guidelines, ULPIN/Bhu-Aadhaar circulars, and Model Tenancy Act documents.', 'ScrollText', 1),
('academic-research', 'Academic & Applied Research', 'शैक्षणिक एवं व्यावहारिक शोध', 'Peer-reviewed whitepapers, LandVoc-tagged publications, remote sensing studies, and tenure evaluation reports.', 'BookOpen', 2),
('judicial-records', 'Judicial & Land Dispute Records', 'न्यायिक एवं भूमि विवाद अभिलेख', 'Supreme Court and High Court landmark rulings on RFCTLARR acquisition, title disputes, and tribal land rights.', 'Scale', 3),
('government-datasets', 'Government Datasets & Baselines', 'सरकारी डेटासेट एवं आधार रेखाएं', 'Geo-referenced cadastral boundaries, village-level RoR metadata, and agricultural/forest census datasets.', 'Database', 4),
('pilot-case-studies', 'Best Practices & Pilot Case Studies', 'सर्वोत्तम प्रथाएं एवं प्रायोगिक केस स्टडीज', 'State-level digital cadastral resurvey reports, modern record room audits, and spatial planning pilots.', 'Award', 5);
