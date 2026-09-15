"""
Bharatlas Administrative Boundaries, SHRUG Village Telemetry, and Spatial Land Litigations
National Land Governance Platform - Ministry of Rural Development, Department of Land Resources (DoLR)

Zero-Bhuvan, Zero-Setu Architecture:
- Bharatlas LGD Boundary Extracts (Gujarat & Odisha)
- SHRUG (Development Data Lab) Socioeconomic Village Telemetry
- Land Conflict Watch / Justice Hub Spatial Land Litigations
"""

from typing import Dict, Any, List

# ---------------------------------------------------------------------------
# 1. Bharatlas LGD Administrative Boundaries (GeoJSON FeatureCollections)
# ---------------------------------------------------------------------------

BHARATLAS_STATES_GEOJSON: Dict[str, Any] = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "state-gj-24",
            "properties": {
                "level": "state",
                "state": "Gujarat",
                "state_code": "GJ",
                "lgd_code": "24",
                "capital": "Gandhinagar",
                "total_districts": 33,
                "active_disputes": 248,
                "disputed_hectares": "42,800 Ha",
                "shrug_villages_indexed": 18240,
                "governing_code": "Gujarat Land Revenue Code 1879 & Jantri Manual 2023"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [68.15, 23.68], [69.10, 24.55], [71.12, 24.70], [72.45, 24.32],
                        [73.55, 24.20], [74.25, 23.10], [74.05, 21.80], [73.80, 21.10],
                        [72.85, 20.25], [72.65, 20.80], [72.20, 21.40], [71.50, 20.75],
                        [70.10, 20.85], [69.05, 22.25], [69.20, 22.95], [68.30, 23.25],
                        [68.15, 23.68]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "state-or-21",
            "properties": {
                "level": "state",
                "state": "Odisha",
                "state_code": "OR",
                "lgd_code": "21",
                "capital": "Bhubaneswar",
                "total_districts": 30,
                "active_disputes": 312,
                "disputed_hectares": "58,400 Ha",
                "shrug_villages_indexed": 51313,
                "governing_code": "Odisha Land Reforms Act 1960 & Forest Rights Directives"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [81.40, 18.20], [82.50, 19.10], [83.30, 19.80], [84.10, 19.20],
                        [85.15, 19.70], [86.70, 20.60], [87.40, 21.50], [86.80, 22.35],
                        [85.30, 22.30], [84.15, 22.50], [83.30, 21.80], [82.60, 21.10],
                        [82.20, 20.10], [81.70, 18.90], [81.40, 18.20]
                    ]
                ]
            }
        }
    ]
}

BHARATLAS_DISTRICTS_GEOJSON: Dict[str, Any] = {
    "type": "FeatureCollection",
    "features": [
        # Gujarat Districts
        {
            "type": "Feature",
            "id": "dist-gj-gandhinagar",
            "properties": {
                "name": "Gandhinagar",
                "state": "Gujarat",
                "lgd_code": "442",
                "category": "Capital Corridor & Urban Transition",
                "active_conflicts": 4,
                "avg_agricultural_pct": 68.4,
                "avg_electrification": 99.2,
                "shrug_villages": 284,
                "jantri_circle_rate_growth": "+12.4% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.50, 23.10], [72.85, 23.12], [72.95, 23.35], [72.65, 23.45],
                        [72.48, 23.30], [72.50, 23.10]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-gj-ahmedabad",
            "properties": {
                "name": "Ahmedabad",
                "state": "Gujarat",
                "lgd_code": "438",
                "category": "Industrial & Freight Corridor",
                "active_conflicts": 12,
                "avg_agricultural_pct": 59.1,
                "avg_electrification": 98.7,
                "shrug_villages": 542,
                "jantri_circle_rate_growth": "+18.2% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [71.80, 22.60], [72.40, 22.45], [72.65, 23.00], [72.35, 23.40],
                        [71.70, 23.20], [71.80, 22.60]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-gj-surat",
            "properties": {
                "name": "Surat",
                "state": "Gujarat",
                "lgd_code": "465",
                "category": "Coastal & Textile Manufacturing Hub",
                "active_conflicts": 7,
                "avg_agricultural_pct": 52.3,
                "avg_electrification": 99.5,
                "shrug_villages": 710,
                "jantri_circle_rate_growth": "+15.6% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.65, 20.90], [73.20, 20.95], [73.30, 21.45], [72.75, 21.50],
                        [72.55, 21.15], [72.65, 20.90]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-gj-kachchh",
            "properties": {
                "name": "Kachchh",
                "state": "Gujarat",
                "lgd_code": "451",
                "category": "Arid Grazing Commons & Renewable Parks",
                "active_conflicts": 9,
                "avg_agricultural_pct": 34.2,
                "avg_electrification": 94.1,
                "shrug_villages": 912,
                "jantri_circle_rate_growth": "+8.1% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [68.50, 23.10], [70.50, 23.10], [71.20, 23.85], [70.80, 24.40],
                        [69.00, 24.20], [68.50, 23.10]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-gj-vadodara",
            "properties": {
                "name": "Vadodara",
                "state": "Gujarat",
                "lgd_code": "468",
                "category": "Chemical & Petrochemical Belt",
                "active_conflicts": 5,
                "avg_agricultural_pct": 61.5,
                "avg_electrification": 99.1,
                "shrug_villages": 678,
                "jantri_circle_rate_growth": "+11.3% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.90, 21.90], [73.50, 21.95], [73.65, 22.50], [73.10, 22.60],
                        [72.90, 21.90]
                    ]
                ]
            }
        },

        # Odisha Districts
        {
            "type": "Feature",
            "id": "dist-or-khordha",
            "properties": {
                "name": "Khordha",
                "state": "Odisha",
                "lgd_code": "358",
                "category": "Capital Region & Coastal Agrarian",
                "active_conflicts": 6,
                "avg_agricultural_pct": 58.7,
                "avg_electrification": 97.4,
                "shrug_villages": 1358,
                "jantri_circle_rate_growth": "+14.2% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [85.40, 19.90], [85.95, 20.05], [86.05, 20.40], [85.50, 20.45],
                        [85.15, 20.10], [85.40, 19.90]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-or-cuttack",
            "properties": {
                "name": "Cuttack",
                "state": "Odisha",
                "lgd_code": "346",
                "category": "Mahanadi Riparian Basin & Delta Commons",
                "active_conflicts": 8,
                "avg_agricultural_pct": 64.1,
                "avg_electrification": 96.8,
                "shrug_villages": 1840,
                "jantri_circle_rate_growth": "+10.5% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [85.50, 20.40], [86.10, 20.42], [86.25, 20.70], [85.70, 20.80],
                        [85.40, 20.55], [85.50, 20.40]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-or-sundargarh",
            "properties": {
                "name": "Sundargarh",
                "state": "Odisha",
                "lgd_code": "366",
                "category": "Mineral-Rich Tribal Belt & Scheduled V Area",
                "active_conflicts": 14,
                "avg_agricultural_pct": 41.2,
                "avg_electrification": 89.6,
                "shrug_villages": 1695,
                "jantri_circle_rate_growth": "+7.8% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [83.80, 21.80], [85.20, 21.90], [85.35, 22.45], [84.20, 22.50],
                        [83.70, 22.10], [83.80, 21.80]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-or-rayagada",
            "properties": {
                "name": "Rayagada",
                "state": "Odisha",
                "lgd_code": "364",
                "category": "Indigenous Dongria Kondh & Forest Rights",
                "active_conflicts": 11,
                "avg_agricultural_pct": 36.8,
                "avg_electrification": 84.3,
                "shrug_villages": 2460,
                "jantri_circle_rate_growth": "+6.4% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [83.10, 18.90], [83.70, 19.10], [83.95, 19.70], [83.30, 19.80],
                        [82.90, 19.25], [83.10, 18.90]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "dist-or-puri",
            "properties": {
                "name": "Puri",
                "state": "Odisha",
                "lgd_code": "362",
                "category": "Coastal Lagoon & Chilika Ecological Commons",
                "active_conflicts": 5,
                "avg_agricultural_pct": 69.3,
                "avg_electrification": 95.2,
                "shrug_villages": 1520,
                "jantri_circle_rate_growth": "+13.1% YoY"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [85.20, 19.65], [86.00, 19.75], [86.15, 20.05], [85.50, 20.00],
                        [85.10, 19.80], [85.20, 19.65]
                    ]
                ]
            }
        }
    ]
}


# ---------------------------------------------------------------------------
# 2. SHRUG (Development Data Lab) Granular Village Telemetry (10 Records)
# ---------------------------------------------------------------------------

SHRUG_VILLAGE_RECORDS: List[Dict[str, Any]] = [
    # Gujarat Villages (5)
    {
        "shrid": "shrug-gj-442-0012",
        "village_name": "Randesan",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "lgd_code": "511240",
        "lat": 23.1852,
        "lon": 72.6341,
        "population": 4820,
        "agricultural_land_pct": 62.4,
        "forest_area_pct": 4.1,
        "electrification_score": 99.4,
        "night_light_index": 28.6,
        "female_literacy_pct": 82.5,
        "secc_poverty_pct": 8.2,
        "rural_urban_class": "Peri-Urban GIFT City Corridor",
        "ulpin_saturation_pct": 98.4,
        "svamitva_cards_issued": 842,
        "linked_disputes_count": 1,
        "primary_crop": "Castor, Cotton & Wheat"
    },
    {
        "shrid": "shrug-gj-442-0089",
        "village_name": "Pethapur",
        "district": "Gandhinagar",
        "state": "Gujarat",
        "lgd_code": "511289",
        "lat": 23.2550,
        "lon": 72.6712,
        "population": 6120,
        "agricultural_land_pct": 71.8,
        "forest_area_pct": 2.8,
        "electrification_score": 98.9,
        "night_light_index": 22.4,
        "female_literacy_pct": 79.1,
        "secc_poverty_pct": 11.6,
        "rural_urban_class": "Agrarian Craft Cluster",
        "ulpin_saturation_pct": 94.2,
        "svamitva_cards_issued": 1104,
        "linked_disputes_count": 0,
        "primary_crop": "Millets, Mustard & Vegetables"
    },
    {
        "shrid": "shrug-gj-438-0245",
        "village_name": "Sanand Rural",
        "district": "Ahmedabad",
        "state": "Gujarat",
        "lgd_code": "511450",
        "lat": 22.9868,
        "lon": 72.3789,
        "population": 12850,
        "agricultural_land_pct": 48.5,
        "forest_area_pct": 1.2,
        "electrification_score": 99.8,
        "night_light_index": 38.2,
        "female_literacy_pct": 81.4,
        "secc_poverty_pct": 12.3,
        "rural_urban_class": "Automobile Manufacturing Hub",
        "ulpin_saturation_pct": 92.1,
        "svamitva_cards_issued": 1650,
        "linked_disputes_count": 2,
        "primary_crop": "Paddy, Cotton & Non-Agri SEZ"
    },
    {
        "shrid": "shrug-gj-438-0412",
        "village_name": "Bavla Gam",
        "district": "Ahmedabad",
        "state": "Gujarat",
        "lgd_code": "511612",
        "lat": 22.8340,
        "lon": 72.3610,
        "population": 8420,
        "agricultural_land_pct": 78.6,
        "forest_area_pct": 0.8,
        "electrification_score": 97.6,
        "night_light_index": 18.5,
        "female_literacy_pct": 74.8,
        "secc_poverty_pct": 14.7,
        "rural_urban_class": "Rice Milling & Agrarian Basin",
        "ulpin_saturation_pct": 89.5,
        "svamitva_cards_issued": 920,
        "linked_disputes_count": 1,
        "primary_crop": "Paddy & Wheat"
    },
    {
        "shrid": "shrug-gj-451-0810",
        "village_name": "Bhujodi",
        "district": "Kachchh",
        "state": "Gujarat",
        "lgd_code": "508100",
        "lat": 23.2384,
        "lon": 69.7214,
        "population": 5140,
        "agricultural_land_pct": 31.4,
        "forest_area_pct": 8.9,
        "electrification_score": 95.1,
        "night_light_index": 14.8,
        "female_literacy_pct": 71.2,
        "secc_poverty_pct": 19.8,
        "rural_urban_class": "Arid Pastoralist & Weaving Settlement",
        "ulpin_saturation_pct": 82.3,
        "svamitva_cards_issued": 740,
        "linked_disputes_count": 1,
        "primary_crop": "Guar, Bajra & Date Palm"
    },

    # Odisha Villages (5)
    {
        "shrid": "shrug-or-358-0044",
        "village_name": "Jatni Rural",
        "district": "Khordha",
        "state": "Odisha",
        "lgd_code": "391440",
        "lat": 20.1582,
        "lon": 85.7061,
        "population": 9100,
        "agricultural_land_pct": 54.8,
        "forest_area_pct": 6.2,
        "electrification_score": 98.1,
        "night_light_index": 26.4,
        "female_literacy_pct": 84.6,
        "secc_poverty_pct": 15.2,
        "rural_urban_class": "Rail Junction & Education Corridor",
        "ulpin_saturation_pct": 91.0,
        "svamitva_cards_issued": 1280,
        "linked_disputes_count": 0,
        "primary_crop": "Paddy, Pulses & Horticulture"
    },
    {
        "shrid": "shrug-or-346-0182",
        "village_name": "Banki Kasba",
        "district": "Cuttack",
        "state": "Odisha",
        "lgd_code": "392182",
        "lat": 20.3785,
        "lon": 85.5320,
        "population": 7240,
        "agricultural_land_pct": 74.2,
        "forest_area_pct": 11.5,
        "electrification_score": 94.7,
        "night_light_index": 16.2,
        "female_literacy_pct": 76.8,
        "secc_poverty_pct": 21.4,
        "rural_urban_class": "Riparian Alluvial Valley",
        "ulpin_saturation_pct": 86.4,
        "svamitva_cards_issued": 890,
        "linked_disputes_count": 1,
        "primary_crop": "Sugarcane, Paddy & Vegetables"
    },
    {
        "shrid": "shrug-or-364-0715",
        "village_name": "Muniguda Forest Fringe",
        "district": "Rayagada",
        "state": "Odisha",
        "lgd_code": "394715",
        "lat": 19.6240,
        "lon": 83.4910,
        "population": 3680,
        "agricultural_land_pct": 28.9,
        "forest_area_pct": 59.4,
        "electrification_score": 81.2,
        "night_light_index": 6.8,
        "female_literacy_pct": 52.4,
        "secc_poverty_pct": 46.8,
        "rural_urban_class": "Indigenous Forest Dwelling Settlement",
        "ulpin_saturation_pct": 58.7,
        "svamitva_cards_issued": 412,
        "linked_disputes_count": 1,
        "primary_crop": "Minor Forest Produce (MFP), Millets & Turmeric"
    },
    {
        "shrid": "shrug-or-366-0390",
        "village_name": "Hemgir Coal Basin",
        "district": "Sundargarh",
        "state": "Odisha",
        "lgd_code": "396390",
        "lat": 21.9420,
        "lon": 83.7150,
        "population": 5420,
        "agricultural_land_pct": 34.5,
        "forest_area_pct": 42.1,
        "electrification_score": 87.5,
        "night_light_index": 19.4,
        "female_literacy_pct": 64.2,
        "secc_poverty_pct": 38.5,
        "rural_urban_class": "Mining Expansion & Tribal Cluster",
        "ulpin_saturation_pct": 64.2,
        "svamitva_cards_issued": 580,
        "linked_disputes_count": 1,
        "primary_crop": "Paddy, Oilseeds & Coal Lease Land"
    },
    {
        "shrid": "shrug-or-362-0112",
        "village_name": "Satapada Chilika",
        "district": "Puri",
        "state": "Odisha",
        "lgd_code": "397112",
        "lat": 19.6780,
        "lon": 85.4320,
        "population": 4210,
        "agricultural_land_pct": 51.2,
        "forest_area_pct": 14.8,
        "electrification_score": 93.4,
        "night_light_index": 12.1,
        "female_literacy_pct": 73.1,
        "secc_poverty_pct": 24.6,
        "rural_urban_class": "Coastal Fishery & Wetland Commons",
        "ulpin_saturation_pct": 84.1,
        "svamitva_cards_issued": 695,
        "linked_disputes_count": 0,
        "primary_crop": "Brackish Aquaculture & Wet Paddy"
    }
]


# ---------------------------------------------------------------------------
# 3. Spatial Land Litigations (Land Conflict Watch / Justice Hub Open Schema)
# ---------------------------------------------------------------------------

SPATIAL_LAND_LITIGATIONS: List[Dict[str, Any]] = [
    {
        "conflict_id": "LCW-GJ-438-001",
        "title": "Dholera Special Investment Region (SIR) Freight Corridor Acquisition",
        "state": "Gujarat",
        "district": "Ahmedabad",
        "lgd_code": "438",
        "lat": 22.2450,
        "lon": 72.1950,
        "act_invoked": "RFCTLARR Act 2013, Section 24(2) & Gujarat Land Revenue Code",
        "affected_hectares": 4200,
        "affected_families": 3850,
        "court_forum": "Supreme Court of India (Appellate Jurisdiction)",
        "legal_status": "STAYED / CONSTITUTION_BENCH_BENCHMARK",
        "primary_trigger": "Retrospective Lapsing of Acquisition Proceedings & Compensation Deposit Validity",
        "case_citation": "Civil Appeal No. 20982/2020 (Manoharlal Precedent Applied)",
        "conflict_type": "Infrastructure & Industrial Corridor",
        "summary": "Landowners across 22 villages challenged acquisition initiated under the 1894 Act, asserting Section 24(2) lapsing due to physical possession disputes and non-deposit into bank accounts. Supreme Court upheld possession via Panchnama.",
        "related_policy_id": "doc-rfctlarr-sc-302"
    },
    {
        "conflict_id": "LCW-OR-364-002",
        "title": "Niyamgiri Bauxite Mining Lease & Dongria Kondh Sacred Forest Rights",
        "state": "Odisha",
        "district": "Rayagada",
        "lgd_code": "364",
        "lat": 19.6420,
        "lon": 83.4210,
        "act_invoked": "Scheduled Tribes and Other Traditional Forest Dwellers (FRA 2006)",
        "affected_hectares": 1850,
        "affected_families": 1420,
        "court_forum": "Supreme Court of India / MoEFCC Forest Advisory Committee",
        "legal_status": "RESOLVED / GRAM_SABHA_REJECTION_UPHELD",
        "primary_trigger": "Non-recognition of Community Forest Rights (CFR) & Gram Sabha Sovereign Veto",
        "case_citation": "Orissa Mining Corporation v. MoEFCC (2013) 6 SCC 476",
        "conflict_type": "Mining & Indigenous Forest Rights",
        "summary": "Historical 12 Gram Sabha unanimous rejections of open-cast bauxite mining in sacred Niyamgiri hills. Established inviolable statutory primacy of Gram Sabha under Forest Rights Act.",
        "related_policy_id": "doc-fra-305"
    },
    {
        "conflict_id": "LCW-OR-346-003",
        "title": "Mahanadi Riverbed Mechanized Sand Mining & Riparian Commons Encroachment",
        "state": "Odisha",
        "district": "Cuttack",
        "lgd_code": "346",
        "lat": 20.4650,
        "lon": 85.8790,
        "act_invoked": "Environment Protection Act & Odisha Minor Minerals Concession Rules",
        "affected_hectares": 620,
        "affected_families": 890,
        "court_forum": "National Green Tribunal (Eastern Zone Bench)",
        "legal_status": "PENDING_TRIBUNAL_INSPECTION",
        "primary_trigger": "Riverbed Morphological Degradation & Floodplain Common Lands Encroachment",
        "case_citation": "NGT OA No. 48/2023 (EZ)",
        "conflict_type": "Ecological Commons & Riverine Extraction",
        "summary": "Local agrarian community litigation against mechanized riverbed quarrying breaching 500-meter safety buffer zones near Cuttack embankments.",
        "related_policy_id": "doc-nrsc-lulc-306"
    },
    {
        "conflict_id": "LCW-GJ-438-004",
        "title": "Sanand Industrial Zone Agricultural Parcel Re-Classification Disputes",
        "state": "Gujarat",
        "district": "Ahmedabad",
        "lgd_code": "438",
        "lat": 22.9750,
        "lon": 72.3850,
        "act_invoked": "Gujarat Tenancy and Agricultural Lands Act 1948 & Jantri Manual",
        "affected_hectares": 1140,
        "affected_families": 640,
        "court_forum": "High Court of Gujarat (Special Civil Application)",
        "legal_status": "PENDING_HEARING",
        "primary_trigger": "Non-Agricultural (NA) Land Conversion Delay & Jantri Valuation Discrepancies",
        "case_citation": "SCA No. 14208/2022",
        "conflict_type": "Tenancy Reforms & Urban Transition",
        "summary": "Farmers challenging valuation differentials in circle rates during urban zoning conversion for automotive suppliers.",
        "related_policy_id": "doc-gujarat-jantri-307"
    },
    {
        "conflict_id": "LCW-OR-366-005",
        "title": "Sundargarh Coal Mining Corridor Displacement & R&R Entitlements",
        "state": "Odisha",
        "district": "Sundargarh",
        "lgd_code": "366",
        "lat": 21.9850,
        "lon": 83.8240,
        "act_invoked": "RFCTLARR 2013, Chapter V & Coal Bearing Areas Act 1957",
        "affected_hectares": 3100,
        "affected_families": 2780,
        "court_forum": "High Court of Orissa (Writ Jurisdiction)",
        "legal_status": "INTERIM_COMPLIANCE_MONITORED",
        "primary_trigger": "Incomplete Resettlement Colony Handover & Employment Entitlements Default",
        "case_citation": "W.P.(C) 19842/2021",
        "conflict_type": "Energy Corridor & Resettlement Default",
        "summary": "Tribal families protesting eviction prior to complete statutory execution of rehabilitation entitlements under Schedule II of RFCTLARR.",
        "related_policy_id": "doc-lcw-synthesis-310"
    }
]

# ---------------------------------------------------------------------------
# 4. Postal Code Zones (DataMeet / Bharatlas Postal GeoJSON Extracts)
# ---------------------------------------------------------------------------

BHARATLAS_POSTAL_GEOJSON: Dict[str, Any] = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "pincode-382010",
            "properties": {
                "pincode": "382010",
                "locality": "Gandhinagar Sector 10-21 & Administrative Enclave",
                "district": "Gandhinagar",
                "state": "Gujarat",
                "circle": "Gujarat Circle",
                "taluka": "Gandhinagar",
                "category": "Urban Administrative Zone",
                "bbox": [72.610, 23.210, 72.670, 23.250]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.610, 23.210], [72.670, 23.215], [72.665, 23.250],
                        [72.615, 23.245], [72.610, 23.210]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "pincode-380001",
            "properties": {
                "pincode": "380001",
                "locality": "Ahmedabad Central (Bhadra & Sabarmati Riverfront)",
                "district": "Ahmedabad",
                "state": "Gujarat",
                "circle": "Gujarat Circle",
                "taluka": "Ahmedabad City",
                "category": "Historic Walled City & Commercial Core",
                "bbox": [72.560, 23.010, 72.610, 23.050]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.560, 23.010], [72.610, 23.015], [72.605, 23.050],
                        [72.565, 23.045], [72.560, 23.010]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "pincode-382421",
            "properties": {
                "pincode": "382421",
                "locality": "Sanand Industrial GIDC & Agro-Fringe",
                "district": "Ahmedabad",
                "state": "Gujarat",
                "circle": "Gujarat Circle",
                "taluka": "Sanand",
                "category": "Industrial-Agrarian Transition Cluster",
                "bbox": [72.330, 22.950, 72.410, 23.030]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.330, 22.950], [72.410, 22.955], [72.405, 23.030],
                        [72.335, 23.025], [72.330, 22.950]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "pincode-395001",
            "properties": {
                "pincode": "395001",
                "locality": "Surat Chowk Bazar & Textile Hub",
                "district": "Surat",
                "state": "Gujarat",
                "circle": "Gujarat Circle",
                "taluka": "Surat City",
                "category": "Diamond & Textile Urban Core",
                "bbox": [72.800, 21.180, 72.860, 21.220]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.800, 21.180], [72.860, 21.185], [72.855, 21.220],
                        [72.805, 21.215], [72.800, 21.180]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "pincode-751001",
            "properties": {
                "pincode": "751001",
                "locality": "Bhubaneswar Secretariat & Capital Enclave",
                "district": "Khordha",
                "state": "Odisha",
                "circle": "Odisha Circle",
                "taluka": "Bhubaneswar",
                "category": "State Administrative Center",
                "bbox": [85.800, 20.270, 85.860, 20.320]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [85.800, 20.270], [85.860, 20.275], [85.855, 20.320],
                        [85.805, 20.315], [85.800, 20.270]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "pincode-753001",
            "properties": {
                "pincode": "753001",
                "locality": "Cuttack Buxi Bazar & High Court Sector",
                "district": "Cuttack",
                "state": "Odisha",
                "circle": "Odisha Circle",
                "taluka": "Cuttack Sadar",
                "category": "Riparian Judicial & Commercial Basin",
                "bbox": [85.850, 20.450, 85.910, 20.490]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [85.850, 20.450], [85.910, 20.455], [85.905, 20.490],
                        [85.855, 20.485], [85.850, 20.450]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "pincode-110001",
            "properties": {
                "pincode": "110001",
                "locality": "New Delhi Central (Connaught Place & Parliament)",
                "district": "New Delhi",
                "state": "Delhi",
                "circle": "Delhi Circle",
                "taluka": "Chanakyapuri",
                "category": "National Capital Heritage & Institutional Core",
                "bbox": [77.200, 28.620, 77.240, 28.650]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [77.200, 28.620], [77.240, 28.625], [77.235, 28.650],
                        [77.205, 28.645], [77.200, 28.620]
                    ]
                ]
            }
        }
    ]
}

# ---------------------------------------------------------------------------
# 5. Village Boundary Polygons (SHRUG Cadastral Framework)
# ---------------------------------------------------------------------------

BHARATLAS_VILLAGES_GEOJSON: Dict[str, Any] = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "village-shrug-gj-442-0012",
            "properties": {
                "village_name": "Koba",
                "shrid": "shrug-gj-442-0012",
                "district": "Gandhinagar",
                "state": "Gujarat",
                "census_code_2011": "511420",
                "lgd_code": "163420",
                "bbox": [72.610, 23.130, 72.660, 23.165]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.615, 23.135], [72.655, 23.138], [72.650, 23.162],
                        [72.620, 23.160], [72.615, 23.135]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "village-shrug-gj-442-0015",
            "properties": {
                "village_name": "Sargasan",
                "shrid": "shrug-gj-442-0015",
                "district": "Gandhinagar",
                "state": "Gujarat",
                "census_code_2011": "511425",
                "lgd_code": "163425",
                "bbox": [72.590, 23.170, 72.635, 23.205]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.595, 23.175], [72.630, 23.178], [72.625, 23.202],
                        [72.600, 23.200], [72.595, 23.175]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "village-shrug-gj-438-0088",
            "properties": {
                "village_name": "Sanand Rural",
                "shrid": "shrug-gj-438-0088",
                "district": "Ahmedabad",
                "state": "Gujarat",
                "census_code_2011": "512340",
                "lgd_code": "164210",
                "bbox": [72.340, 22.960, 72.395, 23.005]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.345, 22.965], [72.390, 22.968], [72.385, 23.002],
                        [72.350, 22.998], [72.345, 22.965]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "village-shrug-gj-438-0120",
            "properties": {
                "village_name": "Dholera Central",
                "shrid": "shrug-gj-438-0120",
                "district": "Ahmedabad",
                "state": "Gujarat",
                "census_code_2011": "512890",
                "lgd_code": "164550",
                "bbox": [72.170, 22.220, 72.230, 22.270]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.175, 22.225], [72.225, 22.228], [72.220, 22.268],
                        [72.180, 22.265], [72.175, 22.225]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "village-shrug-or-364-0019",
            "properties": {
                "village_name": "Muniguda Foothills",
                "shrid": "shrug-or-364-0019",
                "district": "Rayagada",
                "state": "Odisha",
                "census_code_2011": "426110",
                "lgd_code": "128450",
                "bbox": [83.470, 19.610, 83.530, 19.660]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [83.475, 19.615], [83.525, 19.618], [83.520, 19.658],
                        [83.480, 19.655], [83.475, 19.615]
                    ]
                ]
            }
        }
    ]
}

# ---------------------------------------------------------------------------
# 6. City / Municipal Boundaries
# ---------------------------------------------------------------------------

BHARATLAS_CITIES_GEOJSON: Dict[str, Any] = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": "city-ahmedabad",
            "properties": {
                "name": "Ahmedabad",
                "state": "Gujarat",
                "type": "Municipal Corporation",
                "bbox": [72.420, 22.860, 72.740, 23.180]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.45, 22.92], [72.68, 22.92], [72.72, 23.15],
                        [72.48, 23.14], [72.45, 22.92]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "city-gandhinagar",
            "properties": {
                "name": "Gandhinagar",
                "state": "Gujarat",
                "type": "Municipal Corporation & State Capital",
                "bbox": [72.580, 23.160, 72.710, 23.280]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.60, 23.18], [72.70, 23.18], [72.69, 23.27],
                        [72.59, 23.26], [72.60, 23.18]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "city-surat",
            "properties": {
                "name": "Surat",
                "state": "Gujarat",
                "type": "Municipal Corporation & Port City",
                "bbox": [72.720, 21.100, 72.930, 21.260]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [72.75, 21.12], [72.91, 21.13], [72.89, 21.25],
                        [72.74, 21.24], [72.75, 21.12]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "city-bhubaneswar",
            "properties": {
                "name": "Bhubaneswar",
                "state": "Odisha",
                "type": "Municipal Corporation & State Capital",
                "bbox": [85.760, 20.210, 85.900, 20.360]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [85.78, 20.23], [85.88, 20.24], [85.87, 20.35],
                        [85.77, 20.34], [85.78, 20.23]
                    ]
                ]
            }
        },
        {
            "type": "Feature",
            "id": "city-cuttack",
            "properties": {
                "name": "Cuttack",
                "state": "Odisha",
                "type": "Municipal Corporation & Judicial Capital",
                "bbox": [85.810, 20.420, 85.950, 20.530]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [85.83, 20.44], [85.93, 20.44], [85.92, 20.52],
                        [85.82, 20.51], [85.83, 20.44]
                    ]
                ]
            }
        }
    ]
}

# ---------------------------------------------------------------------------
# 7. Comprehensive Jurisdiction Intelligence Dossier (4 Analytical Tabs)
# ---------------------------------------------------------------------------

JURISDICTION_METRICS_MAP: Dict[str, Any] = {
    # Default National fallback
    "national": {
        "demographics": {
            "title": "National Cadastral Benchmark (All India)",
            "population": 1428627663,
            "gender_ratio": 948,
            "households": 312540000,
            "rural_urban_class": "Mixed Continental Cadastre (65.2% Rural)",
            "electrification_pct": 98.4,
            "female_literacy_pct": 74.8,
            "agri_workforce_pct": 46.5
        },
        "disputes": {
            "active_disputes_count": 8420,
            "disputed_hectares": "3,420,000 Ha",
            "acts_invoked": [
                {"statute": "RFCTLARR Act 2013 (Section 24(2))", "count": 3410},
                {"statute": "Scheduled Tribes Forest Rights Act 2006", "count": 1820},
                {"statute": "State Tenancy & Agricultural Lands Acts", "count": 2190},
                {"statute": "Environment Protection & Riverbed Commons", "count": 1000}
            ],
            "landmark_precedents": [
                {
                    "id": "doc-rfctlarr-sc-302",
                    "title": "Supreme Court Constitutional Bench Judgment on Section 24(2) RFCTLARR Act 2013",
                    "authority": "Supreme Court of India (Constitution Bench)",
                    "citation": "Indore Development Authority v. Manoharlal (2020) 8 SCC 129",
                    "pdf_url": "https://main.sci.gov.in/supremecourt/2020/20982/20982_2020_3_1501_21151_Judgement_06-Mar-2020.pdf"
                },
                {
                    "id": "doc-dilrmp-301",
                    "title": "Operational Guidelines for DILRMP 3.0 (2026–2031) & Bhu-Aadhaar Integration",
                    "authority": "Department of Land Resources (DoLR), MoRD",
                    "citation": "DoLR (2026). DILRMP 3.0 Guidelines, New Delhi.",
                    "pdf_url": "https://dolr.gov.in/sites/default/files/DILRMP_Guidelines_2026.pdf"
                }
            ]
        },
        "lulc": {
            "farmland_pct": 54.2,
            "forest_pct": 21.7,
            "water_pct": 4.8,
            "built_up_pct": 8.1,
            "flooded_wetlands_pct": 3.4,
            "rangeland_pct": 7.8,
            "flood_vulnerability_index": "Moderate (Monsoon Riverine)",
            "drought_risk_index": "Seasonal Semiarid Stress"
        },
        "cadastral_reforms": {
            "dilrmp_coverage_pct": 94.8,
            "bhu_aadhaar_ulpin_coverage_pct": 87.2,
            "svamitva_status": {
                "drone_survey_completed": True,
                "map1_generated": True,
                "villages_covered": 284500,
                "property_cards_distributed": 14200000
            },
            "jantri_circle_rate_index": "National Circle Rate Index: +10.8% YoY"
        }
    },

    # Specific PIN code: 382010 (Gandhinagar)
    "pincode-382010": {
        "demographics": {
            "title": "Gandhinagar Sector 10-21 (PIN 382010)",
            "population": 128400,
            "gender_ratio": 932,
            "households": 29800,
            "rural_urban_class": "Planned Institutional Capital Sector",
            "electrification_pct": 99.8,
            "female_literacy_pct": 88.6,
            "agri_workforce_pct": 6.2
        },
        "disputes": {
            "active_disputes_count": 2,
            "disputed_hectares": "18.4 Ha",
            "acts_invoked": [
                {"statute": "Gujarat Town Planning & Urban Development Act 1976", "count": 2}
            ],
            "landmark_precedents": [
                {
                    "id": "doc-dilrmp-301",
                    "title": "Operational Guidelines for DILRMP 3.0 (2026–2031) & Bhu-Aadhaar Integration",
                    "authority": "Department of Land Resources (DoLR), MoRD",
                    "citation": "DoLR (2026). DILRMP 3.0 Guidelines, New Delhi.",
                    "pdf_url": "https://dolr.gov.in/sites/default/files/DILRMP_Guidelines_2026.pdf"
                }
            ]
        },
        "lulc": {
            "farmland_pct": 14.5,
            "forest_pct": 32.8,
            "water_pct": 6.2,
            "built_up_pct": 42.1,
            "flooded_wetlands_pct": 1.4,
            "rangeland_pct": 3.0,
            "flood_vulnerability_index": "Low (High Elevation Terrace)",
            "drought_risk_index": "Low (Canal Grid Supported)"
        },
        "cadastral_reforms": {
            "dilrmp_coverage_pct": 100.0,
            "bhu_aadhaar_ulpin_coverage_pct": 99.2,
            "svamitva_status": {
                "drone_survey_completed": True,
                "map1_generated": True,
                "villages_covered": 18,
                "property_cards_distributed": 12400
            },
            "jantri_circle_rate_index": "₹28,500/sq.m (+14.2% YoY Revision)"
        }
    },

    # Specific PIN code: 380001 (Ahmedabad Central)
    "pincode-380001": {
        "demographics": {
            "title": "Ahmedabad Central Bhadra (PIN 380001)",
            "population": 242000,
            "gender_ratio": 921,
            "households": 56200,
            "rural_urban_class": "Dense Heritage Urban Commercial Core",
            "electrification_pct": 100.0,
            "female_literacy_pct": 86.4,
            "agri_workforce_pct": 1.1
        },
        "disputes": {
            "active_disputes_count": 6,
            "disputed_hectares": "82.5 Ha",
            "acts_invoked": [
                {"statute": "Gujarat Town Planning Act & Sabarmati Riverfront Regulations", "count": 4},
                {"statute": "Wakf & Heritage Conservation By-laws", "count": 2}
            ],
            "landmark_precedents": [
                {
                    "id": "doc-gujarat-jantri-307",
                    "title": "Gujarat Land Value Determination & Cadastral Jantri Revision Manual",
                    "authority": "Revenue Department, Government of Gujarat",
                    "citation": "Revenue Dept Gujarat (2023). Jantri Revision Manual, Gandhinagar.",
                    "pdf_url": "https://revenuedepartment.gujarat.gov.in/downloads/Jantri_Revision_Manual_2023.pdf"
                }
            ]
        },
        "lulc": {
            "farmland_pct": 2.1,
            "forest_pct": 5.4,
            "water_pct": 12.8,
            "built_up_pct": 76.5,
            "flooded_wetlands_pct": 0.8,
            "rangeland_pct": 2.4,
            "flood_vulnerability_index": "Moderate (Sabarmati Controlled Barrage)",
            "drought_risk_index": "Low (Narmada Urban Supply)"
        },
        "cadastral_reforms": {
            "dilrmp_coverage_pct": 98.6,
            "bhu_aadhaar_ulpin_coverage_pct": 94.8,
            "svamitva_status": {
                "drone_survey_completed": True,
                "map1_generated": True,
                "villages_covered": 0,
                "property_cards_distributed": 28500
            },
            "jantri_circle_rate_index": "₹45,000/sq.m (+16.5% YoY)"
        }
    },

    # Specific Village: Koba (shrug-gj-442-0012)
    "village-shrug-gj-442-0012": {
        "demographics": {
            "title": "Koba Village (SHRID: shrug-gj-442-0012)",
            "population": 4820,
            "gender_ratio": 938,
            "households": 1040,
            "rural_urban_class": "Peri-Urban Corridor (GIFT City Influence)",
            "electrification_pct": 99.4,
            "female_literacy_pct": 84.1,
            "agri_workforce_pct": 42.8
        },
        "disputes": {
            "active_disputes_count": 1,
            "disputed_hectares": "14.2 Ha",
            "acts_invoked": [
                {"statute": "Gujarat Land Revenue Code 1879 (Sec 65 NA Conversion)", "count": 1}
            ],
            "landmark_precedents": [
                {
                    "id": "doc-gujarat-jantri-307",
                    "title": "Gujarat Land Value Determination & Cadastral Jantri Revision Manual",
                    "authority": "Revenue Department, Government of Gujarat",
                    "citation": "Revenue Dept Gujarat (2023). Jantri Revision Manual, Gandhinagar.",
                    "pdf_url": "https://revenuedepartment.gujarat.gov.in/downloads/Jantri_Revision_Manual_2023.pdf"
                }
            ]
        },
        "lulc": {
            "farmland_pct": 68.4,
            "forest_pct": 4.1,
            "water_pct": 3.8,
            "built_up_pct": 21.2,
            "flooded_wetlands_pct": 1.1,
            "rangeland_pct": 1.4,
            "flood_vulnerability_index": "Low (Sabarmati East Bank Escarpment)",
            "drought_risk_index": "Low (Perennial Borewell & Canal)"
        },
        "cadastral_reforms": {
            "dilrmp_coverage_pct": 99.4,
            "bhu_aadhaar_ulpin_coverage_pct": 97.8,
            "svamitva_status": {
                "drone_survey_completed": True,
                "map1_generated": True,
                "villages_covered": 1,
                "property_cards_distributed": 980
            },
            "jantri_circle_rate_index": "₹16,800/sq.m (+18.2% YoY Urban Spillover)"
        }
    }
}
