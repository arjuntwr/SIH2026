/**
 * Mock Data Fixtures for Standalone Frontend Execution
 * Aligned 1:1 with Backend Database Models and Government Seeds
 */

export const MOCK_RESOURCES = [
  {
    id: "res-gov-001",
    title: "SVAMITVA Scheme Guidelines: Drone-Based Cadastral Survey & Property Cards in Abadi (Inhabited) Rural Areas",
    title_hi: "स्वामित्व योजना मार्गदर्शिका: ग्रामीण आबादी क्षेत्रों में ड्रोन आधारित भू-कर सर्वेक्षण एवं संपत्ति कार्ड",
    taxonomy_stream: "policy-legislation",
    document_type: "Manual / Framework",
    theme: "Digital Cadastre & Resurvey",
    coverage_scope: "National",
    state_ut: "National",
    district: null,
    lgd_code: "0",
    ulpin: "NA-POLICY-2024-SVAMITVA",
    legal_authority: "Ministry of Panchayati Raj & Department of Land Resources (DoLR)",
    gazette_number: "MoPR/SVAMITVA/2024/CIR-08",
    case_number: null,
    publication_date: "2024-03-15",
    effective_date: "2024-04-01",
    abstract: "Standard operating procedure and technical guidelines for continuous operating reference stations (CORS) network establishment, drone-based aerial orthorectified image acquisition at 5cm GSD, ground control point (GCP) validation, and generation of digitally verifiable 'Gharaunda' / Bhu-Aadhaar property cards under the SVAMITVA national flagship mission.",
    abstract_hi: "स्वामित्व राष्ट्रीय फ्लैगशिप मिशन के तहत कॉर्स नेटवर्क स्थापना, 5 सेमी जीएसडी पर ड्रोन आधारित ऑर्थोरेक्टीफाइड इमेजरी, जीसीपी सत्यापन और डिजिटल रूप से सत्यापित संपत्ति कार्ड निर्माण हेतु तकनीकी दिशानिर्देश।",
    ai_executive_summary: {
      key_takeaways: [
        "Mandates 5cm spatial resolution orthorectified mosaics for all inhabited (Abadi) rural clusters.",
        "Integrates CORS base stations directly with Survey of India reference frames.",
        "Enables rural property holders to leverage property cards as collateral for institutional financial credit.",
        "Eliminates boundary dispute ambiguity between Gram Panchayat public common lands and private village homesteads."
      ],
      policy_implications: [
        "Replaces century-old analog British-era Chahi/Abadi surveys with sub-decimeter geodetic accuracy.",
        "Paves path for property taxation devolution directly to Gram Panchayats.",
        "Accelerates interoperability with Bhu-Aadhaar (14-digit ULPIN) schema."
      ],
      affected_stakeholders: [
        "Gram Panchayats",
        "Rural Homeowners",
        "Survey of India",
        "Commercial & Rural Credit Banks",
        "District Revenue Collectors"
      ],
      legal_doctrines_invoked: [
        "Doctrine of Presumptive Title vs. Conclusive Title",
        "Panchayati Raj Constitutional Framework (Article 243G)"
      ],
      spatial_relevance: "CORS geodetic baseline network and 5cm Drone Orthophoto Mosaics."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "स्वामित्व योजना मार्गदर्शिका: ग्रामीण आबादी क्षेत्रों में ड्रोन सर्वेक्षण",
        abstract: "स्वामित्व मिशन के तहत कॉर्स नेटवर्क, 5 सेमी ड्रोन इमेजरी और डिजिटल संपत्ति कार्ड का तकनीकी ढांचा।"
      },
      mr: {
        title: "स्वामित्व योजना मार्गदर्शक तत्त्वे: ड्रोन सर्वेक्षण व मिळकत पत्रिका",
        abstract: "ग्रामीण गावठाण क्षेत्रातील मालमत्तांचे ड्रोन आधारित नकाशे आणि डिजिटल सनद वाटपाची नियमावली."
      },
      te: {
        title: "స్వామిత్వ పథక మార్గదర్శకాలు: డ్రోన్ సర్వే మరియు ప్రాపర్టీ కార్డులు",
        abstract: "గ్రామీణ ప్రాంతాలలో డ్రోన్ ఆధారిత సర్వే మరియు భూ-ఆధార్ ప్రాపర్టీ కార్డుల జారీ మార్గదర్శకాలు."
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 99.85,
    page_count: 86,
    file_format: "PDF",
    file_size_bytes: 14285700,
    file_url: "/documents/svamitva_operational_guidelines_2024.pdf",
    sha256_checksum: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    has_spatial_layer: true,
    spatial_geojson: {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          properties: {
            name: "Abadi Boundary Parcel Cluster #104",
            ulpin: "27140982341209",
            area_sq_m: 450.2,
            land_use: "Residential Homestead",
            survey_no: "104/1A"
          },
          geometry: {
            type: "Polygon",
            coordinates: [[[78.172, 26.218], [78.175, 26.218], [78.176, 26.215], [78.171, 26.214], [78.172, 26.218]]]
          }
        }
      ]
    },
    source_system: "DoLR Gazette / MoPR",
    source_id: "MOPR-SVAMITVA-2024-DOC",
    citations: {
      apa: "Ministry of Panchayati Raj. (2024). Operational Guidelines for SVAMITVA. Government of India.",
      mla: "Ministry of Panchayati Raj. Operational Guidelines for SVAMITVA. Government of India, 2024.",
      indian_legal: "DoLR / MoPR Notification, SVAMITVA Guidelines 2024, Ref No. MoPR/CIR/08/2024",
      bibtex: "@techreport{svamitva2024,\n  title={SVAMITVA Guidelines},\n  year={2024}\n}"
    },
    last_synced_at: new Date().toISOString()
  },
  {
    id: "res-jud-002",
    title: "Indore Development Authority v. Manoharlal & Ors.: Constitution Bench Judgment on Section 24(2) of RFCTLARR Act 2013",
    title_hi: "इंदौर विकास प्राधिकरण बनाम मनोहर लाल: भूमि अधिग्रहण कानून की धारा 24(2) पर संविधान पीठ का ऐतिहासिक फैसला",
    taxonomy_stream: "judicial-records",
    document_type: "Judgement",
    theme: "Land Acquisition (RFCTLARR)",
    coverage_scope: "National",
    state_ut: "Madhya Pradesh",
    district: "Indore",
    lgd_code: "393",
    ulpin: "MP-IND-JUD-2020-001",
    legal_authority: "Supreme Court of India (Constitution Bench)",
    gazette_number: null,
    case_number: "Civil Appeal No. 20982 of 2020",
    publication_date: "2020-03-06",
    effective_date: "2020-03-06",
    abstract: "Unanimous landmark ruling by a 5-Judge Constitution Bench clarifying lapse of land acquisition proceedings under Section 24(2) of the Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013. Holds that acquisition does not lapse if compensation was tendered in treasury or if possession could not be taken due to interim court injunctions.",
    abstract_hi: "भूमि अधिग्रहण अधिनियम 2013 की धारा 24(2) के तहत अधिग्रहण रद्द होने संबंधी 5-न्यायाधीशों की संविधान पीठ का ऐतिहासिक फैसला। यदि मुआवजा कोषागार में जमा किया गया था या अदालती स्थगन के कारण कब्जा नहीं लिया जा सका, तो अधिग्रहण निष्फल नहीं माना जाएगा।",
    ai_executive_summary: {
      key_takeaways: [
        "Twin conditions under Section 24(2) (failure to take physical possession AND failure to deposit compensation) must BOTH be satisfied for acquisition to lapse.",
        "Payment of compensation does not mandate individual bank deposits if landowners refused tender; deposit in Government Treasury satisfies 'paid'.",
        "Litigants who obtained interim stay orders cannot invoke delay in possession to claim lapse of public infrastructure acquisition.",
        "Resolved conflicting 3-Judge bench precedents (Pune Municipal Corp v. Harakchand Misirimal Solanki vs Indore Development Authority 2018)."
      ],
      policy_implications: [
        "Revived thousands of stalled public urban infrastructure projects across India worth over ₹2.8 Lakh Crore.",
        "Stabilized municipal land banks and highway corridor projects against retroactive lapse claims.",
        "Reaffirmed strict evidentiary burden on landowners claiming non-possession via Panchnama records."
      ],
      affected_stakeholders: [
        "Infrastructure Authorities (NHAI, State Development Authorities)",
        "Original Landowners & Tenancy Litigants",
        "State Revenue & Land Acquisition Collectors"
      ],
      legal_doctrines_invoked: [
        "Actus Curiae Neminem Gravabit (An act of court shall prejudice no man)",
        "Purposive Construction of Expropriatory Statutes"
      ],
      spatial_relevance: "Direct impact on right-of-way corridor acquisition parcels across 18 State Development Authorities."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "इंदौर विकास प्राधिकरण बनाम मनोहर लाल: धारा 24(2) पर फैसला",
        abstract: "सुप्रीम कोर्ट की संविधान पीठ ने भूमि अधिग्रहण कानून 2013 की धारा 24(2) की व्याख्या स्पष्ट की।"
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 99.95,
    page_count: 319,
    file_format: "PDF",
    file_size_bytes: 18450200,
    file_url: "/documents/sc_indore_dev_authority_manoharlal_2020.pdf",
    sha256_checksum: "8a3e7987cb3d4f451f22143714274c43aeef2858b90f4886fa7f88e99e2f9d12",
    has_spatial_layer: false,
    spatial_geojson: null,
    source_system: "e-Courts NJDG / Supreme Court Registry",
    source_id: "SCI-CR-2020-MANOHARLAL",
    citations: {
      apa: "Indore Development Authority v. Manoharlal, (2020) 8 SCC 129 (Supreme Court of India).",
      mla: "Indore Development Authority v. Manoharlal. 8 SCC 129. Supreme Court of India, 2020.",
      indian_legal: "(2020) 8 SCC 129",
      bibtex: "@article{indore_dev_manoharlal_2020,\n  title={Indore Development Authority v. Manoharlal},\n  journal={SCC},\n  year={2020}\n}"
    },
    last_synced_at: new Date().toISOString()
  },
  {
    id: "res-geo-003",
    title: "National Geo-Referenced Cadastral Boundaries & Village-Level RoR Spatial Baseline - District Varanasi (LGD: 187)",
    title_hi: "राष्ट्रीय भू-संदर्भित कैडस्ट्रल सीमाएं एवं ग्राम-स्तरीय अभिलेख spatial बेसलाइन - जनपद वाराणसी",
    taxonomy_stream: "government-datasets",
    document_type: "Dataset",
    theme: "Digital Cadastre & Resurvey",
    coverage_scope: "District",
    state_ut: "Uttar Pradesh",
    district: "Varanasi",
    lgd_code: "187",
    ulpin: "09187000000001",
    legal_authority: "Board of Revenue Uttar Pradesh & DoLR Bhu-Aadhaar National Cell",
    gazette_number: "UP-REV-CAD-2024-VAR-09",
    case_number: null,
    publication_date: "2024-08-20",
    effective_date: "2024-08-20",
    abstract: "High-precision vector cadastral layer covering 1,324 revenue villages in Varanasi District, completely aligned with the national 14-digit Unique Land Parcel Identification Number (ULPIN / Bhu-Aadhaar). Features topological polygons with attribute linkage to Khatauni (Record of Rights), land-use categorization, and dispute flags.",
    abstract_hi: "वाराणसी जनपद के 1,324 राजस्व ग्रामों का उच्च-सटीकता वेक्टर कैडस्ट्रल डेटासेट, जो 14-अंकीय भू-आधार (यूएलपीआईएन) के साथ पूर्णतः एकीकृत है। इसमें खतौनी, भूमि उपयोग वर्गीकरण और न्यायिक विवाद फ़्लैग्स शामिल हैं।",
    ai_executive_summary: {
      key_takeaways: [
        "100% boundary vectorization completed across 1.84 Lakh agricultural and homestead land parcels.",
        "Each parcel assigned deterministic WGS-84 centroid-derived 14-digit alphanumeric Bhu-Aadhaar.",
        "Zero spatial overlap tolerance achieved through automated topology cleaning algorithms.",
        "Includes real-time webhook connector to e-Courts District Revenue Court Computerized System (RCCMS)."
      ],
      policy_implications: [
        "Enables instantaneous automated title verification for PM-KISAN, crop insurance (PMFBY), and land registry.",
        "Reduces demarcation disputes at Tehsil level by 68% within 9 months of rollout.",
        "Forms core geospatial spine for Varanasi Smart City spatial planning."
      ],
      affected_stakeholders: [
        "Farmers & Land Title Holders",
        "Lekhpals / Patwaris",
        "Registration & Sub-Registrar Offices",
        "Lead Bank District Credit Managers"
      ],
      legal_doctrines_invoked: [
        "UP Revenue Code 2006 (Section 31 - Maintenance of Maps and Field-books)"
      ],
      spatial_relevance: "Direct GIS Cadastral Layer with EPSG:4326 GeoJSON polygons."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "राष्ट्रीय भू-संदर्भित कैडस्ट्रल सीमाएं - जनपद वाराणसी",
        abstract: "वाराणसी के 1,324 राजस्व ग्रामों का 14-अंकीय भू-आधार आधारित एकीकृत भू-स्थानिक मानचित्र।"
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 100.0,
    page_count: 1,
    file_format: "GeoJSON",
    file_size_bytes: 48291000,
    file_url: "/datasets/varanasi_cadastral_boundaries_lgd187.geojson",
    sha256_checksum: "b47a9f82d1c25838d7f8d7b3e0291e6b375b4819d2685718fa671239c049d5aa",
    has_spatial_layer: true,
    spatial_geojson: {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          properties: {
            ulpin: "09187042019481",
            survey_no: "241/2",
            khata_no: "00412",
            area_hectares: 0.842,
            owner_type: "Joint Agricultural Tenure",
            irrigation_status: "Tube-well Irrigated",
            dispute_flag: false,
            village_name: "Rameshwar",
            tehsil: "Raja Talab"
          },
          geometry: {
            type: "Polygon",
            coordinates: [
              [[82.8821, 25.3214], [82.8845, 25.3228], [82.8858, 25.3201], [82.8832, 25.3192], [82.8821, 25.3214]]
            ]
          }
        },
        {
          type: "Feature",
          properties: {
            ulpin: "09187042019482",
            survey_no: "241/3",
            khata_no: "00413",
            area_hectares: 1.120,
            owner_type: "Individual Freehold",
            irrigation_status: "Canal Irrigated",
            dispute_flag: true,
            village_name: "Rameshwar",
            tehsil: "Raja Talab"
          },
          geometry: {
            type: "Polygon",
            coordinates: [
              [[82.8845, 25.3228], [82.8872, 25.3241], [82.8885, 25.3218], [82.8858, 25.3201], [82.8845, 25.3228]]
            ]
          }
        },
        {
          type: "Feature",
          properties: {
            ulpin: "09187042019483",
            survey_no: "242/1",
            khata_no: "00098",
            area_hectares: 0.510,
            owner_type: "Gram Sabha Common Land",
            irrigation_status: "Pond Catchment",
            dispute_flag: false,
            village_name: "Rameshwar",
            tehsil: "Raja Talab"
          },
          geometry: {
            type: "Polygon",
            coordinates: [
              [[82.8821, 25.3214], [82.8832, 25.3192], [82.8805, 25.3181], [82.8794, 25.3202], [82.8821, 25.3214]]
            ]
          }
        }
      ]
    },
    source_system: "Open Government Data (data.gov.in) / DoLR",
    source_id: "DLRMP-OGD-UP-VAR-187",
    citations: {
      apa: "Department of Land Resources. (2024). Varanasi District Geo-Referenced Cadastral Baseline [Data set]. Government of India.",
      mla: "Department of Land Resources. 'Varanasi District Geo-Referenced Cadastral Baseline.' 2024.",
      indian_legal: "DoLR Cadastral Baseline Dataset, Varanasi (LGD: 187), Catalog NID: DLRMP-OGD-UP-VAR-187",
      bibtex: "@misc{varanasi2024cadastre,\n  title={Varanasi Cadastre},\n  year={2024}\n}"
    },
    last_synced_at: new Date().toISOString()
  },
  {
    id: "res-pol-004",
    title: "Model Tenancy Act & State Agricultural Land Leasing Regulatory Framework: 2021-2025 Comparative Adoption Compendium",
    title_hi: "मॉडल किराएदारी अधिनियम एवं राज्य कृषि भूमि पट्टा नियामक ढांचा: तुलनात्मक विश्लेषण",
    taxonomy_stream: "policy-legislation",
    document_type: "Policy Brief",
    theme: "Tenancy & Leasing Reforms",
    coverage_scope: "National",
    state_ut: "National",
    district: null,
    lgd_code: "0",
    ulpin: "NA-POLICY-MTA-COMPENDIUM",
    legal_authority: "NITI Aayog & Department of Land Resources (DoLR)",
    gazette_number: "NITI-MTA-2023-REV04",
    case_number: null,
    publication_date: "2023-11-10",
    effective_date: "2023-12-01",
    abstract: "Comprehensive legal and economic assessment of the Model Tenancy Act (MTA) and the NITI Aayog Model Agricultural Land Leasing Act across 28 States and 8 Union Territories. Analyzes institutional transition from informal oral tenancy (Batai/Bargadar systems) to legally protected formal lease registries.",
    abstract_hi: "28 राज्यों और 8 केंद्र शासित प्रदेशों में मॉडल किराएदारी अधिनियम और कृषि भूमि पट्टा कानून का कानूनी व आर्थिक मूल्यांकन। मौखिक अनौपचारिक बटाईदारी से औपचारिक पट्टा पंजीकरण तक का विश्लेषण।",
    ai_executive_summary: {
      key_takeaways: [
        "States adopting formal leasing laws witnessed 41% surge in institutional credit disbursement to tenant cultivators.",
        "Landowners' fear of adverse possession or permanent tenancy vesting reduced drastically with statutory rent authority courts.",
        "Identifies legislative gaps in 9 states where tenancy remains legally prohibited or heavily restricted under 1960s Land Ceiling Acts."
      ],
      policy_implications: [
        "Unlocks uncultivated fallow agricultural land estimated at 24 Million Hectares nationwide.",
        "Protects tenant farmers' eligibility for government compensation during natural crop loss disasters."
      ],
      affected_stakeholders: [
        "Tenant Cultivators & Sharecroppers",
        "Absentee Landowners",
        "State Legislative Assemblies"
      ],
      legal_doctrines_invoked: [
        "Right to Livelihood (Article 21)",
        "State List Entry 18 (Land Rights under Seventh Schedule)"
      ],
      spatial_relevance: "State-level legislative adoption index map across all 36 States/UTs."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "मॉडल किराएदारी अधिनियम एवं राज्य कृषि भूमि पट्टा ढांचा",
        abstract: "28 राज्यों में किराएदारी सुधारों और किसान पट्टा अधिकारों का नीतिगत विश्लेषण।"
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 99.70,
    page_count: 142,
    file_format: "PDF",
    file_size_bytes: 8920400,
    file_url: "/documents/model_tenancy_act_state_adoption_compendium.pdf",
    sha256_checksum: "5f1d7e26b1c43d99e847d81a9f029e46a78b54318c679234ea7629560f89c411",
    has_spatial_layer: false,
    spatial_geojson: null,
    source_system: "DoLR Policy Bulletin / NITI Aayog",
    source_id: "NITI-AAYOG-MTA-2023",
    citations: {
      apa: "NITI Aayog, & DoLR. (2023). Compendium on State Agricultural Land Leasing. Government of India.",
      mla: "NITI Aayog, and DoLR. Compendium on State Agricultural Land Leasing. 2023.",
      indian_legal: "NITI Aayog Policy Report, DoLR Tenancy Compendium 2023, Doc ID: NITI-MTA-2023",
      bibtex: "@techreport{mta2023,\n  title={Compendium on State Land Leasing},\n  year={2023}\n}"
    },
    last_synced_at: new Date().toISOString()
  },
  {
    id: "res-case-005",
    title: "High-Precision Drone Cadastral Resurvey and Modern Record Room Automation: Odisha 5T Land Governance Pilot (Ganjam District)",
    title_hi: "ओडिशा 5T भूमि सुशासन पायलट: गंजम जिले में हाई-प्रिसिजन ड्रोन री-सर्वे एवं आधुनिक रिकॉर्ड रूम स्वचालन",
    taxonomy_stream: "pilot-case-studies",
    document_type: "Best Practice Report",
    theme: "Best Practices & Pilot Case Studies",
    coverage_scope: "District",
    state_ut: "Odisha",
    district: "Ganjam",
    lgd_code: "354",
    ulpin: "21354000109284",
    legal_authority: "Revenue & Disaster Management Department, Government of Odisha",
    gazette_number: "OD-REV-5T-PILOT-2023",
    case_number: null,
    publication_date: "2023-09-18",
    effective_date: "2023-10-01",
    abstract: "Field validation pilot evaluation on end-to-end digital land record modernization in Ganjam District under Odisha's 5T governance mandate. Examines integration of RTK-enabled UAV cadastral flights, automated boundary stitching, public claim/objection grievance resolution via village camps, and issuance of tamper-proof QR-coded Land Passbooks.",
    abstract_hi: "ओडिशा के 5T सुशासन अधिदेश के तहत गंजम जिले में पूर्ण डिजिटल भूमि रिकॉर्ड आधुनिकीकरण का मूल्यांकन। ड्रोन री-सर्वे, स्वचालित सीमा सिलाई, सार्वजनिक आपत्ति निवारण शिविर एवं क्यूआर-कोडेड पट्टा वितरण का अध्ययन।",
    ai_executive_summary: {
      key_takeaways: [
        "Reduced resurvey cycle time from traditional 30 years to just 45 days per revenue village.",
        "Achieved 99.2% citizen satisfaction score during public validation camps (Jan Sunwai).",
        "Modern Record Rooms (MRRs) established at all 23 Tehsils with digital RFID-tagged physical archive retrieval under 3 minutes.",
        "Dispute reduction of 84% in boundary dispute litigations before Sub-Divisional Magistrates."
      ],
      policy_implications: [
        "Recommended by DoLR as national blueprint for States transitioning from Settlement Operations to Continuous Dynamic Cadastres.",
        "Demonstrated cost savings of ₹140 Crore compared to legacy total station terrestrial survey methodologies."
      ],
      affected_stakeholders: [
        "Small & Marginal Landholders",
        "Tehsildars & Revenue Inspectors",
        "Odisha Space Applications Centre (ORSAC)"
      ],
      legal_doctrines_invoked: [
        "Odisha Survey and Settlement Act, 1958",
        "Odisha Right to Public Services Act (ORTPSA)"
      ],
      spatial_relevance: "Complete village boundary vector shapefiles with CORS station base coordinates."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "ओडिशा 5T भूमि सुशासन पायलट - गंजम जिला केस स्टडी",
        abstract: "गंजम में ड्रोन आधारित कैडस्ट्रल री-सर्वे और आधुनिक रिकॉर्ड रूम का सर्वोत्तम अभ्यास विश्लेषण।"
      },
      or: {
        title: "ଓଡ଼ିଶା ୫ଟି ଭୂମି ପ୍ରଶାସନ ପାଇଲଟ୍: ଗଞ୍ଜାମ ଜିଲ୍ଲାରେ ଡ୍ରୋନ୍ ସର୍ବେକ୍ଷଣ",
        abstract: "ଗଞ୍ଜାମ ଜିଲ୍ଲାରେ ଡ୍ରୋନ୍ ଆଧାରିତ କ୍ୟାଡାଷ୍ଟ୍ରାଲ୍ ପୁନଃସର୍ବେକ୍ଷଣ ସଫଳତାର କେସ୍ ଷ୍ଟଡି।"
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 99.90,
    page_count: 64,
    file_format: "PDF",
    file_size_bytes: 11540800,
    file_url: "/documents/odisha_5t_ganjam_cadastral_pilot_report.pdf",
    sha256_checksum: "3c84e1b827e8a9394f92d4f828a2b5e28a49c6d3782b527582b1928374a2b910",
    has_spatial_layer: true,
    spatial_geojson: {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          properties: {
            pilot_zone: "Chhatrapur Tehsil Pilot Cluster",
            survey_stations: 4,
            villages_covered: 12,
            parcels_mapped: 14280,
            accuracy_cm: 3.8
          },
          geometry: {
            type: "Polygon",
            coordinates: [
              [[84.982, 19.345], [85.021, 19.362], [85.045, 19.321], [84.995, 19.308], [84.982, 19.345]]
            ]
          }
        }
      ]
    },
    source_system: "State Revenue Department / DoLR Best Practices Portal",
    source_id: "ODISHA-REV-5T-GANJAM-2023",
    citations: {
      apa: "Revenue & Disaster Management Department. (2023). Odisha 5T Land Governance Pilot: Ganjam District. Government of Odisha.",
      mla: "Revenue & Disaster Management Department. Odisha 5T Land Governance Pilot. 2023.",
      indian_legal: "Odisha State Best Practice Report, Ganjam Pilot 2023, Doc: OD-REV-5T-PILOT-2023",
      bibtex: "@report{odisha2023pilot,\n  title={Odisha 5T Pilot},\n  year={2023}\n}"
    },
    last_synced_at: new Date().toISOString()
  },
  {
    id: "res-acad-006",
    title: "Tenure Security, Land Consolidation, and Agricultural Productivity under ULPIN (Bhu-Aadhaar): An Econometric Evaluation",
    title_hi: "भू-आधार (ULPIN) के तहत भू-स्वामित्व सुरक्षा, चकबंदी एवं कृषि उत्पादकता: एक अर्थमितीय मूल्यांकन",
    taxonomy_stream: "academic-research",
    document_type: "Academic Paper",
    theme: "Urban-Rural Land Transition",
    coverage_scope: "National",
    state_ut: "National",
    district: null,
    lgd_code: "0",
    ulpin: "NA-ACAD-IIMA-2024-ULPIN",
    legal_authority: "Centre for Land Governance, Indian Institute of Management (IIM) Ahmedabad",
    gazette_number: null,
    case_number: null,
    publication_date: "2024-05-12",
    effective_date: "2024-05-12",
    abstract: "Empirical study utilizing difference-in-differences (DiD) and instrumental variable estimation across 4,200 farming households in Maharashtra, Karnataka, and Rajasthan. Quantifies the impact of 14-digit Bhu-Aadhaar seeding on parcel fragmentation, capital investment in micro-irrigation, dispute incidence, and credit accessibility.",
    abstract_hi: "महाराष्ट्र, कर्नाटक और राजस्थान के 4,200 कृषक परिवारों पर आधारित अनुभवजन्य अध्ययन। 14-अंकीय भू-आधार सीडिंग का भूमि विखंडन, सूक्ष्म-सिंचाई में पूंजी निवेश और संस्थागत ऋण पर प्रभाव का अर्थमितीय विश्लेषण।",
    ai_executive_summary: {
      key_takeaways: [
        "Bhu-Aadhaar seeded plots experienced a 27.4% increase in farm-level fixed capital investments (solar pumps, drip irrigation).",
        "Average informal credit interest rates dropped from 24% p.a. to 8.5% p.a. as Kisan Credit Cards (KCC) were sanctioned within 48 hours.",
        "Voluntary parcel consolidation exchanges among contiguous kin rose by 38% due to crystal-clear boundary certainty."
      ],
      policy_implications: [
        "Provides rigorous empirical justification for allocating higher budgetary support for ULPIN roll-out under DILRMP Phase-II.",
        "Urges integration of soil health card and groundwater extraction permits directly into the Bhu-Aadhaar parcel metadata schema."
      ],
      affected_stakeholders: [
        "Agricultural Economists",
        "Ministry of Agriculture & Farmers Welfare",
        "Reserve Bank of India"
      ],
      legal_doctrines_invoked: [
        "Coase Theorem of Property Rights and Transaction Costs",
        "Torrens Title Guarantee Framework"
      ],
      spatial_relevance: "Multi-state sample cluster map with LandVoc ontology keyword indexing."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "भू-आधार (ULPIN) के तहत भू-स्वामित्व सुरक्षा एवं कृषि उत्पादकता",
        abstract: "4,200 किसानों पर आईआईएम अहमदाबाद का अर्थमितीय अध्ययन, जिसने सिद्ध किया कि भू-आधार से कृषि निवेश 27% बढ़ा।"
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 99.80,
    page_count: 48,
    file_format: "PDF",
    file_size_bytes: 5420900,
    file_url: "/documents/iima_land_tenure_ulpin_evaluation_2024.pdf",
    sha256_checksum: "7c92b45a6829f01836e4b830291e7b235928a64917d92847103829471928c019",
    has_spatial_layer: false,
    spatial_geojson: null,
    source_system: "OpenAlex / Academic Land Registry",
    source_id: "IIMA-WP-2024-LAND-04",
    citations: {
      apa: "Sharma, P., Deshmukh, V., & Rao, K. (2024). Tenure Security, Land Consolidation, and Agricultural Productivity under ULPIN. Journal of Land Economics, 18(2), 145–182.",
      mla: "Sharma, P., et al. 'Tenure Security under ULPIN.' Journal of Land Economics, 2024.",
      indian_legal: "IIM-A Working Paper Series, WP No. 2024-05-01, Land Governance Centre",
      bibtex: "@article{iima2024,\n  title={Tenure Security under ULPIN},\n  year={2024}\n}"
    },
    last_synced_at: new Date().toISOString()
  },
  {
    id: "res-jud-007",
    title: "Adivasi Swaraj Morcha v. State Revenue Board: Protection of Scheduled Tribe Agricultural Lands under Section 36A and FRA 2006",
    title_hi: "आदिवासी स्वराज मोर्चा बनाम राज्य राजस्व बोर्ड: धारा 36A एवं वन अधिकार कानून 2006 के तहत जनजातीय भूमि संरक्षण",
    taxonomy_stream: "judicial-records",
    document_type: "Judgement",
    theme: "Forest & Tribal Land Rights",
    coverage_scope: "State",
    state_ut: "Maharashtra",
    district: "Palghar",
    lgd_code: "664",
    ulpin: "MH-PAL-2023-FRA-08",
    legal_authority: "High Court of Judicature at Bombay",
    gazette_number: null,
    case_number: "Writ Petition (PIL) No. 4412 of 2022",
    publication_date: "2023-08-14",
    effective_date: "2023-08-14",
    abstract: "Division Bench ruling declaring void ab initio any unauthorized transfer, non-agricultural (NA) conversion, or long-term lease of agricultural land belonging to Scheduled Tribe members without prior sanction of the District Collector. Confirms absolute primacy of Community Forest Rights (CFR) titles granted under Forest Rights Act 2006.",
    abstract_hi: "बॉम्बे हाई कोर्ट की खंडपीठ का महत्वपूर्ण निर्णय, जिसके अनुसार जिला कलेक्टर की पूर्व अनुमति के बिना अनुसूचित जनजाति की भूमि का कोई भी गैर-कृषि रूपांतरण या अनधिकृत पट्टा प्रारंभ से ही शून्य (void ab initio) होगा।",
    ai_executive_summary: {
      key_takeaways: [
        "Enforces strict statutory bar under Section 36A of Maharashtra Land Revenue Code against alienating tribal lands.",
        "Directs District Collector Palghar to restore possession of 840 acres of illegally occupied tribal lands within 90 days.",
        "Mandates automated GIS overlay checking in online building permission systems to flag Fifth Schedule scheduled area parcels."
      ],
      policy_implications: [
        "Sets rigorous benchmark for preventing peri-urban industrial encroachment into Scheduled Area lands.",
        "Requires State Land Registration Department to block deed execution for non-tribal buyers without Collector approval certificates."
      ],
      affected_stakeholders: [
        "Tribal Communities & FRA Title Holders",
        "Sub-Registrars of Deeds",
        "Tribal Development Department"
      ],
      legal_doctrines_invoked: [
        "Fifth Schedule of the Constitution of India",
        "Doctrine of Non-Alienation of Indigenous Lands"
      ],
      spatial_relevance: "Cadastral boundaries of Fifth Schedule revenue villages in Palghar & Thane."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "आदिवासी स्वराज मोर्चा बनाम राज्य राजस्व बोर्ड: जनजातीय भूमि संरक्षण",
        abstract: "बॉम्बे हाई कोर्ट का ऐतिहासिक फैसला: कलेक्टर की मंजूरी के बिना जनजातीय भूमि का हस्तांतरण अवैध।"
      },
      mr: {
        title: "आदिवासी स्वराज्य मोर्चा वि. राज्य महसूल मंडळ: आदिवासी जमीन संरक्षण निकाल",
        abstract: "आदिवासींच्या जमिनींचे बिगर-आदिवासींना बेकायदेशीर हस्तांतरण रद्दबातल ठरवणारा उच्च न्यायालयाचा निकाल."
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 99.88,
    page_count: 92,
    file_format: "PDF",
    file_size_bytes: 7180200,
    file_url: "/documents/bombay_hc_adivasi_swaraj_morcha_2023.pdf",
    sha256_checksum: "2b91c4871e9842a198c21849182b481928471928471982741982741982741829",
    has_spatial_layer: false,
    spatial_geojson: null,
    source_system: "e-Courts NJDG / High Court Registry",
    source_id: "BOM-HC-PIL-4412-2022",
    citations: {
      apa: "Adivasi Swaraj Morcha v. State of Maharashtra, 2023 SCC OnLine Bom 1840.",
      mla: "Adivasi Swaraj Morcha v. State of Maharashtra. 2023 SCC OnLine Bom 1840.",
      indian_legal: "2023 SCC OnLine Bom 1840",
      bibtex: "@article{bomhc2023,\n  title={Adivasi Swaraj Morcha v. State},\n  year={2023}\n}"
    },
    last_synced_at: new Date().toISOString()
  },
  {
    id: "res-geo-008",
    title: "Village-Level Record of Rights (RoR) Mutation Latency & Agricultural Census Baseline (Maharashtra Mahabhulekh Telemetry)",
    title_hi: "ग्राम-स्तरीय भू-अभिलेख (RoR) दाखिल-खारिज गति एवं कृषि संगणना बेसलाइन - महाभूलेख",
    taxonomy_stream: "government-datasets",
    document_type: "Dataset",
    theme: "Urban-Rural Land Transition",
    coverage_scope: "State",
    state_ut: "Maharashtra",
    district: "Pune",
    lgd_code: "492",
    ulpin: "27492000000001",
    legal_authority: "Settlement Commissioner and Director of Land Records, Maharashtra",
    gazette_number: "MH-REV-DATA-2024-PUN-04",
    case_number: null,
    publication_date: "2024-07-01",
    effective_date: "2024-07-01",
    abstract: "Aggregated transactional dataset tracking digital mutation notice issuances (Form 12), e-Hakk online application lifecycles, Lekhpal verification turnaround times, and crop survey land-use entries across 1,860 revenue villages in Pune District. Provides benchmark data on administrative latency in undisputed vs. disputed mutation cases.",
    abstract_hi: "पुणे जनपद के 1,860 राजस्व ग्रामों में डिजिटल दाखिल-खारिज (ई-हक्क) नोटिस, पटवारी सत्यापन अवधि एवं फसल सर्वेक्षण डेटासेट।",
    ai_executive_summary: {
      key_takeaways: [
        "Average undisputed online mutation turnaround time reduced to 16.4 days (down from 94 days in 2020).",
        "Automated 15-day public objection countdown triggered via SMS alerts to all registered co-sharers.",
        "E-Registration portal integration eliminates manual submission of sale deed copies to Talathi offices."
      ],
      policy_implications: [
        "Serves as national template for Business Reform Action Plan (BRAP) ease of doing business land indicators.",
        "Enables algorithmic detection of suspicious parallel mutations on mortgaged land parcels."
      ],
      affected_stakeholders: [
        "Agricultural Buyers and Sellers",
        "Talathis / Revenue Circle Officers",
        "FinTech Agriloan Underwriters"
      ],
      legal_doctrines_invoked: [
        "Maharashtra Land Revenue Code 1966 (Section 150 - Procedure for record of rights)"
      ],
      spatial_relevance: "Tehsil-wise mutation velocity maps and agricultural census tracts."
    },
    original_language: "English",
    translations: {
      hi: {
        title: "महाभूलेख ग्राम-स्तरीय नामांतरण डेटासेट - पुणे",
        abstract: "पुणे जनपद के 1,860 ग्रामों का डिजिटल म्यूटेशन एवं भूमि रिकॉर्ड डेटाबेस।"
      }
    },
    ocr_status: "VERIFIED_SEARCHABLE",
    ocr_confidence: 100.0,
    page_count: 1,
    file_format: "CSV",
    file_size_bytes: 28490100,
    file_url: "/datasets/mahabhulekh_pune_mutation_telemetry_2024.csv",
    sha256_checksum: "9a18471928471928471982741982741982741982741982741982741982741982",
    has_spatial_layer: true,
    spatial_geojson: {
      type: "FeatureCollection",
      features: [
        {
          type: "Feature",
          properties: {
            tehsil: "Haveli",
            active_mutations: 1420,
            avg_days_undisputed: 14.8,
            disputed_cases: 88,
            e_hakk_adoption_rate: "98.4%"
          },
          geometry: {
            type: "Polygon",
            coordinates: [
              [[73.842, 18.512], [73.895, 18.534], [73.912, 18.498], [73.864, 18.472], [73.842, 18.512]]
            ]
          }
        }
      ]
    },
    source_system: "Open Government Data (data.gov.in) / Mahabhulekh",
    source_id: "OGD-MAHA-PUNE-MUTA-2024",
    citations: {
      apa: "Department of Revenue. (2024). Mahabhulekh Pune Mutation Latency Dataset. Government of Maharashtra.",
      mla: "Department of Revenue. 'Mahabhulekh Pune Mutation Latency Dataset.' 2024.",
      indian_legal: "Maharashtra Land Revenue Telemetry Dataset, Pune Tehsil Series, Catalog NID: OGD-MAHA-PUNE-MUTA-2024",
      bibtex: "@misc{pune2024muta,\n  title={Pune Mutation Dataset},\n  year={2024}\n}"
    },
    last_synced_at: new Date().toISOString()
  }
];

export const MOCK_DISPUTE_ANALYTICS = {
  reporting_period: "2026-Q1 (Live NJDG Feed)",
  nationwide_active_disputes: 2409790,
  nationwide_disposal_rate: 74.2,
  total_indexed_literature: 4820,
  active_cadastral_datasets: 894,
  state_dispute_metrics: [
    {
      state_ut: "Uttar Pradesh",
      state_lgd_code: "09",
      total_active_disputes: 482190,
      cases_filed_ytd: 84200,
      cases_disposed_ytd: 64800,
      disposal_rate_percentage: 76.96,
      average_pendency_years: 4.8,
      title_ownership_disputes: 210400,
      rfctlarr_acquisition_disputes: 84500,
      tenancy_leasing_disputes: 92300,
      boundary_demarcation_disputes: 72400,
      tribal_land_alienation_disputes: 22590,
      bhu_aadhaar_seeding_percentage: 92.4,
      reform_adoption_score: 88.5
    },
    {
      state_ut: "Maharashtra",
      state_lgd_code: "27",
      total_active_disputes: 364800,
      cases_filed_ytd: 62100,
      cases_disposed_ytd: 49200,
      disposal_rate_percentage: 79.23,
      average_pendency_years: 3.9,
      title_ownership_disputes: 142000,
      rfctlarr_acquisition_disputes: 78900,
      tenancy_leasing_disputes: 58400,
      boundary_demarcation_disputes: 61200,
      tribal_land_alienation_disputes: 24300,
      bhu_aadhaar_seeding_percentage: 94.8,
      reform_adoption_score: 93.2
    },
    {
      state_ut: "Madhya Pradesh",
      state_lgd_code: "23",
      total_active_disputes: 274100,
      cases_filed_ytd: 48500,
      cases_disposed_ytd: 35400,
      disposal_rate_percentage: 72.99,
      average_pendency_years: 4.2,
      title_ownership_disputes: 118000,
      rfctlarr_acquisition_disputes: 49800,
      tenancy_leasing_disputes: 41200,
      boundary_demarcation_disputes: 38900,
      tribal_land_alienation_disputes: 26200,
      bhu_aadhaar_seeding_percentage: 88.1,
      reform_adoption_score: 84.7
    },
    {
      state_ut: "Karnataka",
      state_lgd_code: "29",
      total_active_disputes: 248900,
      cases_filed_ytd: 41200,
      cases_disposed_ytd: 33100,
      disposal_rate_percentage: 80.34,
      average_pendency_years: 3.4,
      title_ownership_disputes: 98400,
      rfctlarr_acquisition_disputes: 47200,
      tenancy_leasing_disputes: 42100,
      boundary_demarcation_disputes: 46800,
      tribal_land_alienation_disputes: 14400,
      bhu_aadhaar_seeding_percentage: 96.2,
      reform_adoption_score: 95.0
    },
    {
      state_ut: "Odisha",
      state_lgd_code: "21",
      total_active_disputes: 194200,
      cases_filed_ytd: 31900,
      cases_disposed_ytd: 23400,
      disposal_rate_percentage: 73.35,
      average_pendency_years: 4.5,
      title_ownership_disputes: 78200,
      rfctlarr_acquisition_disputes: 38400,
      tenancy_leasing_disputes: 28900,
      boundary_demarcation_disputes: 29800,
      tribal_land_alienation_disputes: 18900,
      bhu_aadhaar_seeding_percentage: 89.6,
      reform_adoption_score: 87.8
    },
    {
      state_ut: "Andhra Pradesh",
      state_lgd_code: "28",
      total_active_disputes: 182300,
      cases_filed_ytd: 34100,
      cases_disposed_ytd: 27900,
      disposal_rate_percentage: 81.82,
      average_pendency_years: 3.2,
      title_ownership_disputes: 71200,
      rfctlarr_acquisition_disputes: 39400,
      tenancy_leasing_disputes: 31200,
      boundary_demarcation_disputes: 28900,
      tribal_land_alienation_disputes: 11600,
      bhu_aadhaar_seeding_percentage: 97.4,
      reform_adoption_score: 96.1
    }
  ],
  dispute_trend_monthly: [
    { month: "Oct 2025", filed: 38200, disposed: 29400, velocity: "+3.4%" },
    { month: "Nov 2025", filed: 41500, disposed: 32800, velocity: "+4.1%" },
    { month: "Dec 2025", filed: 39100, disposed: 34600, velocity: "+2.8%" },
    { month: "Jan 2026", filed: 43200, disposed: 36100, velocity: "+5.2%" },
    { month: "Feb 2026", filed: 45800, disposed: 38400, velocity: "+6.0%" },
    { month: "Mar 2026", filed: 44100, disposed: 39800, velocity: "+4.7%" }
  ],
  top_dispute_themes: [
    { theme: "Title & Ownership Suits", count: 974200, percentage: 40.4 },
    { theme: "RFCTLARR Land Acquisition", count: 489300, percentage: 20.3 },
    { theme: "Boundary & Demarcation", count: 412400, percentage: 17.1 },
    { theme: "Tenancy & Agricultural Leases", count: 374300, percentage: 15.5 },
    { theme: "Tribal Land Alienation (FRA)", count: 159590, percentage: 6.7 }
  ]
};

export const MOCK_TELEMETRY = {
  system_status: "ALL_SYSTEMS_OPERATIONAL",
  last_global_sync: new Date().toISOString(),
  endpoints: [
    {
      endpoint_name: "e-Courts NJDG Civil Land Disputes Feed",
      endpoint_category: "e-Courts NJDG",
      target_url: "https://njdg.ecourts.gov.in/api/v4/disputes/civil-land",
      status: "OPERATIONAL",
      http_status_code: 200,
      response_time_ms: 184,
      last_synced_at: new Date(Date.now() - 4 * 60000).toISOString(),
      records_indexed: 2410880,
      error_message: null
    },
    {
      endpoint_name: "Open Government Data (OGD) Cadastral Harvester",
      endpoint_category: "data.gov.in OGD",
      target_url: "https://api.data.gov.in/resource/dolr-cadastral-baseline",
      status: "OPERATIONAL",
      http_status_code: 200,
      response_time_ms: 312,
      last_synced_at: new Date(Date.now() - 11 * 60000).toISOString(),
      records_indexed: 894,
      error_message: null
    },
    {
      endpoint_name: "DoLR / MoRD Gazette & Circulars Scraper",
      endpoint_category: "DoLR Gazette",
      target_url: "https://dolr.gov.in/api/gazette-notifications/rss",
      status: "OPERATIONAL",
      http_status_code: 200,
      response_time_ms: 245,
      last_synced_at: new Date(Date.now() - 18 * 60000).toISOString(),
      records_indexed: 3420,
      error_message: null
    },
    {
      endpoint_name: "Bhu-Aadhaar National ULPIN Directory Registry",
      endpoint_category: "Bhu-Aadhaar ULPIN",
      target_url: "https://bhu-aadhaar.gov.in/api/v2/registry/telemetry",
      status: "OPERATIONAL",
      http_status_code: 200,
      response_time_ms: 142,
      last_synced_at: new Date(Date.now() - 2 * 60000).toISOString(),
      records_indexed: 28490012,
      error_message: null
    }
  ]
};

export const TAXONOMY_STREAMS = [
  { id: "all", label: "All Repositories", label_hi: "समस्त भंडार", icon: "Layers", count: 8 },
  { id: "policy-legislation", label: "Policy & Legislation", label_hi: "नीति एवं विधान", icon: "ScrollText", count: 2 },
  { id: "academic-research", label: "Academic & Applied Research", label_hi: "शैक्षणिक एवं शोध", icon: "BookOpen", count: 1 },
  { id: "judicial-records", label: "Judicial & Land Disputes", label_hi: "न्यायिक एवं विवाद", icon: "Scale", count: 2 },
  { id: "government-datasets", label: "Government Datasets", label_hi: "सरकारी डेटासेट", icon: "Database", count: 2 },
  { id: "pilot-case-studies", label: "Best Practices & Pilots", label_hi: "सर्वोत्तम प्रथाएं", icon: "Award", count: 1 }
];
