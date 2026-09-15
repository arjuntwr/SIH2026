# National Digital Platform for Research, Policy Innovation, and Land Governance
### Ministry of Rural Development, Department of Land Resources (DoLR), Government of India

A unified, searchable, and real-time knowledge management repository indexing research papers, policy briefs, cadastral frameworks, legal case studies, and live land dispute datasets.

---

## Architecture Overview

1. **Database Schema (`backend/database/schema.sql`)**:
   - Production PostgreSQL + `pgvector` DDL.
   - Tables for `taxonomies`, `resources`, `dispute_statistics`, and `sync_logs`.
   - Full-text search GIN vectors (`to_tsvector`) and trigram fuzzy matching.

2. **Backend API (`backend/`)**:
   - FastAPI server with CORS, OpenAPI Swagger documentation at `http://localhost:8000/docs`.
   - Asynchronous background ingestion workers simulating e-Courts NJDG, data.gov.in OGD, and DoLR Gazette feeds.
   - Endpoints:
     * `GET /api/v1/repository/resources` (Faceted search, pagination, relevance sorting)
     * `GET /api/v1/repository/resources/{id}` (Detailed record with GeoJSON cadastral layer & AI summary)
     * `GET /api/v1/repository/analytics/disputes` (Real-time dispute velocity, disposal rates, state scorecards)
     * `GET /api/v1/repository/sync/status` (Health & latency of external public government feeds)
     * `POST /api/v1/repository/sync/trigger` (Background ingestion execution with live progress)

3. **Frontend Web Portal (`frontend/`)**:
   - React 18 + Vite + Tailwind CSS + Lucide Icons + Leaflet GIS.
   - Formal Indian Government Web Guidelines (NIC / Digital India) aesthetic with Satyameva Jayate emblem and bilingual typography.
   - Live Government Sync Telemetry ticker with interactive terminal logs modal.
   - Top Dispute & Policy Analytics Summary Bar with dispute velocity micro-charts.
   - Multi-faceted filter sidebar (State/UT, District, LGD Directory Code, Document Type, Theme, GIS Layer, Date Range).
   - Dual view modes: Interactive Evidence Cards and Cadastral Tabular View.
   - Slide-over Document Inspection Drawer:
     * AI Key Takeaways, Policy Implications & Legal Doctrines
     * Regional Language Translation Switcher (English, हिन्दी, मराठी, తెలుగు, ଓଡ଼ିଆ)
     * Interactive Leaflet Cadastral Map rendering vector parcel polygons with attribute inspection
     * Citation Generator (APA, MLA, Indian Legal / Supreme Court citation format)
     * Cryptographic SHA-256 integrity verification badge & verified download.

---

## Quick Start

### 1. Run Backend Server
```bash
# From workspace root:
python -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```
Swagger UI is available at: `http://127.0.0.1:8000/docs`

### 2. Run Frontend Portal
```bash
# Navigate to frontend:
cd frontend
npm run dev
```
Open `http://127.0.0.1:5173/` in your browser.
