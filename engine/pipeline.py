"""
Bhumi-Niti (भूमि-नीति): Master Intelligence Pipeline
Orchestrates geocoding, live spatial extraction, legal alignment, and risk evaluation.
"""

from typing import Dict, Any
from engine.geocoder import resolve_location
from engine.spatial import query_live_spatial_footprint
from engine.legal import evaluate_regulatory_framework
from engine.risk import evaluate_risk_and_vulnerability
from engine.dossier import compile_intelligence_dossier
from engine.thematic import extract_thematic_gis_layers

def run_intelligence_pipeline(query: str, radius_km: float = 3.5) -> Dict[str, Any]:
    """
    Executes end-to-end dynamic query across all live layers.
    Raises ValueError on outside jurisdiction or unresolvable entity.
    """
    # Step 1: Geocode & Territory boundary enforcement
    geo = resolve_location(query)
    
    # Step 2: Live Geospatial Extraction
    spatial = query_live_spatial_footprint(geo["lat"], geo["lon"], radius_km=radius_km)
    
    # Step 3: Land Administration & Policy Context
    legal = evaluate_regulatory_framework(geo["hierarchy"], geo["official_name"], spatial.get("forest_ecology", {}))
    
    # Step 4: Live Dispute & Ecological Risk Signals
    risk = evaluate_risk_and_vulnerability(geo["hierarchy"], geo["lat"], geo["lon"], geo["official_name"])
    
    # Step 5: Synthesize Standardized Dossier
    dossier = compile_intelligence_dossier(geo, spatial, legal, risk)

    # Step 6: Extract Thematic GIS Layers & Inverted Spotlight Mask
    thematic = extract_thematic_gis_layers(
        lat=geo["lat"],
        lon=geo["lon"],
        radius_km=radius_km,
        official_name=geo["official_name"],
        district=geo["hierarchy"].get("district", ""),
        entity_geojson=geo.get("geojson"),
        bbox=geo.get("bbox")
    )
    dossier["thematic_layers"] = thematic
    dossier["raw_layers"]["thematic"] = thematic
    
    return dossier
