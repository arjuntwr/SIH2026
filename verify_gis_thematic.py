import urllib.request
import json
import sys

BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(name, url, method="GET", data=None):
    print(f"Testing {name}: {url}...", flush=True)
    if data is not None:
        encoded = json.dumps(data).encode("utf-8")
        headers = {"User-Agent": "GUJ-GIS-TEST/1.0", "Content-Type": "application/json"}
    else:
        encoded = None
        headers = {"User-Agent": "GUJ-GIS-TEST/1.0"}
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
    
    # 1. District GIS Layers
    s, body = test_endpoint("District GIS Layers", f"{BASE_URL}/api/v1/districts/Ahmedabad/gis-layers")
    if s == 200:
        data = json.loads(body)
        features = data.get("features", [])
        print(f"  Features count: {len(features)}")
        categories = {f['properties'].get('category') for f in features}
        print(f"  Categories detected: {categories}")
        required_cats = {"disputed", "government", "forest", "water", "residential"}
        if not categories.intersection(required_cats):
            print("  [ERROR] None of the required thematic categories present!")
            errors += 1

        # Check Z-Index Sorting (1: residential <= 2: forest <= 3: water <= 4: government <= 5: disputed)
        z_ranks = [f['properties'].get('z_rank', 0) for f in features]
        is_sorted = all(z_ranks[i] <= z_ranks[i+1] for i in range(len(z_ranks)-1))
        print(f"  Z-Index sorted check (residential -> forest -> water -> government -> disputed): {is_sorted}")
        if not is_sorted:
            print(f"  [ERROR] Features are not sorted by visual z_rank! ranks: {z_ranks[:10]}...")
            errors += 1

        # Check geometry types are Polygon or MultiPolygon
        geom_types = {f['geometry']['type'] for f in features}
        print(f"  Geometry types present: {geom_types}")
        invalid_types = geom_types - {"Polygon", "MultiPolygon"}
        if invalid_types:
            print(f"  [ERROR] Invalid geometry types found: {invalid_types}")
            errors += 1

        # Check non-rectangular coordinates (not simple 4-corner bounding boxes)
        for f in features[:10]:
            coords = f['geometry']['coordinates']
            cat = f['properties'].get('category')
            if f['geometry']['type'] == 'Polygon':
                ring = coords[0]
                pt_count = len(ring)
                # Check that it's not a trivial 4-corner rectangle (5 points with identical min/max lat/lons)
                xs = [p[0] for p in ring]
                ys = [p[1] for p in ring]
                unique_xs = len(set(xs))
                unique_ys = len(set(ys))
                if pt_count == 5 and unique_xs == 2 and unique_ys == 2:
                    print(f"  [ERROR] Feature {f.get('id')} ({cat}) is a synthetic axis-aligned 4-point rectangle!")
                    errors += 1
                else:
                    print(f"  [OK] Feature {f.get('id')} ({cat}) has {pt_count} vertices (organic/vector geometry).")

        # Check sequential integer IDs for MapLibre feature-state
        feature_ids = [f.get('id') for f in features]
        if any(fid is None or not isinstance(fid, int) for fid in feature_ids):
            print(f"  [ERROR] Non-integer or missing feature IDs found!")
            errors += 1
        else:
            print(f"  [OK] All {len(feature_ids)} features have integer IDs for MapLibre feature-state.")
    else:
        errors += 1

    # 2. Location Autocomplete
    s, body = test_endpoint("Suggest Autocomplete", f"{BASE_URL}/api/v1/locations/suggest?q=Dhol")
    if s == 200:
        suggestions = json.loads(body)
        print(f"  Suggestions returned: {len(suggestions)}")
        if len(suggestions) == 0:
            print("  [WARN] Zero suggestions returned")
    else:
        errors += 1

    # 3. Location Resolve
    s, body = test_endpoint("Resolve Location", f"{BASE_URL}/api/v1/resolve?query=Dholera")
    if s == 200:
        res = json.loads(body)
        print(f"  Resolved: {res.get('official_name')}")
        if res.get("geojson"):
            print(f"  Resolved GeoJSON type: {res['geojson'].get('type')}")
    else:
        errors += 1

    # 4. Simulation Endpoint
    s, body = test_endpoint("Policy Simulation", f"{BASE_URL}/api/v1/simulate?query=Dholera&buffer_meters=500&proposed_use=Industrial")
    if s != 200:
        errors += 1

    # 5. AI RAG Query
    s, body = test_endpoint("AI Query", f"{BASE_URL}/api/v1/ai/query", method="POST", data={"query": "Summary of land risk in Ahmedabad", "location": "Ahmedabad"})
    if s != 200:
        errors += 1

    # 6. Frontend HTML Verification
    s, html = test_endpoint("Frontend HTML", f"{BASE_URL}/")
    if s == 200:
        checks = [
            ("MapLibre GL JS CSS", "maplibre-gl@3.6.2/dist/maplibre-gl.css"),
            ("MapLibre GL JS Script", "maplibre-gl@3.6.2/dist/maplibre-gl.js"),
            ("Unified Source thematic-data", "thematic-data"),
            ("Tolerance 0.375", "0.375"),
            ("Data-driven Fill thematic-fills", "thematic-fills"),
            ("Dedicated Stroke thematic-borders", "thematic-borders"),
            ("Stroke width 1.8", "'line-width': 1.8"),
            ("Line Join Round", "'line-join': 'round'"),
            ("Line Cap Round", "'line-cap': 'round'"),
            ("First Symbol Insertion Hierarchy", "firstSymbolId"),
            ("Fill Color #EF4444 (Disputed)", "#EF4444"),
            ("Fill Color #3B82F6 (Government)", "#3B82F6"),
            ("Fill Color #22C55E (Forest)", "#22C55E"),
            ("Fill Color #06B6D4 (Water)", "#06B6D4"),
            ("Fill Color #F59E0B (Residential)", "#F59E0B"),
            ("Satellite Opacity 0.20/0.25 to 0.50", "SATELLITE_FILL_OPACITY"),
            ("Basemap Opacity 0.40 to 0.65", "BASEMAP_FILL_OPACITY"),
            ("Basemap Toggle Fill Opacity Adaptor", "map.setPaintProperty('thematic-fills', 'fill-opacity'"),
            ("Spotlight Mask Layer", "spotlight-mask-layer"),
            ("Boundary Stroke #38BDF8", "#38BDF8"),
            ("Floating Legend & Toggles", "map-floating-legend"),
            ("Legend Checkbox Disputed", "checkDisputed"),
            ("Legend Checkbox Government", "checkGovernment"),
            ("Legend Checkbox Forest", "checkForest"),
            ("Legend Checkbox Water", "checkWater"),
            ("Legend Checkbox Residential", "checkResidential"),
            ("FitBounds Transition", "map.fitBounds")
        ]
        for name, pattern in checks:
            if pattern in html:
                print(f"  [CHECK PASS] {name}")
            else:
                print(f"  [CHECK FAIL] {name} missing from index.html")
                errors += 1
    else:
        errors += 1

    print(f"\nFinal verification complete. Total errors: {errors}", flush=True)
    if errors > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
