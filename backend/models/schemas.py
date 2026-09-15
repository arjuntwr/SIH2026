"""
Pydantic Schemas & Mock Government API Models
Ministry of Rural Development, Department of Land Resources (DoLR)
National Digital Platform for Land Governance
"""

from typing import List, Optional, Dict, Any
from datetime import date, datetime
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Core Resource Schemas
# ---------------------------------------------------------------------------

class AIExecutiveSummary(BaseModel):
    key_takeaways: List[str]
    policy_implications: List[str]
    affected_stakeholders: List[str]
    legal_doctrines_invoked: Optional[List[str]] = []
    spatial_relevance: Optional[str] = None


class MultilingualTranslations(BaseModel):
    hi: Optional[Dict[str, str]] = None
    mr: Optional[Dict[str, str]] = None
    te: Optional[Dict[str, str]] = None
    or_: Optional[Dict[str, str]] = Field(None, alias="or")


class CitationFormats(BaseModel):
    apa: str
    mla: str
    indian_legal: str  # e.g., (2023) 4 SCC 121 or DoLR Gaz. S.O. 412(E)
    bibtex: str


class ResourceBase(BaseModel):
    title: str
    title_hi: Optional[str] = None
    taxonomy_stream: str
    document_type: str
    theme: str
    coverage_scope: str = "National"
    state_ut: Optional[str] = None
    district: Optional[str] = None
    lgd_code: Optional[str] = None
    ulpin: Optional[str] = None
    legal_authority: str
    gazette_number: Optional[str] = None
    case_number: Optional[str] = None
    publication_date: date
    effective_date: Optional[date] = None
    abstract: str
    abstract_hi: Optional[str] = None
    ai_executive_summary: Optional[AIExecutiveSummary] = None
    original_language: str = "English"
    translations: Optional[MultilingualTranslations] = None
    ocr_status: str = "VERIFIED_SEARCHABLE"
    ocr_confidence: float = 99.40
    page_count: int = 1
    file_format: str = "PDF"
    file_size_bytes: int = 0
    file_url: str
    sha256_checksum: str
    has_spatial_layer: bool = False
    spatial_geojson: Optional[Dict[str, Any]] = None
    source_system: str
    source_id: Optional[str] = None


class ResourceResponse(ResourceBase):
    id: str
    citations: Optional[CitationFormats] = None
    last_synced_at: datetime
    created_at: datetime

    class Config:
        populate_by_name = True


class ResourceFilterParams(BaseModel):
    q: Optional[str] = None
    taxonomy_stream: Optional[str] = None
    document_type: Optional[str] = None
    theme: Optional[str] = None
    state_ut: Optional[str] = None
    district: Optional[str] = None
    lgd_code: Optional[str] = None
    legal_authority: Optional[str] = None
    year_from: Optional[int] = None
    year_to: Optional[int] = None
    has_spatial: Optional[bool] = None
    sort_by: str = "date_desc"  # date_desc, date_asc, relevance, citations
    page: int = 1
    page_size: int = 10


class PaginatedResourcesResponse(BaseModel):
    items: List[ResourceResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
    facets: Dict[str, Dict[str, int]]


# ---------------------------------------------------------------------------
# Dispute Analytics Schemas (e-Courts NJDG Ingestion)
# ---------------------------------------------------------------------------

class StateDisputeMetric(BaseModel):
    state_ut: str
    state_lgd_code: str
    total_active_disputes: int
    cases_filed_ytd: int
    cases_disposed_ytd: int
    disposal_rate_percentage: float
    average_pendency_years: float
    title_ownership_disputes: int
    rfctlarr_acquisition_disputes: int
    tenancy_leasing_disputes: int
    boundary_demarcation_disputes: int
    tribal_land_alienation_disputes: int
    bhu_aadhaar_seeding_percentage: float
    reform_adoption_score: float  # Scale 0 - 100


class DisputeAnalyticsSummary(BaseModel):
    reporting_period: str
    nationwide_active_disputes: int
    nationwide_disposal_rate: float
    total_indexed_literature: int
    active_cadastral_datasets: int
    state_dispute_metrics: List[StateDisputeMetric]
    dispute_trend_monthly: List[Dict[str, Any]]
    top_dispute_themes: List[Dict[str, Any]]


# ---------------------------------------------------------------------------
# Government API Telemetry & Sync Schemas
# ---------------------------------------------------------------------------

class EndpointTelemetry(BaseModel):
    endpoint_name: str
    endpoint_category: str  # e-Courts NJDG, data.gov.in OGD, DoLR Gazette, Bhu-Aadhaar ULPIN
    target_url: str
    status: str  # OPERATIONAL, DEGRADED, SYNCING, OFFLINE
    http_status_code: int
    response_time_ms: int
    last_synced_at: datetime
    records_indexed: int
    error_message: Optional[str] = None


class TelemetryStatusResponse(BaseModel):
    system_status: str  # ALL_SYSTEMS_OPERATIONAL, PARTIAL_DEGRADATION
    last_global_sync: datetime
    endpoints: List[EndpointTelemetry]


class SyncTriggerRequest(BaseModel):
    target_endpoints: Optional[List[str]] = None  # None means all
    force_resync: bool = False


class SyncTriggerResponse(BaseModel):
    job_id: str
    status: str
    initiated_at: datetime
    message: str
    endpoints_queued: List[str]


# ---------------------------------------------------------------------------
# External Government Public Portal Mock Payload Schemas
# ---------------------------------------------------------------------------

# 1. e-Courts National Judicial Data Grid (NJDG) Mock Feed Schema
class ECourtsNJDGMockRecord(BaseModel):
    cnr_number: str  # Case Natural Resource Number (16-char unique identifier)
    court_establishment: str  # e.g., District & Sessions Court, Pune
    state_code: str
    district_code: str
    case_type: str  # Land Acquisition (LAR), Title Suit (TS), Tenancy Appeal
    filing_date: str
    petitioner_advocate: str
    respondent_dept: str  # e.g., Collector & District Magistrate, Land Acquisition Officer
    dispute_category: str
    current_status: str  # Pending Arguments, Reserved for Orders, Disposed
    relief_claimed: str
    khasra_survey_numbers: List[str]
    ulpin_referenced: Optional[str] = None


# 2. data.gov.in (Open Government Data - OGD) Catalog Harvester Mock Schema
class OGDCatalogDatasetMock(BaseModel):
    dataset_nid: str
    catalog_title: str
    ministry: str = "Ministry of Rural Development"
    department: str = "Department of Land Resources"
    granularity: str  # Village, Taluk, District, National
    frequency: str  # Real-time, Monthly, Annual
    data_formats: List[str]  # GeoJSON, SHP, CSV, JSON
    last_updated: str
    spatial_bbox: Optional[List[float]] = None
    record_count: int
    api_endpoint_url: str
    checksum_md5: str
