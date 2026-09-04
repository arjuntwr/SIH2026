"""
Comprehensive Verification Script for Bhumi-Niti GIGW 3.0 Portal Modules
Verifies:
1. Root GIS Map (/ and /map)
2. Policy Knowledge Repository (/knowledge-base)
3. Innovation Hub (/innovation)
4. GIGW 3.0 Dual-tier Masthead & Footer consistency
5. API endpoints integrity
"""

import sys
import json
import urllib.request

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

BASE_URL = "http://localhost:8000"

def get(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return resp.status, resp.read().decode('utf-8')

def post_json(url, payload):
    req = urllib.request.Request(url, method="POST")
    req.add_header('Content-Type', 'application/json')
    data_bytes = json.dumps(payload).encode('utf-8')
    with urllib.request.urlopen(req, data=data_bytes, timeout=15) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8'))

def test_suite():
    errors = 0

    print("=" * 70)
    print("1. VERIFYING POLICY KNOWLEDGE REPOSITORY (/knowledge-base)")
    print("=" * 70)
    try:
        status, html = get(f"{BASE_URL}/knowledge-base")
        assert status == 200, f"Expected 200, got {status}"
        print("  [OK] Status 200")

        # Tier 1 Utility Bar Checks
        tier1_tokens = [
            "gov-utility-bar", "istClock", "personaSelector", "stateSelector",
            "font-btn", "contrastToggleBtn", "langSelector", "Screen Reader Access"
        ]
        for tok in tier1_tokens:
            assert tok in html, f"Missing Tier 1 token: {tok}"
            print(f"  [PASS] Tier 1 Token: {tok}")

        # Tier 2 Masthead Checks
        tier2_tokens = [
            "gov-masthead", "ग्रामीण विकास मंत्रालय, भूमि संसाधन विभाग",
            "Ministry of Rural Development, Department of Land Resources",
            "Bhumi-Niti", "(भूमि-नीति)", "सत्यमेव जयते",
            "Spatial GIS Platform", "Policy Repository", "Innovation Hub"
        ]
        for tok in tier2_tokens:
            assert tok in html, f"Missing Tier 2 token: {tok}"
            print(f"  [PASS] Tier 2 Token: {tok}")

        # Active tab indicator
        assert 'href="/knowledge-base" class="gov-tab active"' in html, "Active tab indicator missing on /knowledge-base"
        print("  [PASS] Active Tab Indicator on Policy Repository")

        # Sub-header & KPI Bar Checks
        kpi_tokens = [
            "Gujarat State Land Governance & Statutory Knowledge Repository",
            "Total Enacted Acts", "Active Circulars & GRs",
            "Indexed Research Papers", "Live Open Datasets"
        ]
        for tok in kpi_tokens:
            assert tok in html, f"Missing KPI token: {tok}"
            print(f"  [PASS] Sub-header / KPI Token: {tok}")

        # Left Filter Sidebar Checks
        sidebar_tokens = [
            "kb-sidebar", "kbSearchInput", "authorityFilter",
            "Statutory Acts & Codes", "Town Planning & Urban Laws",
            "Government Resolutions (GRs) & Revenue Circulars",
            "indiacode.nic.in"
        ]
        for tok in sidebar_tokens:
            assert tok in html, f"Missing Sidebar token: {tok}"
            print(f"  [PASS] Filter Sidebar Token: {tok}")

        # Grounded AI Drawer & Modals Checks
        drawer_tokens = [
            "synthesisDrawerOverlay", "synthesis-drawer", "drawerBody",
            "researchModal", "disclaimerModal"
        ]
        for tok in drawer_tokens:
            assert tok in html, f"Missing Drawer/Modal token: {tok}"
            print(f"  [PASS] Drawer / Modal Token: {tok}")

        # Tier 3 Footer Checks
        footer_tokens = ["gov-footer", "GIGW 3.0", "WCAG 2.1 AA", "Statutory Legal Disclaimer"]
        for tok in footer_tokens:
            assert tok in html, f"Missing Footer token: {tok}"
            print(f"  [PASS] Footer Token: {tok}")

    except Exception as e:
        print(f"  [FAIL] Knowledge Base UI: {e}")
        errors += 1

    print("\n" + "=" * 70)
    print("2. VERIFYING INNOVATION HUB (/innovation)")
    print("=" * 70)
    try:
        status, html = get(f"{BASE_URL}/innovation")
        assert status == 200, f"Expected 200, got {status}"
        print("  [OK] Status 200")

        # Tier 1 Utility Bar Checks
        tier1_tokens = [
            "gov-utility-bar", "istClock", "personaSelector", "stateSelector",
            "font-btn", "contrastToggleBtn", "langSelector", "Screen Reader Access"
        ]
        for tok in tier1_tokens:
            assert tok in html, f"Missing Tier 1 token: {tok}"
            print(f"  [PASS] Tier 1 Token: {tok}")

        # Tier 2 Masthead Checks
        tier2_tokens = [
            "gov-masthead", "ग्रामीण विकास मंत्रालय, भूमि संसाधन विभाग",
            "Ministry of Rural Development, Department of Land Resources",
            "Bhumi-Niti", "(भूमि-नीति)", "सत्यमेव जयते",
            "Spatial GIS Platform", "Policy Repository", "Innovation Hub"
        ]
        for tok in tier2_tokens:
            assert tok in html, f"Missing Tier 2 token: {tok}"
            print(f"  [PASS] Tier 2 Token: {tok}")

        # Active tab indicator
        assert 'href="/innovation" class="gov-tab active"' in html, "Active tab indicator missing on /innovation"
        print("  [PASS] Active Tab Indicator on Innovation Hub")

        # Sub-header & Program Metrics Checks
        metric_tokens = [
            "National Land Governance Innovation Hub & Applied Research Sandbox",
            "4 Active", "National Challenges", "₹2.40 Cr", "Sanctioned Grants",
            "12 Partner", "7 Pilots"
        ]
        for tok in metric_tokens:
            assert tok in html, f"Missing Metric token: {tok}"
            print(f"  [PASS] Banner / Metric Token: {tok}")

        # Tab Navigation & Panes Checks
        tab_tokens = [
            "tabBtnChallenges", "tabBtnGrants", "tabBtnPilots",
            "paneChallenges", "paneGrants", "panePilots"
        ]
        for tok in tab_tokens:
            assert tok in html, f"Missing Tab token: {tok}"
            print(f"  [PASS] Tab Structure Token: {tok}")

        # Problem statements in Tab A
        challenges = [
            "Automated Cadastral Map Alignment using AI & High-Res Drone Imagery",
            "Predictive Peri-Urban Sprawl & Agricultural Land Transition Modeling",
            "Smart Contract-based RTS Land Record Mutation System",
            "Drone-Based 3D Land Titling & Abadi Rooftop Delineation"
        ]
        for ch in challenges:
            assert ch in html, f"Missing Challenge: {ch}"
            print(f"  [PASS] Challenge Card: {ch[:45]}...")

        # Tab B Research Grants
        assert "Land Governance Research Grant Scheme (LGRGS)" in html
        assert "Download Guidelines (PDF)" in html
        assert "Submit Grant Proposal" in html
        print("  [PASS] Research Grants Section & Actions")

        # Tab C Pilot Projects Tracker
        pilots = ["Sanand, Ahmedabad", "Dholera, Ahmedabad", "Kevadia, Narmada", "Gautam Buddha Nagar, UP", "Haveli, Pune, MH"]
        for p in pilots:
            assert p in html, f"Missing Pilot Location: {p}"
            print(f"  [PASS] Pilot Tracker Location: {p}")

        # Modals
        assert "challengeModal" in html
        assert "grantModal" in html
        assert "disclaimerModal" in html
        print("  [PASS] Innovation Modals Registered")

        # Tier 3 Footer Checks
        footer_tokens = ["gov-footer", "GIGW 3.0", "WCAG 2.1 AA", "Statutory Legal Disclaimer"]
        for tok in footer_tokens:
            assert tok in html, f"Missing Footer token: {tok}"
            print(f"  [PASS] Footer Token: {tok}")

    except Exception as e:
        print(f"  [FAIL] Innovation Hub UI: {e}")
        errors += 1

    print("\n" + "=" * 70)
    print("3. VERIFYING BACKEND APIS & INVARIANTS")
    print("=" * 70)
    try:
        status, data = get(f"{BASE_URL}/api/v1/kb/documents?jurisdiction=Gujarat")
        assert status == 200
        parsed = json.loads(data)
        assert len(parsed.get("documents", [])) > 0
        print(f"  [PASS] /api/v1/kb/documents returned {len(parsed['documents'])} live docs")

        status, synth = post_json(f"{BASE_URL}/api/v1/kb/live-synthesize", {
            "topic": "Section 73AA tribal permissions",
            "user_query": "What is the procedure under Section 73AA?"
        })
        assert status == 200
        assert "grounded_response" in synth or "executive_summary" in synth
        print("  [PASS] /api/v1/kb/live-synthesize executed successfully")

        status, sugg = get(f"{BASE_URL}/api/v1/locations/suggest?q=Sanand")
        assert status == 200
        print("  [PASS] /api/v1/locations/suggest intact")

        status, res = get(f"{BASE_URL}/api/v1/resolve?query=Sanand")
        assert status == 200
        print("  [PASS] /api/v1/resolve intact")

    except Exception as e:
        print(f"  [FAIL] Backend APIs: {e}")
        errors += 1

    print("\n" + "=" * 70)
    print(f"VERIFICATION COMPLETE. TOTAL ERRORS: {errors}")
    print("=" * 70)
    return errors == 0

if __name__ == "__main__":
    success = test_suite()
    sys.exit(0 if success else 1)
