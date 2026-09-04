"""
Bhumi-Niti (भूमि-नीति): Innovation & Challenges Hub View (Req 15)
Dedicated /innovation portal showcasing:
1. Active DoLR Innovation Challenges (National Hackathon & Grand Challenges 2026)
2. Academic Research Grant Application Pipeline for Universities
3. State Land Reform Pilot Projects Live Tracker
"""

def render_innovation_html() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bhumi-Niti (भूमि-नीति) | DoLR Land Governance Innovation Hub & Research Grants</title>
  <meta name="description" content="Bhumi-Niti Innovation Hub — Active DoLR Innovation Challenges, University Research Grants, and State Land Reform Pilot Projects. DoLR, Ministry of Rural Development.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <style>
    :root {
      --bg-base: #060911;
      --bg-surface: #0E1526;
      --bg-card: #131D31;
      --bg-card-hover: #1A2744;
      --border-subtle: #1E2D4A;
      --border-strong: #2D4168;
      --accent: #F59E0B;
      --accent-hover: #D97706;
      --accent-glow: rgba(245, 158, 11, 0.2);
      --cyan: #38BDF8;
      --cyan-glow: rgba(56, 189, 248, 0.2);
      --text-main: #F1F5F9;
      --text-dim: #94A3B8;
      --text-muted: #64748B;
      --green: #10B981;
      --green-glow: rgba(16, 185, 129, 0.25);
      --red: #EF4444;
      --purple: #A855F7;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg-base);
      color: var(--text-main);
      font-family: 'Inter', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Scrollbars */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--bg-base); }
    ::-webkit-scrollbar-thumb { background: var(--border-strong); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--accent); }

    /* Header */
    header {
      background: rgba(14, 21, 38, 0.96);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-subtle);
      padding: 12px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      flex-shrink: 0;
      gap: 16px;
    }
    .brand-section {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .brand-logo {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: linear-gradient(135deg, #F59E0B, #B45309);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.1rem;
      color: #060911;
      box-shadow: 0 0 16px var(--accent-glow);
    }
    .brand-title h1 {
      font-size: 1.1rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .tag-engine {
      font-size: 0.68rem;
      padding: 2px 7px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid var(--accent);
      color: var(--accent);
      border-radius: 4px;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
    }
    .brand-title p {
      font-size: 0.74rem;
      color: var(--text-dim);
      margin-top: 1px;
    }

    /* Global Navigation */
    .global-nav {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(6, 9, 17, 0.6);
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
    }
    .nav-tab {
      padding: 6px 14px;
      border-radius: 6px;
      color: var(--text-dim);
      font-size: 0.82rem;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .nav-tab:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }
    .nav-tab.active {
      color: #FFF;
      background: var(--accent);
      color: #060911;
      font-weight: 700;
      box-shadow: 0 0 12px var(--accent-glow);
    }

    /* Header Controls */
    .header-controls {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .selector-box {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(19, 29, 49, 0.9);
      border: 1px solid var(--border-strong);
      padding: 4px 10px;
      border-radius: 8px;
      font-size: 0.78rem;
    }
    .selector-label {
      color: var(--text-dim);
      font-size: 0.72rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .custom-dropdown {
      background: transparent;
      border: none;
      color: var(--accent);
      font-family: 'Inter', sans-serif;
      font-size: 0.80rem;
      font-weight: 600;
      cursor: pointer;
      outline: none;
    }
    .custom-dropdown option {
      background: var(--bg-surface);
      color: var(--text-main);
    }

    /* Hero Section */
    .hero-section {
      background: linear-gradient(180deg, rgba(245, 158, 11, 0.08) 0%, rgba(6, 9, 17, 0) 100%);
      border-bottom: 1px solid var(--border-subtle);
      padding: 40px 32px 30px;
    }
    .hero-container {
      max-width: 1280px;
      margin: 0 auto;
    }
    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 4px 12px;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 20px;
      color: var(--accent);
      font-size: 0.78rem;
      font-weight: 600;
      margin-bottom: 16px;
    }
    .hero-title {
      font-size: 2.2rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.2;
      margin-bottom: 12px;
      background: linear-gradient(135deg, #FFFFFF 40%, var(--accent) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
      font-size: 1.0rem;
      color: var(--text-dim);
      max-width: 820px;
      line-height: 1.6;
      margin-bottom: 28px;
    }

    /* Metric Grid */
    .kpi-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-top: 10px;
    }
    .kpi-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      position: relative;
      overflow: hidden;
    }
    .kpi-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, var(--accent), transparent);
    }
    .kpi-val {
      font-size: 1.6rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: #FFF;
    }
    .kpi-title {
      font-size: 0.80rem;
      color: var(--text-dim);
      font-weight: 500;
    }
    .kpi-note {
      font-size: 0.72rem;
      color: var(--green);
      font-weight: 600;
      margin-top: 2px;
    }

    /* Main Container */
    .main-content {
      max-width: 1280px;
      margin: 0 auto;
      padding: 36px 32px 60px;
      width: 100%;
      flex: 1;
    }

    /* Section Headers */
    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-subtle);
    }
    .section-title-box h2 {
      font-size: 1.4rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .section-title-box p {
      font-size: 0.85rem;
      color: var(--text-dim);
      margin-top: 4px;
    }
    .btn-action-primary {
      background: var(--accent);
      color: #060911;
      padding: 8px 18px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.85rem;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn-action-primary:hover {
      background: var(--accent-hover);
      box-shadow: 0 0 16px var(--accent-glow);
    }

    /* Challenge Cards Grid */
    .challenge-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 20px;
      margin-bottom: 48px;
    }
    .challenge-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s;
      position: relative;
    }
    .challenge-card:hover {
      border-color: var(--accent);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .challenge-badge-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .badge-tag {
      font-size: 0.72rem;
      font-family: 'JetBrains Mono', monospace;
      padding: 3px 8px;
      border-radius: 4px;
      font-weight: 600;
      background: rgba(56, 189, 248, 0.12);
      color: var(--cyan);
      border: 1px solid rgba(56, 189, 248, 0.3);
    }
    .badge-status {
      font-size: 0.70rem;
      padding: 3px 8px;
      border-radius: 20px;
      font-weight: 600;
      background: rgba(16, 185, 129, 0.15);
      color: var(--green);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .challenge-card h3 {
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 10px;
      line-height: 1.3;
      color: #FFF;
    }
    .challenge-desc {
      font-size: 0.85rem;
      color: var(--text-dim);
      line-height: 1.55;
      margin-bottom: 18px;
      flex: 1;
    }
    .challenge-metrics {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      padding: 12px;
      background: rgba(6, 9, 17, 0.5);
      border-radius: 8px;
      margin-bottom: 16px;
      border: 1px solid rgba(255,255,255,0.05);
    }
    .cm-val {
      font-size: 1.05rem;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      color: var(--accent);
    }
    .cm-lbl {
      font-size: 0.70rem;
      color: var(--text-dim);
    }
    .btn-apply-challenge {
      width: 100%;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid var(--accent);
      color: var(--accent);
      padding: 10px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.82rem;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-apply-challenge:hover {
      background: var(--accent);
      color: #060911;
    }

    /* Grant Themes Section */
    .grant-box {
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.08) 0%, rgba(19, 29, 49, 0.6) 100%);
      border: 1px solid var(--border-strong);
      border-radius: 16px;
      padding: 32px;
      margin-bottom: 50px;
    }
    .grant-themes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 18px;
      margin: 24px 0 28px;
    }
    .grant-theme-card {
      background: rgba(6, 9, 17, 0.7);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 18px;
    }
    .grant-theme-card h4 {
      font-size: 0.95rem;
      color: #FFF;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .grant-theme-card p {
      font-size: 0.80rem;
      color: var(--text-dim);
      line-height: 1.5;
    }

    /* Pilot Table */
    .table-responsive {
      overflow-x: auto;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 14px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      text-align: left;
    }
    th {
      background: rgba(6, 9, 17, 0.8);
      padding: 14px 18px;
      color: var(--text-dim);
      font-weight: 600;
      border-bottom: 1px solid var(--border-strong);
      font-size: 0.76rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    td {
      padding: 16px 18px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-main);
    }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: rgba(255, 255, 255, 0.02); }
    .progress-bar-wrap {
      width: 140px;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 3px;
      overflow: hidden;
      margin-top: 4px;
    }
    .progress-fill {
      height: 100%;
      background: var(--green);
      border-radius: 3px;
    }
    .state-badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 600;
      background: rgba(245, 158, 11, 0.15);
      color: var(--accent);
    }

    /* Modals */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .modal-dialog {
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      border-radius: 16px;
      width: 100%;
      max-width: 600px;
      max-height: 90vh;
      overflow-y: auto;
      padding: 28px;
      position: relative;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
    }
    .modal-close {
      position: absolute;
      top: 20px;
      right: 20px;
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-size: 1.2rem;
      cursor: pointer;
    }
    .form-group {
      margin-bottom: 16px;
    }
    .form-group label {
      display: block;
      font-size: 0.80rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 6px;
    }
    .form-control {
      width: 100%;
      background: var(--bg-base);
      border: 1px solid var(--border-strong);
      border-radius: 8px;
      padding: 10px 14px;
      color: #FFF;
      font-family: 'Inter', sans-serif;
      font-size: 0.85rem;
      outline: none;
    }
    .form-control:focus {
      border-color: var(--accent);
    }
    .form-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
    }

    /* Toast Notification */
    .toast-notice {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--bg-card);
      border: 1px solid var(--green);
      border-radius: 10px;
      padding: 14px 20px;
      color: #FFF;
      font-size: 0.85rem;
      display: none;
      align-items: center;
      gap: 10px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      z-index: 3000;
    }
  </style>
</head>
<body>

  <!-- Top Global Navigation Bar -->
  <header>
    <div class="brand-section">
      <div class="brand-logo">BN</div>
      <div class="brand-title">
        <h1>Bhumi-Niti <span class="tag-engine">भूमि-नीति</span></h1>
        <p>National Digital Platform for Evidence-Based Land Governance | DoLR, Ministry of Rural Development</p>
      </div>
    </div>

    <!-- Live Multi-Page Routing Links -->
    <nav class="global-nav">
      <a href="/" class="nav-tab">🗺️ Spatial GIS Map</a>
      <a href="/knowledge-base" class="nav-tab">📚 Policy Repository</a>
      <a href="/innovation" class="nav-tab active">💡 Innovation & Challenges</a>
    </nav>

    <!-- Header Controls: Persona Switcher & State Switcher (Req 17 & 10) -->
    <div class="header-controls">
      <div class="selector-box">
        <span class="selector-label">Role:</span>
        <select id="personaSelector" class="custom-dropdown" onchange="onPersonaChange(this.value)">
          <option value="citizen">👤 Public Citizen</option>
          <option value="researcher">🔬 Academic Researcher</option>
          <option value="official">🏛️ DoLR Policy Official</option>
        </select>
      </div>

      <div class="selector-box">
        <span class="selector-label">State:</span>
        <select id="stateSelector" class="custom-dropdown" onchange="onStateChange(this.value)">
          <option value="gujarat">Gujarat (Active Pilot)</option>
          <option value="up">Uttar Pradesh (Demo)</option>
          <option value="maharashtra">Maharashtra (Demo)</option>
        </select>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero-section">
    <div class="hero-container">
      <div class="hero-tag">🚀 Problem Statement 26019: Innovation & Research Acceleration</div>
      <h1 class="hero-title">DoLR Land Governance Innovation Hub & Research Grants</h1>
      <p class="hero-subtitle">
        Accelerating technology-driven land administration, spatial AI pipelines, and evidence-based legal research across Indian states. Bridging academia, startups, and district administration under the Department of Land Resources (MoRD).
      </p>

      <div class="kpi-row">
        <div class="kpi-card">
          <div class="kpi-val">3 Open</div>
          <div class="kpi-title">National Innovation Challenges</div>
          <div class="kpi-note">₹80 Lakhs Active Prize Pool</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-val">₹3.50 Cr</div>
          <div class="kpi-title">Academic Fellowship Allocation</div>
          <div class="kpi-note">18 University Labs Eligible</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-val">6 States</div>
          <div class="kpi-title">Active Reform Pilot Trackers</div>
          <div class="kpi-note">2.82 Lakh Villages Monitored</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-val">98.6%</div>
          <div class="kpi-title">Cadastral Map Digitization (DILRMP)</div>
          <div class="kpi-note">National Baseline Telemetry</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Container -->
  <main class="main-content">
    
    <!-- SECTION 1: Active DoLR Innovation Challenges -->
    <div class="section-header">
      <div class="section-title-box">
        <h2>🏆 Active DoLR Innovation Challenges 2026</h2>
        <p>Open GovTech Grand Challenges for startups, researchers, and tech consortia to modernize land administration.</p>
      </div>
    </div>

    <div class="challenge-grid">
      
      <!-- Challenge 1 -->
      <div class="challenge-card">
        <div>
          <div class="challenge-badge-row">
            <span class="badge-tag">AI / Computer Vision</span>
            <span class="badge-status">Submissions Open</span>
          </div>
          <h3>Automated Satbara & Cadastral AI 2026</h3>
          <p class="challenge-desc">
            Develop end-to-end computer vision pipelines capable of extracting multilingual, hand-annotated cadastral village maps (Village Form 7/12, 8A, Tipan) into geo-referenced GeoJSON vector parcels linked with 16-digit ULPIN / Bhu-Aadhaar.
          </p>
          <div class="challenge-metrics">
            <div>
              <div class="cm-val">₹25,00,000</div>
              <div class="cm-lbl">Grand Prize Pool</div>
            </div>
            <div>
              <div class="cm-val">15 Oct 2026</div>
              <div class="cm-lbl">Submission Deadline</div>
            </div>
          </div>
        </div>
        <button class="btn-apply-challenge" onclick="openChallengeModal('Automated Satbara & Cadastral AI 2026')">
          🚀 Submit Solution / Register Team
        </button>
      </div>

      <!-- Challenge 2 -->
      <div class="challenge-card">
        <div>
          <div class="challenge-badge-row">
            <span class="badge-tag">SVAMITVA 2.0 / Drone LiDAR</span>
            <span class="badge-status">Phase 1 Active</span>
          </div>
          <h3>Drone-Based 3D Land Titling & Abadi Mapping</h3>
          <p class="challenge-desc">
            High-precision photogrammetry and point-cloud elevation extraction to generate 3D digital twins of rural abadi lands with sub-5cm vertical accuracy, automated rooftop boundary delineation, and property card linking.
          </p>
          <div class="challenge-metrics">
            <div>
              <div class="cm-val">₹35,00,000</div>
              <div class="cm-lbl">Grand Prize Pool</div>
            </div>
            <div>
              <div class="cm-val">30 Nov 2026</div>
              <div class="cm-lbl">Submission Deadline</div>
            </div>
          </div>
        </div>
        <button class="btn-apply-challenge" onclick="openChallengeModal('Drone-Based 3D Land Titling & Abadi Mapping')">
          🚀 Submit Solution / Register Team
        </button>
      </div>

      <!-- Challenge 3 -->
      <div class="challenge-card">
        <div>
          <div class="challenge-badge-row">
            <span class="badge-tag">Graph AI / Risk Telemetry</span>
            <span class="badge-status">Submissions Open</span>
          </div>
          <h3>Predictive Fraud & Mutation Anomaly Detection</h3>
          <p class="challenge-desc">
            Machine learning graph models analyzing historical land mutation ledgers, partition deeds, and civil court stay records to detect anomalous title transfers, benami transactions, and high-risk unauthorized subdivisions.
          </p>
          <div class="challenge-metrics">
            <div>
              <div class="cm-val">₹20,00,000</div>
              <div class="cm-lbl">Grand Prize Pool</div>
            </div>
            <div>
              <div class="cm-val">10 Dec 2026</div>
              <div class="cm-lbl">Submission Deadline</div>
            </div>
          </div>
        </div>
        <button class="btn-apply-challenge" onclick="openChallengeModal('Predictive Fraud & Mutation Anomaly Detection')">
          🚀 Submit Solution / Register Team
        </button>
      </div>

    </div>

    <!-- SECTION 2: Academic Research Grants -->
    <div class="grant-box">
      <div class="section-header" style="border-bottom-color: rgba(255,255,255,0.1);">
        <div class="section-title-box">
          <h2 style="color:var(--cyan);">🎓 DoLR Academic Fellowship & Research Grants 2026-27</h2>
          <p>Direct grant funding for Indian Universities, IITs, IIMs, and NLUs to produce evidence-based statutory policy research.</p>
        </div>
        <button class="btn-action-primary" onclick="openGrantModal()">
          <span>📝</span>
          <span>Apply for Research Grant</span>
        </button>
      </div>

      <div class="grant-themes-grid">
        <div class="grant-theme-card">
          <h4>📊 Spatial Econometrics & Jantri Capture</h4>
          <p>Empirical evaluation of periodic Jantri revisions on urban infrastructure finance, municipal revenue buoyancy, and affordable housing land banking.</p>
        </div>
        <div class="grant-theme-card">
          <h4>🌾 Tenancy Formalization & Agricultural Yield</h4>
          <p>Assessing registered agricultural tenancy under Model Land Leasing Act vs. customary oral tenancies across Gujarat, Maharashtra, and UP.</p>
        </div>
        <div class="grant-theme-card">
          <h4>🌲 Carbon Credit Agro-Forestry Cadastres</h4>
          <p>Geo-spatial verification (MRV) models for revenue wasteland afforestation, community pasture (Gauchar) restoration, and carbon credit allocation.</p>
        </div>
        <div class="grant-theme-card">
          <h4>🌊 Coastal Zone Regulation (CRZ) Compliance</h4>
          <p>Longitudinal satellite assessment of coastal revenue land erosion, mangrove buffers, and CRZ notification adherence in industrial ports.</p>
        </div>
      </div>
      
      <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.80rem; color:var(--text-dim);">
        <span>Grant Range: <strong>₹15,00,000 – ₹50,00,000</strong> per approved project</span>
        <span>Peer Review Committee: <strong>DoLR, MoRD & NITI Aayog Advisory Board</strong></span>
      </div>
    </div>

    <!-- SECTION 3: State Land Reform Pilot Tracker -->
    <div class="section-header">
      <div class="section-title-box">
        <h2>📍 State Land Reform Pilot Projects Live Tracker</h2>
        <p>Real-time telemetry tracking flagship digital land initiatives across Indian pilot jurisdictions.</p>
      </div>
    </div>

    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th>Initiative / Pilot Name</th>
            <th>Jurisdiction</th>
            <th>Nodal Department</th>
            <th>Key Deliverables</th>
            <th>Completion</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>SVAMITVA Scheme 2.0</strong>
              <div style="font-size:0.75rem; color:var(--text-dim);">Abadi Rural Drone Survey</div>
            </td>
            <td><span class="state-badge">National</span></td>
            <td>Survey of India & MoRD</td>
            <td>2,82,450 Villages Droned | 1.48 Cr Cards</td>
            <td>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono'; font-size:0.78rem;">91.2%</span>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width:91.2%;"></div></div>
              </div>
            </td>
            <td><span class="badge-status">Active</span></td>
          </tr>

          <tr>
            <td>
              <strong>DILRMP 2.0 (Modernization)</strong>
              <div style="font-size:0.75rem; color:var(--text-dim);">Digital RoR & SRO Integration</div>
            </td>
            <td><span class="state-badge">National</span></td>
            <td>DoLR, Government of India</td>
            <td>98.6% Cadastral Maps Digitized</td>
            <td>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono'; font-size:0.78rem;">98.6%</span>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width:98.6%;"></div></div>
              </div>
            </td>
            <td><span class="badge-status">Active</span></td>
          </tr>

          <tr>
            <td>
              <strong>Gujarat Jantri 2.0 Pilot</strong>
              <div style="font-size:0.75rem; color:var(--text-dim);">GIS Road-Width Spatial Valuation</div>
            </td>
            <td><span class="state-badge" style="background:rgba(16, 185, 129, 0.15); color:var(--green);">Gujarat Pilot</span></td>
            <td>Revenue Dept, Govt of Gujarat</td>
            <td>33 Districts, 252 Talukas Integrated</td>
            <td>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono'; font-size:0.78rem;">100%</span>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width:100%;"></div></div>
              </div>
            </td>
            <td><span class="badge-status">Live Pilot</span></td>
          </tr>

          <tr>
            <td>
              <strong>UP Bhulekh Real-Time Sync</strong>
              <div style="font-size:0.75rem; color:var(--text-dim);">16-Digit ULPIN & e-Khasra</div>
            </td>
            <td><span class="state-badge" style="background:rgba(56, 189, 248, 0.15); color:var(--cyan);">UP Demo</span></td>
            <td>UP Board of Revenue</td>
            <td>Bhu-Aadhaar Integration in 75 Districts</td>
            <td>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono'; font-size:0.78rem;">87.5%</span>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width:87.5%;"></div></div>
              </div>
            </td>
            <td><span class="badge-status">Demo Ready</span></td>
          </tr>

          <tr>
            <td>
              <strong>Maharashtra E-Chawdi & E-Hakk</strong>
              <div style="font-size:0.75rem; color:var(--text-dim);">Paperless Satbara Mutation</div>
            </td>
            <td><span class="state-badge" style="background:rgba(168, 85, 247, 0.15); color:var(--purple);">MH Demo</span></td>
            <td>Settlement Commissioner, MH</td>
            <td>Digital 7/12 & 8A with Aadhaar e-Sign</td>
            <td>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono'; font-size:0.78rem;">93.8%</span>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width:93.8%;"></div></div>
              </div>
            </td>
            <td><span class="badge-status">Demo Ready</span></td>
          </tr>

          <tr>
            <td>
              <strong>MP Saara Portal</strong>
              <div style="font-size:0.75rem; color:var(--text-dim);">Drone Crop Survey Verification</div>
            </td>
            <td><span class="state-badge">Madhya Pradesh</span></td>
            <td>MP Land Records HQ</td>
            <td>AI Crop Girdawari & Farmer Self-App</td>
            <td>
              <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-family:'JetBrains Mono'; font-size:0.78rem;">82.0%</span>
                <div class="progress-bar-wrap"><div class="progress-fill" style="width:82.0%;"></div></div>
              </div>
            </td>
            <td><span class="badge-status">Active</span></td>
          </tr>
        </tbody>
      </table>
    </div>

  </main>

  <!-- Challenge Submission Modal -->
  <div class="modal-backdrop" id="challengeModal">
    <div class="modal-dialog">
      <button class="modal-close" onclick="closeModal('challengeModal')">✕</button>
      <h3 style="font-size:1.2rem; margin-bottom:4px;" id="modalChallengeTitle">Submit Challenge Solution</h3>
      <p style="font-size:0.80rem; color:var(--text-dim); margin-bottom:20px;">DoLR National Innovation Pipeline • MoRD Problem Statement 26019</p>
      
      <form onsubmit="handleChallengeSubmit(event)">
        <div class="form-group">
          <label>Lead Applicant / Team Name *</label>
          <input type="text" class="form-control" placeholder="e.g., GeoCad Innovations Lab / IIT Bombay" required />
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Primary Contact Email *</label>
            <input type="email" class="form-control" placeholder="pi@institute.ac.in" required />
          </div>
          <div class="form-group">
            <label>Applicant Type *</label>
            <select class="form-control">
              <option>Academic Research Lab</option>
              <option>GovTech Startup (DPIIT registered)</option>
              <option>Independent Researcher</option>
              <option>University Student Consortium</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label>Solution Architecture & Methodology Abstract *</label>
          <textarea class="form-control" rows="4" placeholder="Summarize your approach, computer vision model or GIS data pipeline, accuracy benchmarks, and scalability..." required></textarea>
        </div>
        <div class="form-group">
          <label>Technical Repository / Proposal Link (GitHub, Google Drive, or PDF URL) *</label>
          <input type="url" class="form-control" placeholder="https://github.com/your-team/cadastral-ai" required />
        </div>
        <button type="submit" class="btn-action-primary" style="width:100%; justify-content:center; padding:12px; margin-top:8px;">
          Submit Challenge Entry
        </button>
      </form>
    </div>
  </div>

  <!-- Grant Application Modal -->
  <div class="modal-backdrop" id="grantModal">
    <div class="modal-dialog">
      <button class="modal-close" onclick="closeModal('grantModal')">✕</button>
      <h3 style="font-size:1.2rem; margin-bottom:4px;">DoLR Academic Research Grant Proposal</h3>
      <p style="font-size:0.80rem; color:var(--text-dim); margin-bottom:20px;">Department of Land Resources (MoRD) • Academic Fellowship 2026-27</p>
      
      <form onsubmit="handleGrantSubmit(event)">
        <div class="form-group">
          <label>Principal Investigator (PI) Full Name *</label>
          <input type="text" class="form-control" placeholder="Prof. / Dr. Full Name" required />
        </div>
        <div class="form-group">
          <label>Host Institution / University *</label>
          <input type="text" class="form-control" placeholder="e.g. National Law School / IIT / IIM / Central University" required />
        </div>
        <div class="form-row">
          <div class="form-group">
            <label>Priority Research Theme *</label>
            <select class="form-control">
              <option>Spatial Econometrics & Jantri Capture</option>
              <option>Tenancy Law Formalization & Yields</option>
              <option>Carbon Credit Agro-Forestry Cadastres</option>
              <option>CRZ & Coastal Cadastral Vulnerability</option>
              <option>Multi-State Digital Land Integration</option>
            </select>
          </div>
          <div class="form-group">
            <label>Requested Grant Budget (INR) *</label>
            <select class="form-control">
              <option>₹15,00,000 (12 Months Study)</option>
              <option>₹25,00,000 (18 Months Empirical Field Pilot)</option>
              <option>₹50,00,000 (24 Months Multi-State Consortium)</option>
            </select>
          </div>
        </div>
        <div class="form-group">
          <label>Executive Proposal Abstract & Policy Impact *</label>
          <textarea class="form-control" rows="4" placeholder="State hypothesis, research methodology, sample districts, and expected policy deliverables for DoLR..." required></textarea>
        </div>
        <button type="submit" class="btn-action-primary" style="width:100%; justify-content:center; padding:12px; margin-top:8px;">
          Submit Academic Proposal for Peer Review
        </button>
      </form>
    </div>
  </div>

  <!-- Toast Notice -->
  <div class="toast-notice" id="toastNotice">
    <span>✅</span>
    <span id="toastMsg">Action successfully completed</span>
  </div>

  <script>
    // ------------------------------------------------------------------------
    // Persona & State Synchronization (Req 17 & 10)
    // ------------------------------------------------------------------------
    document.addEventListener("DOMContentLoaded", () => {
      const savedPersona = localStorage.getItem("bhumi_persona") || "citizen";
      const savedState = localStorage.getItem("bhumi_state") || "gujarat";
      
      const pSel = document.getElementById("personaSelector");
      const sSel = document.getElementById("stateSelector");
      if (pSel) pSel.value = savedPersona;
      if (sSel) sSel.value = savedState;
    });

    function onPersonaChange(val) {
      localStorage.setItem("bhumi_persona", val);
      showToast(`Switched Role: ${val === 'citizen' ? 'Public Citizen' : (val === 'researcher' ? 'Academic Researcher' : 'DoLR Policy Official')}`);
    }

    function onStateChange(val) {
      localStorage.setItem("bhumi_state", val);
      showToast(`Selected Jurisdiction: ${val === 'gujarat' ? 'Gujarat (Active Pilot)' : (val === 'up' ? 'Uttar Pradesh (Demo)' : 'Maharashtra (Demo)')}`);
    }

    // ------------------------------------------------------------------------
    // Modal Helpers
    // ------------------------------------------------------------------------
    function openChallengeModal(title) {
      document.getElementById("modalChallengeTitle").textContent = `Submit Solution: ${title}`;
      document.getElementById("challengeModal").style.display = "flex";
    }

    function openGrantModal() {
      document.getElementById("grantModal").style.display = "flex";
    }

    function closeModal(id) {
      document.getElementById(id).style.display = "none";
    }

    function handleChallengeSubmit(e) {
      e.preventDefault();
      closeModal("challengeModal");
      const refId = "DoLR-CHAL-2026-" + Math.floor(1000 + Math.random() * 9000);
      showToast(`Challenge submission accepted! Registered under Docket ID: ${refId}`);
    }

    function handleGrantSubmit(e) {
      e.preventDefault();
      closeModal("grantModal");
      const grantId = "DoLR-FELLOW-2026-" + Math.floor(1000 + Math.random() * 9000);
      showToast(`Research proposal submitted! Queued for DoLR Advisory Peer Review ID: ${grantId}`);
    }

    function showToast(msg) {
      const t = document.getElementById("toastNotice");
      document.getElementById("toastMsg").textContent = msg;
      t.style.display = "flex";
      setTimeout(() => { t.style.display = "none"; }, 4500);
    }
  </script>

</body>
</html>
"""
