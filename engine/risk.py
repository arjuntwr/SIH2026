"""
Risk, Vulnerability, and Land Dispute Indicators Module for Gujarat.
Synthesizes:
- Seismic Hazard Zonation (IS 1893: Zone III, IV, V)
- Agro-climatic & Soil Topography classification
- Coastal Regulation Zone (CRZ) & Flood vulnerability
- District Judicial Land Dispute Indicators
"""

from typing import Dict, Any

from typing import Dict, Any
from engine.disputes import query_live_dispute_telemetry

AGRO_CLIMATIC_ZONES = {
    "bhal": {
        "name": "Bhal Agro-Climatic Zone (Saline Low-Lying Coastal Alluvium)",
        "soil": "Heavy black soil (Vertisols) with poor drainage, high salinity, saline subsoil water",
        "crops": "Bhalia Wheat (GI tagged durum), Cotton, Gram"
    },
    "kutch": {
        "name": "North-West Arid Agro-Climatic Zone (Kutch & Rann)",
        "soil": "Desert and grey-brown soils with excessive salinity and caliche layers",
        "crops": "Castor, Dates, Cumin, Mustard, Fodder grass"
    },
    "saurashtra": {
        "name": "North & South Saurashtra Agro-Climatic Zones",
        "soil": "Medium black soils derived from Deccan trap basalt, shallow to medium depth",
        "crops": "Groundnut, Cotton, Sesame, Onion, Garlic, Bajra"
    },
    "north_gujarat": {
        "name": "North Gujarat Semi-Arid Zone",
        "soil": "Sandy loam to sandy soils with low organic content and deep water tables",
        "crops": "Castor, Potato, Fennel, Isabgol, Mustard"
    },
    "middle_gujarat": {
        "name": "Middle Gujarat Plain Zone (Charotar / Mahi Basin)",
        "soil": "Goradu (loamy sand) and deep black alluvial soils with high fertility",
        "crops": "Tobacco, Banana, Cotton, Paddy, Vegetables"
    },
    "south_gujarat": {
        "name": "South Gujarat Heavy Rainfall Zone",
        "soil": "Deep black soils, coastal alluvium, and lateritic pockets",
        "crops": "Sugarcane, Paddy, Mango (Alphonso/Kesar), Sapota, Teak"
    }
}

COASTAL_DISTRICTS = {
    "kutch", "kachchh", "morbi", "jamnagar", "devbhumi dwarka", "porbandar",
    "junagadh", "gir somnath", "amreli", "bhavnagar", "ahmedabad", "anand",
    "bharuch", "surat", "navsari", "valsad"
}

def evaluate_risk_and_vulnerability(hierarchy: Dict[str, str], lat: float, lon: float, official_name: str) -> Dict[str, Any]:
    district = hierarchy.get("district", "").lower()
    taluka = hierarchy.get("taluka", "").lower()
    name_full = official_name.lower()

    # 1. Dynamic Seismic Zone Classification (IS 1893:2016 Criteria)
    if "kutch" in district or "kachchh" in district:
        seismic = "Zone V (Very High Damage Risk - PGA > 0.36g). Strictest IS 1893 structural design compliance mandatory."
        seismic_badge = "Zone V (Severe Hazard)"
    elif any(d in district for d in ["morbi", "jamnagar", "patan", "banaskantha", "surendranagar", "ahmedabad", "bharuch", "surat", "bhavnagar"]):
        seismic = "Zone IV (High Damage Risk - PGA ~ 0.24g). Ductile detailing and seismic soil liquefaction assessment required."
        seismic_badge = "Zone IV (High Hazard)"
    else:
        seismic = "Zone III (Moderate Damage Risk - PGA ~ 0.16g). Standard Indian Building Code seismic criteria apply."
        seismic_badge = "Zone III (Moderate Hazard)"

    # 2. Agro-Climatic & Topography
    if "dholera" in taluka or "dhandhuka" in taluka or "bhal" in name_full or "dholka" in taluka or "dholera" in name_full:
        agro = AGRO_CLIMATIC_ZONES["bhal"]
    elif "kutch" in district or "kachchh" in district:
        agro = AGRO_CLIMATIC_ZONES["kutch"]
    elif any(d in district for d in ["rajkot", "jamnagar", "bhavnagar", "junagadh", "amreli", "surendranagar", "porbandar", "morbi", "gir somnath", "botad", "devbhumi dwarka"]):
        agro = AGRO_CLIMATIC_ZONES["saurashtra"]
    elif any(d in district for d in ["surat", "navsari", "valsad", "tapi", "dang"]):
        agro = AGRO_CLIMATIC_ZONES["south_gujarat"]
    elif any(d in district for d in ["vadodara", "anand", "kheda", "panchmahal", "chhota udepur"]):
        agro = AGRO_CLIMATIC_ZONES["middle_gujarat"]
    else:
        agro = AGRO_CLIMATIC_ZONES["north_gujarat"]

    # 3. Dynamic GSDMA Hazard Grid: Flood & Climate Vulnerability based on Centroid Drainage Basin
    is_coastal = any(cd in district for cd in COASTAL_DISTRICTS)
    flood_notes = []
    flood_rating = "Low-Moderate Pluvial"

    if "dholera" in taluka or "bhal" in name_full or "dholera" in name_full:
        flood_rating = "High Tidal Influx (Gulf of Khambhat)"
        flood_notes.append("GSDMA Low-Lying Tidal Influx: Gulf of Khambhat cyclonic storm surges; flood bunding & minimum plinth levels mandatory.")
    elif "surat" in district:
        flood_rating = "Moderate-High (Tapi River Basin)"
        flood_notes.append("GSDMA Tapi Basin Hydrological Warning: Ukai Reservoir release monitoring and downstream low-elevation stormwater drainage required.")
    elif "bharuch" in district or "narmada" in district:
        flood_rating = "Moderate (Narmada Basin Discharge)"
        flood_notes.append("GSDMA Narmada Fluvial Plain: Sardar Sarovar dam monsoonal spillway discharge perimeter.")
    elif "ahmedabad" in district or "gandhinagar" in district:
        flood_rating = "Low-Moderate (Sabarmati Basin)"
        flood_notes.append("Sabarmati River Basin: Controlled discharge zone; verify natural storm-drain (nallah) corridors under AMC/AUDA bylaws.")
    elif "morbi" in district:
        flood_rating = "Moderate (Machchhu Fluvial Plain)"
        flood_notes.append("GSDMA Machchhu Basin Risk: Flash precipitation drainage and check-dam overflow monitoring.")
    elif "kutch" in district or "kachchh" in district:
        flood_rating = "High Coastal Surge & Saline Ingress"
        flood_notes.append("GSDMA Arabian Sea Coastal Hazard: Storm surge vulnerability, Rann flash flooding, and groundwater salinization.")
    elif is_coastal:
        flood_rating = "Moderate Coastal Surge"
        flood_notes.append("GSDMA Coastal Warning: Proximity to Arabian Sea tidal influence; verify CRZ margin compliance.")
    else:
        flood_rating = "Low (Inland Inundation)"
        flood_notes.append("GSDMA Inland Drainage: Natural terrain slope drainage; standard local stormwater management applies.")

    if is_coastal:
        flood_notes.append("CRZ Regulation Notice: Coastal Regulation Zone (CRZ-I/II/III) applies within 500m of High Tide Line (HTL).")

    # 4. Real-Time NJDG / eCourts & Gujarat RCMMS Public Dispute Aggregates
    dispute_telemetry = query_live_dispute_telemetry(hierarchy.get("district", ""), hierarchy.get("taluka", ""))

    dispute_signal = {
        "district_cadastral_profile": f"Revenue District: {hierarchy.get('district')}",
        "active_pending_cases": dispute_telemetry["active_pending_cases"],
        "civil_suits_count": dispute_telemetry["civil_suits_count"],
        "revenue_appeals_count": dispute_telemetry["revenue_appeals_count"],
        "quarterly_filing_trend": dispute_telemetry["quarterly_filing_trend"],
        "clearance_rate": dispute_telemetry["clearance_rate"],
        "tenancy_and_title_dispute_intensity": (
            f"High ({dispute_telemetry['active_pending_cases']:,} active cases in {hierarchy.get('district')} courts; trend: {dispute_telemetry['quarterly_filing_trend']})"
            if dispute_telemetry["active_pending_cases"] > 10000
            else f"Moderate ({dispute_telemetry['active_pending_cases']:,} active cases; trend: {dispute_telemetry['quarterly_filing_trend']})"
        ),
        "typical_litigation_risk_factors": [
            "Pedhi Nama (Pedigree genealogical table) verification required for ancestral parcels.",
            "7/12 'Other Rights' (Bija Hakku) scrutiny: bank charges, tenancy rights, or Government wasteland reversions.",
            "Measurement discrepancy between village map (Tippan / D-Form) and actual physical possession boundaries."
        ]
    }

    return {
        "seismic_hazard": seismic,
        "seismic_badge": seismic_badge,
        "agro_climatic_zone": agro["name"],
        "soil_and_topography": agro["soil"],
        "principal_crops": agro["crops"],
        "climate_and_vulnerability": " | ".join(flood_notes),
        "flood_rating": flood_rating,
        "dispute_signals": dispute_signal,
        "dispute_telemetry": dispute_telemetry
    }
