# Bhumi-Niti (भूमि-नीति)
### National Digital Platform for Evidence-Based Land Governance

> **Ministry of Rural Development (DoLR) · Department of Land Resources**
> **Smart India Hackathon 2024 · Problem Statement ID: 26019**

---

![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi&logoColor=white)
![MapLibre GL JS](https://img.shields.io/badge/MapLibre_GL_JS-3.6-396CB2?logo=maplibre&logoColor=white)
![Sentinel-2 LULC](https://img.shields.io/badge/Esri_Sentinel--2_LULC-10m-4CAF50?logo=arcgis&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

---

## Executive Overview

Bhumi-Niti bridges the persistent gap between static land administration records and the real-time, evidence-based policy intelligence that administrators, researchers, and citizens urgently need. Across Gujarat — and India broadly — land conversion decisions, revenue dispute resolutions, and ecological risk assessments are made from fragmented, paper-based records, outdated cadastral maps, and siloed department databases. Bhumi-Niti synthesises public government data streams, satellite-calibrated raster imagery, statutory legal corpora, and judicial telemetry into a single, interactive intelligence dashboard that any administrator or researcher can query in seconds by typing a village, city, PIN code, or taluka name.

The platform's core intelligence loop operates as:

```
SELECT AREA  →  DYNAMIC RESOLUTION  →  SATELLITE LULC  →  LIVE DISPUTE TELEMETRY
     ↓                  ↓                    ↓                        ↓
  Type any         Nominatim resolves    Esri 10m Sentinel-2    NJDG / RCMMS
  village, PIN,    precise boundary,    raster overlay shows   aggregated land
  city or taluka   hierarchy & area     Forest / Agri / Urban  case counts & trends
                                                ↓
                                     ASK AI  →  POLICY SIMULATION
                                         ↓              ↓
                                   Grounded RAG    Heuristic zoning
                                   answers legal   & conversion risk
                                   queries from    scoring vs. green
                                   GLRC 1879 &     buffer mandates
                                   Saurashtra Act
```

---

## Key Modules & Features

### 1. High-Fidelity Thematic GIS Canvas

| Capability | Implementation |
|---|---|
| Boundary spotlight | Live Nominatim GeoJSON → inverted polygon mask dims the world outside the searched area |
| LULC raster overlay | Esri 10m Sentinel-2 Land Cover ImageServer tiles — Settlement (red), Agriculture (yellow), Forest (green), Water (blue) |
| Basemap toggle | CARTO Dark Matter ↔ Esri World Imagery (satellite) with smooth fade transition |
| Opacity control | Floating slider adjusts LULC tile opacity 20%–90% in real time |
| Boundary glow | Cyan (#38BDF8) stroke + subtle outer glow on the searched polygon perimeter |

**No synthetic polygons.** Every overlay is sourced from satellite-calibrated raster tiles or live Nominatim geometry. The old Overpass QL rectangular artifacts have been fully replaced.

---

### 2. Live Administrative & Risk Intelligence Dossier

The right-hand panel populates dynamically for every searched location via `/api/v1/intel`:

**Geographic Identity (engine/geocoder.py)**
- Full state → district → taluka → village/ward hierarchy resolved via Nominatim reverse geocoding
- Exact area computed using Shapely projected to EPSG:7755 (India equal-area datum)
- 6-digit PIN code validated and resolved via postal reverse lookup

**Spatial Profile (engine/spatial.py)**
- Dominant Land Use classification from OpenStreetMap Overpass QL feature distribution
- Vegetation cover %, agricultural proportion %, and water body footprint % computed dynamically
- Forest ecology alerts for National Parks, Wildlife Sanctuaries, Reserved Forest, and Eco-Sensitive Zones

**Legal & Regulatory Framework (engine/legal.py)**
- Automatic planning authority detection (AUDA, SUDA, VUDA, RUDA, DSIRDA, GIDC, Forest Dept, Gram Panchayat)
- Jantri circle rate tier (Tier 1 metro core → Tier 4 rural agricultural)
- Section 63 / Section 54 tenancy restriction flags for Gujarat Tenancy Act vs. Saurashtra Gharkhed Act
- Section 73AA tribal inalienability alerts for Fifth Schedule districts (Dang, Dahod, Narmada, etc.)
- Non-Agricultural (NA) conversion prerequisites checklist (iORA portal, Form 7/12, 30-year encumbrance, GDCR)

**Risk & Dispute Telemetry (engine/risk.py)**
- IS 1893:2016 seismic zone classification (Zone II–V) keyed to district centroids
- GSDMA flood hazard rating with basin-specific context
- NJDG/RCMMS-derived active pending land dispute count, civil/revenue split, quarterly trend, and clearance rate
- Category breakdown: partition suits, revenue mutation appeals, tribal inalienability violations, CRZ/ESZ encroachments

---

### 3. Grounded Legal AI & Policy Simulation Engine

**Bhumi-Niti AI Grounded Assistant** (`engine/ai_query.py`)

Answers natural-language queries about land law strictly grounded in the live dossier context — no hallucinated citations, no generic responses.

Supported query topics:
- Non-Agricultural (NA) conversion procedures and risks
- Forest clearance and ESZ buffer requirements
- Tribal land protection (PESA, Section 73AA)
- CRZ / coastal regulation zone constraints
- Jantri premium and TP scheme feasibility
- Dispute backlog impact on title clarity

**Policy Simulation Drawer** (`engine/simulate.py`)

Heuristic trade-off scorer for proposed land-use changes:
- Buffer radius selector (100m – 5000m)
- Proposed use: Residential / Industrial-Logistics / Commercial / Eco-Tourism / Agricultural Consolidation
- Feasibility score (0–100) factoring in seismic zone, flood risk, ESZ proximity, tribal flags, and dispute density
- Estimated timeline and authority approval chain

---

### 4. Bhumi-Niti Knowledge Repository (`/knowledge-base`)

A dedicated portal (`engine/kb_view.py` + `engine/live_gov_kb.py`) fetching live government documents:

| Data Source | Content | Endpoint |
|---|---|---|
| **India Code** (`indiacode.nic.in`) | Gujarat State Acts (GLRC 1879, Saurashtra Gharkhed Act 1949, GTPUDA 1976, GSIR Act 2009) | DSpace REST API |
| **Open Government Data** (`data.gov.in`) | Land, Revenue & Agriculture datasets for Gujarat | OGD REST API |
| **DoLR DILRMP** | Digital India Land Records Modernisation Programme circulars | Public portal |
| **GSDMA** | State Disaster Management Authority flood hazard compendium | Public documents |

Features:
- Full-text faceted search by theme, document type, and year
- AI synthesis: submit any policy question → Bhumi-Niti AI synthesises an answer from retrieved documents
- All documents link back to authoritative government source URLs

---

## Architecture & Data Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       BHUMI-NITI SYSTEM ARCHITECTURE                    │
└─────────────────────────────────────────────────────────────────────────┘

  PUBLIC DATA SOURCES                    FASTAPI BACKEND (main.py)
  ──────────────────                     ────────────────────────────────
  Nominatim OSM API  ─────────────────►  engine/geocoder.py
  (boundary GeoJSON,                       └─ EPSG:7755 area (Shapely)
   reverse geocode)                         └─ Hierarchy resolution

  OSM Overpass QL ────────────────────►  engine/spatial.py
  (land use features)                      └─ LULC distribution
                                            └─ Ecology detection

  IS 1893:2016 Seismic ────────────────►  engine/risk.py
  GSDMA Flood Grid                         └─ Seismic badge
  NJDG / RCMMS Telemetry                   └─ Flood rating
                                            └─ Dispute aggregates

  Gujarat Statutory Acts ──────────────►  engine/legal.py
  (GLRC, Tenancy Act,                      └─ Authority detection
   Saurashtra Gharkhed,                    └─ Jantri tier
   PESA / 73AA, GTPUDA)                    └─ NA prerequisites

  India Code DSpace API ───────────────►  engine/live_gov_kb.py
  data.gov.in OGD API                      └─ Live act retrieval
                                            └─ Dataset listing

  ┌─────────────────────────────────────────────────────────────────────┐
  │                    engine/pipeline.py (orchestrator)                │
  │   geocoder → spatial → legal → risk → dossier → HTTP response      │
  └─────────────────────────────────────────────────────────────────────┘
                │                               │
                ▼                               ▼
  ┌──────────────────────────┐    ┌──────────────────────────────────┐
  │   MapLibre GL JS 3.6     │    │   Right-Hand Intelligence Panel   │
  │   (GIS Canvas — left)    │    │   (Dynamic Telemetry — right)    │
  │                          │    │                                  │
  │  • CARTO Dark basemap    │    │  • KPI cards (area, LULC, seismic│
  │  • Esri 10m Sentinel-2   │    │  • Accordion 1: Land & Ecology   │
  │    LULC raster tiles     │    │  • Accordion 2: Revenue & Legal  │
  │  • Spotlight mask        │    │  • Accordion 3: Dispute & Risk   │
  │  • Boundary glow/stroke  │    │  • Policy Simulation Drawer      │
  │  • Floating LULC legend  │    │  • Bhumi-Niti AI Chat (RAG)      │
  └──────────────────────────┘    └──────────────────────────────────┘

                        SEPARATE ROUTE: /knowledge-base
                        ────────────────────────────────
                        engine/kb_view.py  +  engine/live_gov_kb.py
                        • Live statutory act search (India Code)
                        • Faceted OGD dataset browser
                        • AI-powered policy synthesis
```

---

## Quick Start

### Prerequisites

- Python 3.10+ ([python.org](https://www.python.org/downloads/))
- Internet access (required for live Nominatim, Overpass, and government API calls)
- ~150 MB disk space for Python dependencies

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-org/bhumi-niti.git
cd bhumi-niti

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Start the application (pre-flight checks + auto browser launch)
python run.py
```

The `run.py` launcher will:
1. Verify Python 3.10+ is active
2. Detect virtual environment status
3. Confirm all required packages are installed
4. Print a clean ASCII banner with all service URLs
5. Launch Uvicorn on `http://localhost:8000` with hot-reload
6. Automatically open your default browser after 1.5 seconds

### Manual start (alternative)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### API Documentation

Visit **http://localhost:8000/docs** for the interactive Swagger UI listing all endpoints.

| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/locations/suggest` | GET | Autocomplete search (debounced, Gujarat-enforced) |
| `/api/v1/intel` | GET | Full intelligence pipeline for a location |
| `/api/v1/simulate` | GET | Policy zoning simulation with feasibility score |
| `/api/v1/ai/query` | POST | Grounded AI Q&A for land law questions |
| `/api/v1/kb/documents` | GET | Live government document repository |
| `/api/v1/kb/live-synthesize` | POST | AI synthesis from KB documents |
| `/knowledge-base` | GET | Knowledge Repository portal (HTML) |
| `/` or `/map` | GET | Main GIS Intelligence Dashboard (HTML) |

---

## Demo Walkthrough — Best Test Locations

### 🏭 Sanand, Ahmedabad
**Theme: Peri-urban industrial conversion + agricultural compensation disputes**

Type `Sanand` in the search bar. Observe:
- LULC tiles show a mosaic of agricultural (yellow) and built-up (red) zones reflecting rapid industrialisation along the Dedicated Freight Corridor
- Jantri tier resolves to **Tier 1: Metro Growth Corridor (AUDA jurisdiction)**
- Dispute telemetry shows elevated civil suit counts from land acquisition for Maruti-Suzuki and Tata Nano plant relocations
- Policy simulation: Select "Industrial / Logistics" → Bhumi-Niti scores feasibility and flags Section 63 tenancy clearance as a mandatory prerequisite

---

### 🐆 Sasan Gir, Gir Somnath
**Theme: Asiatic Lion habitat, ESZ buffer rules, and Wildlife Protection constraints**

Type `Sasan Gir` in the search bar. Observe:
- LULC tiles show dense forest canopy (dark green) with protected area boundaries
- Legal panel flags **Wildlife (Protection) Act, 1972** and **NBWL 10km ESZ clearance** as mandatory
- AI chat: Ask *"Can I build an eco-resort 3 km from the sanctuary boundary?"* → grounded answer cites ESZ notification limits and Forest Department NOC requirements
- Simulation: "Eco-Tourism" use type → highest allowable feasibility score with strict buffer conditions

---

### 🌊 Dholera SIR, Ahmedabad
**Theme: TP schemes, coastal mudflats, high flood hazard, and smart city infrastructure**

Type `Dholera` in the search bar. Observe:
- Dispute telemetry reflects TP scheme land pooling appeals from farmers
- Legal panel shows **DSIRDA jurisdiction** under GSIR Act 2009 with Tier 2 Jantri classification
- Risk panel shows **High Flood Hazard** (Gulf of Khambhat tidal basin) and Zone III seismic badge
- LULC tiles show tidal mudflat / water-adjacent zones near the SIR perimeter

---

### ⚓ Mundra, Kutch
**Theme: Port SEZ, CRZ regulations, and maximum seismic hazard (Zone V)**

Type `Mundra` in the search bar. Observe:
- Risk panel displays **Zone V (Very High Seismic Hazard)** — the highest IS 1893 classification
- LULC tiles show industrial (red) and water (blue) zones along the Kutch coastline
- Legal panel flags **Coastal Regulation Zone (CRZ)** constraints and **KUTCH — Tier 2 Industrial Estate** Jantri
- AI chat: Ask *"What are the CRZ clearance requirements for a logistics warehouse near Mundra port?"* → grounded response cites CRZ Notification 2019 and MoEFCC mandatory conditions

---

## Project Structure

```
bhumi-niti/
│
├── main.py                  # FastAPI app, all HTML/CSS/JS (single-file server)
├── run.py                   # Universal startup runner (this file)
├── requirements.txt         # Python dependencies
├── README.md                # This document
│
└── engine/                  # Intelligence pipeline modules
    ├── __init__.py
    ├── pipeline.py          # Master orchestrator
    ├── geocoder.py          # Nominatim geocoding + Gujarat enforcement + area (EPSG:7755)
    ├── spatial.py           # Overpass QL LULC + ecology detection
    ├── legal.py             # Planning authority, Jantri tier, tenancy, NA prerequisites
    ├── risk.py              # IS 1893 seismic, GSDMA flood, dispute telemetry
    ├── dossier.py           # 5-part dossier compiler
    ├── simulate.py          # Policy & zoning heuristic simulation
    ├── thematic.py          # Boundary GeoJSON processor (spotlight mask)
    ├── ai_query.py          # Grounded legal & spatial AI query engine
    ├── disputes.py          # NJDG / RCMMS dispute telemetry aggregator
    ├── live_gov_kb.py       # Live India Code + OGD retrieval pipeline
    ├── kb_view.py           # /knowledge-base HTML portal renderer
    └── knowledge_base.py    # KB faceted search & synthesis logic
```

---

## Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | FastAPI 0.111 + Uvicorn | Async REST API, HTML serving |
| **Geocoding** | Nominatim (OpenStreetMap) | Boundary resolution, hierarchy, PIN |
| **Spatial** | Overpass QL (OSM) | Live LULC feature extraction |
| **Area Calc** | Shapely + pyproj (EPSG:7755) | Exact equal-area polygon measurement |
| **GIS Canvas** | MapLibre GL JS 3.6 | WebGL map rendering |
| **LULC Tiles** | Esri 10m Sentinel-2 ImageServer | Satellite-calibrated land cover |
| **Basemaps** | CARTO Dark, Esri Imagery | Map backgrounds |
| **Legal AI** | Rule-based RAG (ai_query.py) | Grounded statutory Q&A |
| **Gov Data** | India Code DSpace REST | Live statutory acts |
| **Gov Data** | data.gov.in OGD API | Live land/revenue datasets |
| **Seismic** | IS 1893:2016 zone lookup | District-level hazard classification |
| **Flood** | GSDMA flood grid heuristics | River-basin flood rating |
| **Disputes** | NJDG / RCMMS aggregates | Land litigation telemetry |

---

## Data Privacy, Ethics & Source Transparency

> **Bhumi-Niti does not collect, store, or expose any individual citizen data.**

All data presented on this platform is sourced exclusively from:

- **Public aggregated statistics** — NJDG district-level case counts (no party names, no case details)
- **Open government datasets** — data.gov.in, India Code, GSDMA — all carrying open government data licences
- **Public satellite imagery** — Esri 10m Sentinel-2 Land Cover (class-level raster tiles, not parcel-level)
- **OpenStreetMap** — community-contributed public geodata (ODbL licence)
- **Nominatim** — OSM geocoding service (no user queries stored beyond session)

**No private 7/12 (Satbara) ownership records, no Aadhaar-linked data, no individual mutation or registration documents are accessed or displayed.** All dispute metrics are district-level aggregates from public judicial dashboards. The platform is fully compliant with the National Data Sharing and Accessibility Policy (NDSAP) 2012 and India's Digital Personal Data Protection Act (DPDPA) 2023.

---

## Disclaimer

This platform is a proof-of-concept research tool built for Smart India Hackathon 2024. Geospatial boundaries, administrative hierarchies, and statutory interpretations are provided for research and demonstration purposes only and should not be used as a substitute for official government records, legal advice, or certified land survey data. All regulatory queries should be verified with the competent authority (Revenue Collector / Planning Authority / Forest Department) before any land-related decision.

---

## Team

Built for **Smart India Hackathon 2024** — Problem Statement 26019
**Ministry of Rural Development (DoLR) | Department of Land Resources**

---

*Bhumi-Niti (भूमि-नीति) — "Policy for the Land"*
