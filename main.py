"""
Bhumi-Niti (भूमि-नीति): National Digital Platform for Evidence-Based Land Governance
FastAPI Dynamic Geospatial Engine & MapLibre GL JS Executive Dashboard | DoLR, MoRD
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any, List

from engine.geocoder import resolve_location, suggest_locations
from engine.spatial import query_live_spatial_footprint
from engine.legal import evaluate_regulatory_framework
from engine.risk import evaluate_risk_and_vulnerability
from engine.dossier import compile_intelligence_dossier
from engine.pipeline import run_intelligence_pipeline
from engine.simulate import run_policy_simulation
from engine.ai_query import query_grounded_ai
from engine.thematic import extract_thematic_gis_layers
from engine.knowledge_base import (
    get_all_documents,
    get_document_by_id,
    synthesize_policy_literature
)
from engine.live_gov_kb import (
    get_live_gujarat_repository,
    synthesize_live_gujarat_document
)
from engine.kb_view import render_knowledge_base_html
from engine.innovation_view import render_innovation_html
from engine.gov_portal_view import render_gov_portal_html

app = FastAPI(
    title="Bhumi-Niti (भूमि-नीति) Core API",
    description="Backend engine for the National Digital Platform for Evidence-Based Land Governance — DoLR, Ministry of Rural Development.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# Dedicated Knowledge Base Route
# -----------------------------------------------------------------------------
@app.get("/knowledge-base", response_class=HTMLResponse)
def knowledge_base_ui():
    """Dedicated Land Governance Knowledge Base & Policy Research Portal."""
    return render_knowledge_base_html()

# -----------------------------------------------------------------------------
# Dedicated Innovation & Challenges Route (Req 15)
# -----------------------------------------------------------------------------
@app.get("/innovation", response_class=HTMLResponse)
def innovation_ui():
    """DoLR Land Governance Innovation Hub, Challenges & Research Grants Portal."""
    return render_innovation_html()

# -----------------------------------------------------------------------------
# Data Models
# -----------------------------------------------------------------------------
class QueryRequest(BaseModel):
    query: str
    radius_km: Optional[float] = 3.5

class SimulationRequest(BaseModel):
    query: str
    simulation_type: Optional[str] = "na_conversion"
    buffer_meters: Optional[float] = 500.0
    proposed_use: Optional[str] = "Industrial / Logistics"
    target_area_sqm: Optional[float] = 10000.0

class AIQueryRequest(BaseModel):
    query: str
    location: Optional[str] = "Gujarat"
    context: Optional[Dict[str, Any]] = None

class SpatialSynthesisRequest(BaseModel):
    query: Optional[str] = None
    location: Optional[str] = None
    district_id: Optional[str] = None
    radius_km: Optional[float] = 3.5

class SynthesisRequest(BaseModel):
    doc_ids: Optional[List[str]] = None
    topic: Optional[str] = None
    question: Optional[str] = None

class LiveSynthesisRequest(BaseModel):
    doc_id: Optional[str] = None
    document_url: Optional[str] = None
    topic: Optional[str] = None
    user_query: Optional[str] = None

# -----------------------------------------------------------------------------
# REST API Endpoints
# -----------------------------------------------------------------------------
@app.get("/api/v1/locations/suggest")
def api_suggest_locations(q: str = Query(..., min_length=1, description="Prefix search term")):
    """
    Real-time autocomplete suggestions strictly scoped to Gujarat territorial limits.
    Returns maximum 5 suggestions with display_name, osm_id, type, lat, lon, and category badge.
    """
    try:
        return suggest_locations(q, limit=5)
    except Exception:
        return []

@app.get("/api/v1/resolve")
def api_resolve_gujarat_location(query: str = Query(..., description="Entity name, PIN code, village, or taluka in Gujarat")):
    """Dynamically geocodes and strictly ensures query is within Gujarat."""
    try:
        return resolve_location(query)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/spatial")
def api_extract_spatial_footprint(
    lat: float = Query(..., description="Latitude coordinate"),
    lon: float = Query(..., description="Longitude coordinate"),
    radius_km: float = Query(3.5, description="Search radius in kilometers")
):
    """Dynamically queries Overpass API for live LULC, forest, and protected zone footprints."""
    return query_live_spatial_footprint(lat, lon, radius_km)

@app.get("/api/v1/intel")
def api_get_intelligence_dossier(
    query: str = Query(..., description="Entity name, PIN code, village, or taluka in Gujarat"),
    radius_km: float = Query(3.5, description="Extraction radius in km")
):
    """End-to-end live intelligence pipeline synthesizing all 5 dossier layers plus thematic GIS vectors."""
    try:
        return run_intelligence_pipeline(query, radius_km=radius_km)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/intel")
def api_post_intelligence_dossier(payload: QueryRequest):
    """POST endpoint for end-to-end intelligence synthesis."""
    try:
        return run_intelligence_pipeline(payload.query, radius_km=payload.radius_km or 3.5)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/synthesize")
def api_post_synthesize(payload: SpatialSynthesisRequest):
    """
    Real-time dynamic synthesis endpoint:
    Computes all administrative hierarchy, EPSG:7755 geographic area, live dispute aggregates,
    dynamic land use distribution, and statutory framework on the fly.
    """
    try:
        target = payload.query or payload.location or payload.district_id or "Gandhinagar, Gujarat"
        return run_intelligence_pipeline(target, radius_km=payload.radius_km or 3.5)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/districts/{district_id}/profile")
def api_get_district_profile(district_id: str):
    """District profile telemetry returning hierarchy, agro-climatic profile, and risk indicators."""
    try:
        geo = resolve_location(district_id)
        hierarchy = geo["hierarchy"]
        risk = evaluate_risk_and_vulnerability(hierarchy, geo["lat"], geo["lon"], geo["official_name"])
        return {
            "status": "success",
            "district": hierarchy.get("district", district_id),
            "taluka": hierarchy.get("taluka"),
            "official_name": geo["official_name"],
            "lat": geo["lat"],
            "lon": geo["lon"],
            "pin_code": geo["pin_code"],
            "exact_area_sqkm": geo.get("exact_area_sqkm"),
            "bbox": geo["bbox"],
            "hierarchy": hierarchy,
            "agro_climatic_zone": risk.get("agro_climatic_zone"),
            "soil_topography": risk.get("soil_and_topography"),
            "seismic_hazard": risk.get("seismic_hazard"),
            "flood_rating": risk.get("flood_rating"),
            "dispute_telemetry": risk.get("dispute_telemetry", {}),
            "dispute_signal": risk.get("dispute_signals", {}),
            "coastal_climate_notes": risk.get("climate_and_vulnerability", "")
        }
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/districts/{district_id}/gis-layers")
def api_get_district_gis_layers(
    district_id: str,
    radius_km: float = Query(3.5, description="Extraction radius in km")
):
    """
    Returns GeoJSON FeatureCollection with 5 distinct thematic layers:
    disputed, government, forest, water, residential.
    """
    try:
        geo = resolve_location(district_id)
        return extract_thematic_gis_layers(
            lat=geo["lat"],
            lon=geo["lon"],
            radius_km=radius_km,
            official_name=geo["official_name"],
            district=geo["hierarchy"].get("district", ""),
            entity_geojson=geo.get("geojson"),
            bbox=geo.get("bbox")
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/gis-layers")
def api_get_gis_layers(
    lat: Optional[float] = Query(None, description="Latitude coordinate"),
    lon: Optional[float] = Query(None, description="Longitude coordinate"),
    query: Optional[str] = Query(None, description="Optional entity name or query to resolve"),
    radius_km: float = Query(3.5, description="Extraction radius in km"),
    entity: Optional[str] = Query(None, description="Optional entity name")
):
    """Returns GeoJSON FeatureCollection with 5 distinct thematic layers."""
    try:
        target_entity = query or entity
        official_name = "Gujarat Territory"
        district = ""
        bbox = None
        geojson = None
        
        if lat is None or lon is None:
            if not target_entity:
                target_entity = "Gandhinagar, Gujarat"
            geo = resolve_location(target_entity)
            lat = geo["lat"]
            lon = geo["lon"]
            official_name = geo["official_name"]
            district = geo["hierarchy"].get("district", "")
            bbox = geo.get("bbox")
            geojson = geo.get("geojson")
        elif target_entity:
            official_name = target_entity
            
        return extract_thematic_gis_layers(
            lat=lat,
            lon=lon,
            radius_km=radius_km,
            official_name=official_name,
            district=district,
            entity_geojson=geojson,
            bbox=bbox
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/simulate")
def api_post_policy_simulation(payload: SimulationRequest):
    """Dynamically simulates land conversion, buffer zoning, and statutory clearance feasibility."""
    try:
        return run_policy_simulation(
            query=payload.query,
            simulation_type=payload.simulation_type or "na_conversion",
            buffer_meters=payload.buffer_meters or 500.0,
            proposed_use=payload.proposed_use or "Industrial / Logistics",
            target_area_sqm=payload.target_area_sqm or 10000.0
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/simulate")
def api_get_policy_simulation(
    query: str = Query(...),
    simulation_type: str = Query("na_conversion"),
    buffer_meters: float = Query(500.0),
    proposed_use: str = Query("Industrial / Logistics"),
    target_area_sqm: float = Query(10000.0)
):
    """GET simulation endpoint."""
    try:
        return run_policy_simulation(
            query=query,
            simulation_type=simulation_type,
            buffer_meters=buffer_meters,
            proposed_use=proposed_use,
            target_area_sqm=target_area_sqm
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/ai/query")
def api_post_grounded_ai_query(payload: AIQueryRequest):
    """Answers user queries grounded in live spatial dossier data and statutory legal codes of Gujarat."""
    try:
        return query_grounded_ai(user_question=payload.query, location_query=payload.location, context=payload.context)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/ai/query")
def api_get_grounded_ai_query(
    query: str = Query(..., description="User question"),
    location: str = Query(..., description="Location to ground the query against")
):
    """GET grounded AI query endpoint."""
    try:
        return query_grounded_ai(user_question=query, location_query=location)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------------------------------------------------------
# Live Government Knowledge Repository & Policy Research Endpoints (Gujarat)
# -----------------------------------------------------------------------------
@app.get("/api/v1/kb/documents")
def api_kb_get_documents(
    q: Optional[str] = Query(None, description="Search query strictly covering Gujarat enactments, circulars, and datasets"),
    type: Optional[str] = Query(None, description="Document category"),
    theme: Optional[str] = Query(None, description="Gujarat governance facet (e.g. Gujarat Land Revenue Code, Tenancy, GTPUDA, Section 73AA, Dholera)"),
    jurisdiction: Optional[str] = Query("Gujarat", description="State jurisdiction (strictly scoped to Gujarat)"),
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    """
    Live Government Data Retrieval Pipeline:
    Dynamically queries India Code (Gujarat jurisdiction), OGD Platform India (Gujarat filters),
    and Gujarat Revenue Department circulars/gazettes without static seed files.
    """
    try:
        return get_live_gujarat_repository(
            q=q,
            theme=theme,
            doc_type=type,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/kb/documents/{doc_id}")
def api_kb_get_document_by_id(doc_id: str):
    """
    Returns full document details, official government citations, and live download links.
    """
    repo = get_live_gujarat_repository(limit=100)
    for doc in repo.get("documents", []):
        if doc.get("doc_id") == doc_id:
            return doc
    # Fallback to local record if query matches
    doc = get_document_by_id(doc_id)
    if doc:
        return doc
    raise HTTPException(status_code=404, detail=f"Document '{doc_id}' not found in Gujarat live repository.")

@app.post("/api/v1/kb/live-synthesize")
def api_kb_live_synthesize(payload: LiveSynthesisRequest):
    """
    Real-Time AI Synthesis & In-Memory RAG:
    Streams live-retrieved government documents / acts into memory (no persistent mock files)
    and executes real-time statutory clause extraction, legal cross-referencing,
    and policy impact assessment for Gujarat regulations.
    """
    try:
        return synthesize_live_gujarat_document(
            doc_id=payload.doc_id,
            document_url=payload.document_url,
            topic=payload.topic,
            user_query=payload.user_query
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/kb/synthesize")
def api_kb_synthesize(payload: SynthesisRequest):
    """
    Unified synthesis endpoint: delegates to live in-memory RAG pipeline.
    """
    try:
        doc_id = payload.doc_ids[0] if (payload.doc_ids and len(payload.doc_ids) > 0) else None
        return synthesize_live_gujarat_document(
            doc_id=doc_id,
            topic=payload.topic,
            user_query=payload.question
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------------------------------------------------------------
# Frontend Dashboard with MapLibre GL JS Integration (/ and /map)
# -----------------------------------------------------------------------------
@app.get("/map", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
def index_ui():
    """GIGW 3.0 National Geoportal Executive Dashboard with MapLibre GL JS and Esri 10m LULC."""
    return render_gov_portal_html()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
