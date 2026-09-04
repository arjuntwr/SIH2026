"""
Test suite for Live Gujarat Government Knowledge Repository and Policy Intelligence
"""
import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def test_endpoints():
    print("--- 1. Testing GET /api/v1/kb/documents (Live Gujarat Gov Repository) ---")
    r = requests.get(f"{BASE_URL}/api/v1/kb/documents", timeout=15)
    assert r.status_code == 200, f"Expected 200, got {r.status_code}: {r.text}"
    data = r.json()
    assert data["status"] == "success"
    assert "Gujarat" in data["jurisdiction"]
    docs = data.get("documents", [])
    print(f"Total live Gujarat documents retrieved: {len(docs)}")
    assert len(docs) > 0, "Expected at least 1 document from live pipeline"
    
    # Check strict Gujarat invariant and government badges
    for d in docs[:5]:
        act_title = d.get('title', '').encode('ascii', errors='replace').decode('ascii')
        print(f"  [Act] {act_title} | Badge: {d.get('official_badge')} | URL: {d.get('download_url')}")
        assert "gujarat" in d.get("jurisdiction", "").lower(), f"Non-Gujarat document detected: {d}"
        assert any(gov in (d.get("download_url", "") + d.get("official_badge", "")).lower() for gov in ["gov.in", "nic.in", "gujarat"]), f"Missing official gov URL: {d}"

    print("\n--- 2. Testing Gujarat-Specific Facet Filtering ---")
    r_filter = requests.get(f"{BASE_URL}/api/v1/kb/documents?theme=Gujarat+Land+Revenue+Code", timeout=15)
    assert r_filter.status_code == 200
    filter_data = r_filter.json()
    print(f"Filtered GLRC docs count: {filter_data.get('total_count')}")

    print("\n--- 3. Testing POST /api/v1/kb/live-synthesize (Real-Time In-Memory RAG) ---")
    synth_payload = {
        "doc_id": "DOC-GLRC-1879",
        "topic": "Section 73AA restrictions on tribal land alienation in Gujarat",
        "user_query": "What are the specific requirements under Section 73AA of Gujarat Land Revenue Code to transfer tribal land?"
    }
    r_synth = requests.post(f"{BASE_URL}/api/v1/kb/live-synthesize", json=synth_payload, timeout=20)
    assert r_synth.status_code == 200, f"Expected 200, got {r_synth.status_code}: {r_synth.text}"
    synth_data = r_synth.json()
    assert synth_data["status"] == "success"
    print("AI Synthesis Status:", synth_data.get("status"))
    print("Executive Summary:", synth_data.get("literature_summary") or synth_data.get("executive_summary"))
    print("Operational Clauses Count:", len(synth_data.get("operational_clauses", [])))
    print("Grounded Response Snippet:", (synth_data.get("grounded_response") or "")[:120], "...")

    print("\n--- 4. Testing GET /knowledge-base (Frontend UI) ---")
    r_kb = requests.get(f"{BASE_URL}/knowledge-base", timeout=10)
    assert r_kb.status_code == 200
    html = r_kb.text
    assert "Gujarat State Legal &amp; Policy Knowledge Repository (Live Official Gov Feeds)" in html or "Gujarat State Legal & Policy Knowledge Repository (Live Official Gov Feeds)" in html
    assert "Live sync active with indiacode.nic.in &amp; data.gov.in" in html or "Live sync active with indiacode.nic.in & data.gov.in" in html
    assert "Gujarat Land Revenue Code &amp; Amendments" in html or "Gujarat Land Revenue Code & Amendments" in html
    assert "Section 73AA restrictions" in html
    assert "Dholera SIR" in html
    assert "Run AI Statutory Analysis" in html
    print("Verified /knowledge-base HTML renders Gujarat jurisdiction banner, live sync badge, and Gujarat facets.")

    print("\n--- 5. Testing Invariants: GIS Map at / and /map ---")
    r_map = requests.get(f"{BASE_URL}/map", timeout=10)
    assert r_map.status_code == 200
    assert "maplibre-gl" in r_map.text
    assert "Sentinel2_10m_LandCover" in r_map.text
    print("Verified /map has MapLibre GL JS and Esri 10m LandCover raster intact.")

    r_suggest = requests.get(f"{BASE_URL}/api/v1/locations/suggest?q=Sanand", timeout=10)
    assert r_suggest.status_code == 200
    suggs = r_suggest.json()
    print(f"Suggestions for 'Sanand': {len(suggs)} found")
    assert len(suggs) > 0

    print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_endpoints()
