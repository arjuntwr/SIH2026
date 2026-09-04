"""
Bhumi-Niti (भूमि-नीति): Dynamic Policy & Zoning Simulation Engine
Simulates policy, land conversion (Section 65 GLRC), buffer zoning (ESZ/GIDC), and risk factors
using live geospatial data layers without synthetic mock values.
"""

from typing import Dict, Any, Optional
import math
from engine.geocoder import resolve_location
from engine.spatial import query_live_spatial_footprint
from engine.legal import evaluate_regulatory_framework
from engine.risk import evaluate_risk_and_vulnerability

def run_policy_simulation(
    query: str,
    simulation_type: str = "na_conversion",
    buffer_meters: float = 500.0,
    proposed_use: str = "Industrial / Logistics",
    target_area_sqm: float = 10000.0
) -> Dict[str, Any]:
    """
    Simulates regulatory, ecological, and procedural impact of land conversion or zoning change.
    """
    # 1. Resolve Location within Gujarat
    geo = resolve_location(query)
    lat, lon = geo["lat"], geo["lon"]
    h = geo["hierarchy"]
    district = h["district"]
    official_name = geo["official_name"]

    # 2. Extract live spatial context around buffer
    radius_km = max(1.0, buffer_meters / 1000.0)
    spatial = query_live_spatial_footprint(lat, lon, radius_km=radius_km)
    legal = evaluate_regulatory_framework(h, official_name, spatial.get("forest_ecology", {}))
    risk = evaluate_risk_and_vulnerability(h, lat, lon, official_name)

    # 3. Dynamic Feasibility Calculation
    feasibility_score = 85.0
    bottlenecks = []
    clearances_required = []

    # Check Forest / ESZ proximity
    forest_info = spatial.get("forest_ecology", {})
    if forest_info.get("is_protected"):
        feasibility_score -= 40.0
        bottlenecks.append("Site falls inside notified Eco-Sensitive Zone (ESZ) or Protected Forest boundary.")
        clearances_required.append("National Board for Wildlife (NBWL) & MoEFCC Forest Clearance under FCA 1980")
    elif forest_info.get("forest_clusters"):
        feasibility_score -= 20.0
        bottlenecks.append(f"Woodland / Reserve Forest tracts located within {buffer_meters}m buffer.")
        clearances_required.append("State Forest Department No-Objection Certificate (NOC)")

    if forest_info.get("has_grasslands_vidi"):
        feasibility_score -= 15.0
        bottlenecks.append("Reserved Vidi / Grassland classification detected in surrounding buffer.")
        clearances_required.append("Revenue Department Vidi verification & Collector De-reservation Order")

    # Check Tenancy & Conversion Legal Rules
    is_saurashtra = any("Saurashtra Gharkhed" in r for r in legal["tenancy_and_conversion_rules"])
    is_tribal = "Section 73AA" in legal["special_legislation"]

    if is_tribal:
        feasibility_score -= 35.0
        bottlenecks.append("Scheduled Area restrictions (Section 73AA GLRC): Strict ban on non-tribal alienation.")
        clearances_required.append("State Government sanction under Section 73AA (Rarely granted for private industry)")

    if is_saurashtra and proposed_use.lower() not in ["agricultural"]:
        feasibility_score -= 15.0
        bottlenecks.append("Saurashtra Gharkhed Act (1949) compliance: Non-agriculturist acquisition requires prior Collector permission (Section 54).")
        clearances_required.append("Collector Permission under Section 54 of Gharkhed Act")

    # Check Waterbody / Coastal
    distribution = spatial.get("distribution", {})
    water_pct = float(distribution.get("Waterbody / Wetland / Coast", "0%").replace("%", ""))
    if water_pct > 5.0 or "Coastal" in risk["climate_and_vulnerability"]:
        feasibility_score -= 15.0
        bottlenecks.append("Waterbody / Coastal proximity detected. High tidal or drainage buffer mandatory.")
        clearances_required.append("Gujarat Coastal Zone Management Authority (GCZMA) CRZ clearance")

    # Standard Section 65 NA Clearances
    clearances_required.append("District Collector Non-Agricultural (NA) Permission under Section 65 GLRC")
    clearances_required.append("Gujarat Pollution Control Board (GPCB) CTE/CTO Clearance")
    clearances_required.append("Town Planning / Local Development Authority (AUDA/GIDC/Panchayat) Layout Approval")

    feasibility_score = max(5.0, min(95.0, round(feasibility_score, 1)))

    # Estimate timeline based on bottlenecks
    if feasibility_score < 40:
        est_timeline_months = "18 - 36 months (High Legal & Environmental Friction)"
        risk_rating = "HIGH RESTRICTION"
    elif feasibility_score < 70:
        est_timeline_months = "9 - 18 months (Multi-Departmental Interventions)"
        risk_rating = "MODERATE FRICTION"
    else:
        est_timeline_months = "4 - 8 months (Standard Single-Window NA Conversion)"
        risk_rating = "HIGH FEASIBILITY"

    # Conversion Premium Estimate (INR per sq meter indicative revenue tariff)
    base_rate_sqm = 250.0
    if "industrial" in proposed_use.lower():
        base_rate_sqm = 450.0
    elif "commercial" in proposed_use.lower():
        base_rate_sqm = 750.0

    conversion_fee_estimate_inr = round(target_area_sqm * base_rate_sqm * (1.2 if is_saurashtra else 1.0), 2)

    return {
        "status": "success",
        "entity": geo["name"],
        "official_name": geo["official_name"],
        "hierarchy": h,
        "coordinates": {"lat": lat, "lon": lon},
        "simulation_parameters": {
            "simulation_type": simulation_type,
            "buffer_meters": buffer_meters,
            "proposed_use": proposed_use,
            "target_area_sqm": target_area_sqm
        },
        "feasibility": {
            "score_percentage": feasibility_score,
            "risk_rating": risk_rating,
            "estimated_clearance_timeline": est_timeline_months,
            "estimated_na_assessment_fee_inr": conversion_fee_estimate_inr
        },
        "statutory_bottlenecks": bottlenecks if bottlenecks else ["No high-severity statutory bans detected within direct radial envelope."],
        "required_clearances_checklist": clearances_required,
        "active_zoning_authority": legal["applicable_authority"],
        "seismic_design_requirement": risk["seismic_hazard"]
    }
