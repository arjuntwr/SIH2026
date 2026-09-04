from typing import Dict, Any

SCHEDULED_TRIBAL_DISTRICTS = {
    "dang", "the dangs", "dahod", "chhota udepur", "chhotaudepur", "narmada", 
    "tapi", "panchmahal", "panch mahals", "sabarkantha", "banaskantha", 
    "aravalli", "valsad", "navsari", "bharuch"
}

SAURASHTRA_DISTRICTS = {
    "rajkot", "jamnagar", "bhavnagar", "junagadh", "amreli", "surendranagar", 
    "porbandar", "morbi", "devbhumi dwarka", "gir somnath", "botad"
}

KUTCH_DISTRICTS = {"kutch", "kachchh"}

def evaluate_regulatory_framework(hierarchy: Dict[str, str], official_name: str, ecology: Dict[str, Any]) -> Dict[str, Any]:
    district = hierarchy.get("district", "").lower()
    taluka = hierarchy.get("taluka", "").lower()
    village = hierarchy.get("village_ward", "").lower()
    state = hierarchy.get("state", "Gujarat").lower()
    name_full = official_name.lower()

    # 0. National Multi-State Jurisdiction Support (UP & Maharashtra Demo)
    if "uttar pradesh" in state or "gautam buddha" in district or "noida" in name_full:
        authority = "New Okhla Industrial Development Authority (NOIDA) / YEIDA"
        authority_short = "NOIDA / YEIDA"
        special_act = "UP Industrial Area Development Act, 1976 & UP Revenue Code, 2006"
        jantri_tier = "Circle Rate Tier 1: Premium NCR Commercial & Industrial Hub (Sectoral Master Plan)"
        na_prereqs = [
            "Section 80 Declaration under UP Revenue Code 2006 (Agricultural to Non-Agricultural status).",
            "NOIDA Master Plan 2041 zoning conformance and building layout sanction.",
            "State Environmental Impact Assessment Authority (SEIAA UP) clearance for built-up > 20,000 sqm.",
            "NOC from Uttar Pradesh Ground Water Department and Forest Department buffer compliance.",
            "16-digit ULPIN (Bhu-Aadhaar) digital parcel validation via UP Bhulekh portal."
        ]
        tenancy_rules = [
            "UP Zamindari Abolition and Land Reforms (UPZALR) Act 1950 & UP Revenue Code 2006 ceiling compliance (12.5 acres).",
            "Section 98/99 UP Revenue Code: Strict restrictions on alienation of SC/ST land without prior sanction of Collector.",
            "RERA Uttar Pradesh registration mandatory for residential/commercial plotted layout developments.",
            "Hindon/Yamuna riverbed zonation restrictions (no permanent construction within 100m high-flood level)."
        ]
        return {
            "applicable_authority": authority,
            "authority_short": authority_short,
            "special_legislation": special_act,
            "jantri_tier": jantri_tier,
            "na_prerequisites": na_prereqs,
            "tenancy_and_conversion_rules": tenancy_rules
        }

    if "maharashtra" in state or "pune" in district or "pune" in name_full:
        authority = "Pune Metropolitan Region Development Authority (PMRDA) / PMC"
        authority_short = "PMRDA / PMC"
        special_act = "Maharashtra Regional and Town Planning (MRTP) Act 1966 & Maharashtra Land Revenue Code (MLRC) 1966"
        jantri_tier = "Ready Reckoner Tier 1: Pune Metropolitan Corridor (Annual Statement of Rates 2026)"
        na_prereqs = [
            "Section 44 Maharashtra Land Revenue Code (MLRC) 1966 non-agricultural permission via e-Hakk portal.",
            "PMRDA Development Plan 2041 zoning verification and layout sanction.",
            "Maharashtra Pollution Control Board (MPCB) consent to establish for commercial/industrial setups.",
            "Water Resources Department (WRD) NOC for projects adjacent to Mula-Mutha river basin.",
            "Verification of Title / Search Report for 30 years from Sub-Registrar Office."
        ]
        tenancy_rules = [
            "Section 63 Bombay Tenancy and Agricultural Lands Act 1948 (Strict bar on transfer of agricultural land to non-agriculturists).",
            "Section 36 & 36A MLRC: Absolute prohibition on non-tribal transfer of tribal lands without State Govt sanction.",
            "Section 85 MLRC partition compliance and Satbara (7/12 & 8A) digital record synchronization.",
            "Western Ghats Eco-Sensitive Area (ESA) foothills construction buffer compliance."
        ]
        return {
            "applicable_authority": authority,
            "authority_short": authority_short,
            "special_legislation": special_act,
            "jantri_tier": jantri_tier,
            "na_prerequisites": na_prereqs,
            "tenancy_and_conversion_rules": tenancy_rules
        }

    # 1. Dynamically Detect Governing Planning Authority
    authority = "Gram Panchayat / Revenue Department (District Collectorate)"
    authority_short = "Gram Panchayat"
    special_act = "Gujarat Panchayats Act, 1993 & Gujarat Land Revenue Code (GLRC), 1879"
    jantri_tier = "Tier 4: Rural Agricultural Base (Standard agricultural Jantri tariff)"

    if "dholera" in name_full or "dholera" in taluka:
        authority = "Dholera Special Investment Region Development Authority (DSIRDA) & DICDL"
        authority_short = "DSIRDA"
        special_act = "Gujarat Special Investment Region (GSIR) Act, 2009 & TP Schemes 1-6"
        jantri_tier = "Tier 2: Special Investment Region (Industrial / Logistics Jantri with SIR infrastructure cess)"
    elif "kevadia" in name_full or "statue of unity" in name_full or "garudeshwar" in taluka:
        authority = "Statue of Unity Area Development and Tourism Governance Authority (SOUADTGA)"
        authority_short = "SOUADTGA"
        special_act = "Statue of Unity Area Development and Tourism Governance Act, 2019"
        jantri_tier = "Tier 2: High-Density Tourism Zone (Special commercial master plan valuation)"
    elif "ahmedabad" in district and any(t in taluka for t in ["ahmedabad", "daskroi", "sanand", "ghatlodiya", "sabarmati", "vatva"]):
        authority = "Ahmedabad Urban Development Authority (AUDA) / Amdavad Municipal Corporation (AMC)"
        authority_short = "AUDA / AMC"
        special_act = "Gujarat Town Planning and Urban Development Act (GTPUDA), 1976"
        jantri_tier = "Tier 1: Metro Core Corridor (Premium urban Jantri valuation with 40% TP scheme land pooling)"
    elif "gandhinagar" in district and any(t in taluka for t in ["gandhinagar", "kalol"]):
        authority = "Gandhinagar Urban Development Authority (GUDA) / GIFT City SEZ Authority"
        authority_short = "GUDA / GMC"
        special_act = "Gujarat Town Planning and Urban Development Act (GTPUDA), 1976"
        jantri_tier = "Tier 1: Capital / Financial Hub (GIFT City special planning and high-density FSI Jantri)"
    elif "surat" in district and any(t in taluka for t in ["surat", "choryasi", "olpad", "kamrej"]):
        authority = "Surat Urban Development Authority (SUDA) / Surat Municipal Corporation (SMC)"
        authority_short = "SUDA / SMC"
        special_act = "Gujarat Town Planning and Urban Development Act (GTPUDA), 1976"
        jantri_tier = "Tier 1: Metro Growth Corridor (High commercial/industrial Jantri tier along Hazira & Outer Ring Road)"
    elif "vadodara" in district and any(t in taluka for t in ["vadodara", "padra", "waghodia"]):
        authority = "Vadodara Urban Development Authority (VUDA) / Vadodara Municipal Corporation (VMC)"
        authority_short = "VUDA / VMC"
        special_act = "GTPUDA, 1976 & VUDA General Development Control Regulations"
        jantri_tier = "Tier 1: Urban / Industrial Corridor (Petrochemical & industrial zone Jantri rates)"
    elif "rajkot" in district and any(t in taluka for t in ["rajkot", "lodhika"]):
        authority = "Rajkot Urban Development Authority (RUDA) / Rajkot Municipal Corporation (RMC)"
        authority_short = "RUDA / RMC"
        special_act = "GTPUDA, 1976 & RUDA Comprehensive Development Plan"
        jantri_tier = "Tier 1: Saurashtra Commercial Core (Engineering cluster & urban Jantri rates)"
    elif "gidc" in name_full:
        authority = "Gujarat Industrial Development Corporation (GIDC)"
        authority_short = "GIDC"
        special_act = "Gujarat Industrial Development Act, 1962"
        jantri_tier = "Tier 2: Industrial Estate (Pre-fixed GIDC industrial plot allotment rate)"
    elif ecology.get("is_protected") or "forest" in name_full or "sanctuary" in name_full or "national park" in name_full:
        authority = "Gujarat State Forest Department (Principal Chief Conservator of Forests - Wildlife)"
        authority_short = "Forest Department"
        special_act = "Indian Forest Act, 1927 & Wildlife (Protection) Act, 1972"
        jantri_tier = "Tier 4: Non-alienable Protected / Reserved Forest Zone (Conversion prohibited)"
    else:
        # Check if taluka is an urban municipality
        if any(w in village for w in ["nagarpalika", "municipality", "city"]):
            authority = f"{hierarchy.get('taluka')} Municipality / Urban Local Body"
            authority_short = "Municipality"
            special_act = "Gujarat Municipalities Act, 1963 & GLRC 1879"
            jantri_tier = "Tier 3: Semi-Urban / Nagarpalika (Standard commercial/residential municipal rates)"

    # 2. Tenancy Framework (Saurashtra Gharkhed Act vs Bombay Tenancy Act)
    is_saurashtra = any(sd in district for sd in SAURASHTRA_DISTRICTS)
    tenancy_rules = []
    if is_saurashtra:
        tenancy_rules.append(
            "Saurashtra Gharkhed, Tenancy Settlement and Agricultural Lands Act, 1949 (Section 54): "
            "Strict bar on transfer of agricultural land to non-agriculturists without prior permission of the competent Revenue Collector."
        )
    else:
        tenancy_rules.append(
            "Gujarat Tenancy and Agricultural Lands Act, 1948 (Section 63): "
            "Bars transfer of agricultural land to non-agriculturists without prior sanction of the Collector."
        )

    # 3. Section 73AA / 73AB - PESA & Fifth Schedule Tribal land protections
    is_tribal = any(td in district for td in SCHEDULED_TRIBAL_DISTRICTS) or any(td in taluka for td in SCHEDULED_TRIBAL_DISTRICTS)
    if is_tribal:
        tenancy_rules.append(
            "Section 73AA of Gujarat Land Revenue Code (1879 / Amended) & PESA Act 1996: "
            "STRICT INALIENABILITY on transfer of tribal land to non-tribals without prior sanction of State Government/Collector; unauthorized occupancy is a non-bailable statutory offense."
        )

    # 4. Non-Agricultural (NA) Conversion Prerequisites
    na_prerequisites = [
        "Online submission via Gujarat Revenue iORA / e-NA single-window portal.",
        "Computerized Village Form 7/12 & 8-A certified extracts with Barcode verification.",
        "30-year non-encumbrance Title Search Certificate by an enrolled revenue advocate.",
        f"Development Permission (Rajachithi) / NOC from {authority_short} under GTPUDA / Panchayats Act.",
        f"Zonal master plan alignment and Jantri premium assessment under {jantri_tier.split(':')[0]}."
    ]

    if is_saurashtra:
        na_prerequisites.append("Section 54 sanction under Saurashtra Gharkhed Act for non-agriculturist applicant.")
    else:
        na_prerequisites.append("Section 63 Tenancy clearance under Gujarat Tenancy and Agricultural Lands Act.")

    if is_tribal:
        na_prerequisites.append("Section 73AA tribal inalienability clearance & District Collector special sanction.")

    if ecology.get("is_protected") or "forest" in name_full:
        na_prerequisites.append("National Board for Wildlife (NBWL) & State Forest Department 10km ESZ clearance.")

    return {
        "applicable_authority": authority,
        "authority_short": authority_short,
        "special_legislation": special_act,
        "jantri_tier": jantri_tier,
        "tenancy_and_conversion_rules": tenancy_rules,
        "na_prerequisites": na_prerequisites,
        "tribal_land_protection_active": is_tribal,
        "tenancy_jurisdiction": "Saurashtra Gharkhed Act (1949)" if is_saurashtra else "Gujarat Tenancy Act (1948)"
    }

