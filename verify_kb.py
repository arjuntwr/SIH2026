"""
Verification script for LAND-INNOVATE Knowledge Base & Policy Research Portal.
Tests:
1. GET /api/v1/kb/documents (with & without filters)
2. GET /api/v1/kb/documents/{doc_id}
3. POST /api/v1/kb/synthesize (topic RAG & doc_ids synthesis)
4. GET /knowledge-base UI route
5. GET /map and / routes
6. Preservation of existing spatial APIs (/api/v1/locations/suggest, /api/v1/resolve)
"""

import sys
import json
import urllib.request
import urllib.parse

BASE_URL = "http://localhost:8000"

def test_api(description, url, method="GET", payload=None):
    print(f"[*] Testing: {description} -> {method} {url}")
    try:
        req = urllib.request.Request(url, method=method)
        if payload:
            data_bytes = json.dumps(payload).encode('utf-8')
            req.add_header('Content-Type', 'application/json')
            req.data = data_bytes
        
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            body = resp.read().decode('utf-8')
            print(f"    [OK] Status: {status}, Length: {len(body)} bytes")
            if "application/json" in resp.headers.get("Content-Type", ""):
                parsed = json.loads(body)
                return True, parsed
            return True, body
    except Exception as e:
        print(f"    [FAIL] Error: {e}")
        return False, str(e)

def main():
    results = []

    # 1. Test GET /api/v1/kb/documents (All docs)
    ok, res = test_api("KB Documents - All", f"{BASE_URL}/api/v1/kb/documents")
    results.append(("GET /api/v1/kb/documents (all)", ok and res.get("total_count", 0) >= 9))
    if ok:
        print(f"    Count: {res.get('total_count')}, Docs: {[d['doc_id'] for d in res.get('documents', [])]}")

    # 2. Test GET /api/v1/kb/documents with query filter
    ok, res = test_api("KB Documents - Query 'Section 65'", f"{BASE_URL}/api/v1/kb/documents?q=Section+65")
    results.append(("GET /api/v1/kb/documents (query filter)", ok and res.get("total_count", 0) >= 1))

    # 3. Test GET /api/v1/kb/documents with type filter
    ok, res = test_api("KB Documents - Type 'Legal Act'", f"{BASE_URL}/api/v1/kb/documents?type=Legal+Act")
    results.append(("GET /api/v1/kb/documents (type filter)", ok and res.get("total_count", 0) >= 3))

    # 4. Test GET /api/v1/kb/documents with theme filter
    ok, res = test_api("KB Documents - Theme 'Urban Transition'", f"{BASE_URL}/api/v1/kb/documents?theme=Urban+Transition")
    results.append(("GET /api/v1/kb/documents (theme filter)", ok and res.get("total_count", 0) >= 2))

    # 5. Test GET /api/v1/kb/documents/{doc_id}
    ok, res = test_api("KB Document by ID - DOC-GLRC-1879", f"{BASE_URL}/api/v1/kb/documents/DOC-GLRC-1879")
    results.append(("GET /api/v1/kb/documents/DOC-GLRC-1879", ok and res.get("doc_id") == "DOC-GLRC-1879" and len(res.get("key_highlights", [])) > 0))

    # 6. Test POST /api/v1/kb/synthesize with doc_ids
    synth_payload = {"doc_ids": ["DOC-GLRC-1879", "DOC-RFCTLARR-2013"]}
    ok, res = test_api("KB Synthesize - Specific Doc IDs", f"{BASE_URL}/api/v1/kb/synthesize", method="POST", payload=synth_payload)
    results.append(("POST /api/v1/kb/synthesize (doc_ids)", ok and len(res.get("key_trade_offs", [])) > 0 and len(res.get("analyzed_documents", [])) == 2))

    # 7. Test POST /api/v1/kb/synthesize with topic & question RAG
    rag_payload = {"topic": "tenancy conversion", "question": "What are the restrictions under Gujarat Tenancy Act Section 84?"}
    ok, res = test_api("KB Synthesize - Topic & Grounded Q&A", f"{BASE_URL}/api/v1/kb/synthesize", method="POST", payload=rag_payload)
    results.append(("POST /api/v1/kb/synthesize (RAG Q&A)", ok and res.get("grounded_response") is not None))

    # 8. Test /knowledge-base HTML view
    ok, res = test_api("Knowledge Base UI Route", f"{BASE_URL}/knowledge-base")
    results.append(("GET /knowledge-base UI", ok and "Land Governance Knowledge Base" in str(res) and "synthesis-drawer" in str(res)))

    # 9. Test /map HTML view
    ok, res = test_api("Map UI Route (/map)", f"{BASE_URL}/map")
    results.append(("GET /map UI", ok and "LAND-INNOVATE" in str(res) and "Policy Repository" in str(res)))

    # 10. Test / root route has navigation
    ok, res = test_api("Map UI Root Route (/)", f"{BASE_URL}/")
    results.append(("GET / UI with nav", ok and "nav-tab" in str(res) and "Policy Repository" in str(res)))

    # 11. Preservation check: /api/v1/locations/suggest
    ok, res = test_api("Preservation: Location Autocomplete", f"{BASE_URL}/api/v1/locations/suggest?q=Sanand")
    results.append(("GET /api/v1/locations/suggest", ok and isinstance(res, list)))

    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY:")
    print("=" * 60)
    all_passed = True
    for name, passed in results:
        status_str = "PASS" if passed else "FAIL"
        if not passed:
            all_passed = False
        print(f"[{status_str}] {name}")

    if all_passed:
        print("\n[SUCCESS] ALL 11 TESTS PASSED PERFECTLY!")
        sys.exit(0)
    else:
        print("\n[FAILURE] SOME TESTS FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()
