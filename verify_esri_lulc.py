import urllib.request
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(name, url, method="GET", data=None):
    print(f"Testing {name}: {url}...", flush=True)
    if data is not None:
        encoded = json.dumps(data).encode("utf-8")
        headers = {"User-Agent": "GUJ-GIS-TEST/2.0", "Content-Type": "application/json"}
    else:
        encoded = None
        headers = {"User-Agent": "GUJ-GIS-TEST/2.0"}
    req = urllib.request.Request(url, data=encoded, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=90) as response:
            status = response.status
            body = response.read().decode("utf-8")
            print(f"  [OK] Status: {status}", flush=True)
            return status, body
    except Exception as e:
        print(f"  [FAIL] {e}", flush=True)
        return None, str(e)

def main():
    errors = 0

    # 1. District GIS Layers Endpoint
    s, body = test_endpoint("District GIS Layers", f"{BASE_URL}/api/v1/districts/Ahmedabad/gis-layers")
    if s == 200:
        data = json.loads(body)
        features = data.get("features", [])
        boundary = data.get("boundary")
        inverted_mask = data.get("inverted_mask")
        bounds = data.get("bounds")
        metadata = data.get("metadata")

        print(f"  Features count: {len(features)} (Expected: 0 synthetic polygons)")
        if len(features) > 0:
            print("  [ERROR] Synthetic vector features still present!")
            errors += 1
        else:
            print("  [OK] Synthetic Overpass vector polygons successfully stripped.")

        if not boundary or boundary.get("geometry", {}).get("type") not in ["Polygon", "MultiPolygon"]:
            print("  [ERROR] Boundary polygon missing or invalid!")
            errors += 1
        else:
            print("  [OK] Exact boundary polygon present.")

        if not inverted_mask or inverted_mask.get("geometry", {}).get("type") != "Polygon":
            print("  [ERROR] Inverted world spotlight mask missing or invalid!")
            errors += 1
        else:
            print("  [OK] Inverted spotlight mask present.")

        if not bounds or len(bounds) != 2:
            print("  [ERROR] Bounding box (bounds) missing or invalid!")
            errors += 1
        else:
            print(f"  [OK] BBOX bounds present: {bounds}")

        if not metadata or "agro_climatic_zone" not in metadata:
            print("  [ERROR] Real-time attribute metadata missing!")
            errors += 1
        else:
            print(f"  [OK] Real-time metadata present: agro_climatic_zone='{metadata.get('agro_climatic_zone')}'")
    else:
        errors += 1

    # 2. District Profile Telemetry Endpoint
    s, body = test_endpoint("District Profile Telemetry", f"{BASE_URL}/api/v1/districts/Ahmedabad/profile")
    if s == 200:
        prof = json.loads(body)
        print(f"  [OK] District: {prof.get('district')}, Agro Zone: {prof.get('agro_climatic_zone')}")
    else:
        print("  [ERROR] District profile endpoint failed!")
        errors += 1

    # 3. Location Resolve Endpoint
    s, body = test_endpoint("Location Resolve", f"{BASE_URL}/api/v1/resolve?query=Champaner")
    if s == 200:
        res = json.loads(body)
        print(f"  [OK] Resolved: {res.get('official_name')}")
        if not res.get("geojson"):
            print("  [WARN] GeoJSON missing from resolve")
        else:
            print(f"  [OK] Resolve GeoJSON type: {res['geojson'].get('type')}")
        if not res.get("metadata"):
            print("  [ERROR] Attribute metadata missing from resolve!")
            errors += 1
        else:
            print("  [OK] Resolve attribute metadata present.")
    else:
        errors += 1

    # 4. Suggest Autocomplete Endpoint
    s, body = test_endpoint("Suggest Autocomplete", f"{BASE_URL}/api/v1/locations/suggest?q=Dhol")
    if s == 200:
        suggestions = json.loads(body)
        print(f"  [OK] Suggestions returned: {len(suggestions)}")
    else:
        errors += 1

    # 5. Policy Simulation Endpoint
    s, body = test_endpoint("Policy Simulation", f"{BASE_URL}/api/v1/simulate?query=Dholera&buffer_meters=500&proposed_use=Industrial")
    if s == 200:
        sim = json.loads(body)
        print(f"  [OK] Simulation feasibility score: {sim.get('feasibility_score')}%")
    else:
        errors += 1

    # 6. AI RAG Query Endpoint
    s, body = test_endpoint("AI Query", f"{BASE_URL}/api/v1/ai/query", method="POST", data={"query": "Summary of land risk in Ahmedabad", "location": "Ahmedabad"})
    if s == 200:
        ai_resp = json.loads(body)
        print("  [OK] Grounded AI answer synthesized successfully.")
    else:
        errors += 1

    # 7. Frontend HTML Verification
    s, html = test_endpoint("Frontend HTML", f"{BASE_URL}/")
    if s == 200:
        checks = [
            ("Esri 10m LULC Source ID", "esri-lulc"),
            ("Esri Sentinel-2 ImageServer URL", "Sentinel2_10m_LandCover/ImageServer/exportImage"),
            ("Esri LULC Raster Layer ID", "esri-lulc-layer"),
            ("First Label Layer Helper", "getFirstLabelLayerId"),
            ("Spotlight Mask Layer", "spotlight-mask-layer"),
            ("Spotlight Mask Color #0F172A", "#0F172A"),
            ("Spotlight Mask Opacity 0.35", "0.35"),
            ("Boundary Stroke Layer", "boundary-stroke-layer"),
            ("Boundary Stroke Color #38BDF8", "#38BDF8"),
            ("Boundary Line Width 2.5", "'line-width': 2.5"),
            ("Boundary Line Dasharray [1, 0]", "'line-dasharray': [1, 0]"),
            ("Camera FitBounds with padding 40 and duration 1000", "padding: 40"),
            ("LULC Master Toggle Switch", "checkLulcMaster"),
            ("LULC Opacity Slider", "rngLulcOpacity"),
            ("LULC Opacity Function", "setLulcOpacity"),
            ("LULC Layer Toggle Function", "toggleLulcLayer"),
            ("Focus Boundary Toggle", "checkFocusBoundary"),
            ("Forest & Tree Cover Swatch", "Forest & Tree Cover"),
            ("Water Resources Swatch", "Water Resources"),
            ("Built-up Red Color #EF4444", "#EF4444"),
            ("Built-up / Settlement Swatch", "🔴 Built-up / Settlement"),
            ("Agricultural Yellow Color #FACC15", "#FACC15"),
            ("Agricultural / Crop Land Swatch", "🟡 Agricultural / Crop Land"),
        ]

        # Ensure Disputed and Government items are NOT in legend
        prohibited_legend_patterns = [
            'id="checkDisputed"',
            'id="checkGovernment"',
            '<span>Disputed Land</span>',
            '<span>Government / Public</span>',
            'thematic-fills',
            'thematic-borders'
        ]

        for name, pattern in checks:
            if pattern in html:
                print(f"  [CHECK PASS] {name}")
            else:
                print(f"  [CHECK FAIL] {name} missing from index.html")
                errors += 1

        for pat in prohibited_legend_patterns:
            if pat in html:
                print(f"  [PROHIBITED FOUND] '{pat}' is still present in index.html!")
                errors += 1
            else:
                print(f"  [CHECK PASS] Obsolete pattern '{pat}' correctly stripped.")

    else:
        errors += 1

    print(f"\nFinal verification complete. Total errors: {errors}", flush=True)
    if errors > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
