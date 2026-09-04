"""
Bhumi-Niti (भूमि-नीति): Innovation Hub & Research Sandbox View (Req 15 & Problem Statement 26019)
GIGW 3.0 Compliant National Innovation Portal | DoLR, Ministry of Rural Development
Authentic Indian Government Standards (MyGov Innovation / Smart India Hackathon / DoLR Sandbox)
"""

def render_innovation_html() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bhumi-Niti (भूमि-नीति) | National Land Governance Innovation Hub & Research Sandbox</title>
  <meta name="description" content="Bhumi-Niti Innovation Hub — DoLR Land Governance Hackathons, University Research Grants, and State Pilot Projects Tracker. Ministry of Rural Development, Government of India.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    /* ------------------------------------------------------------------------
       1. GovTech GIGW 3.0 Design Tokens & Color Palette
       ------------------------------------------------------------------------ */
    :root {
      --gov-blue-dark: #082136;
      --gov-blue-primary: #0B3C5D;
      --gov-blue-deep: #1E3A8A;
      --gov-blue-light: #EBF3FA;
      --gov-blue-border: #BFDBFE;
      --gov-saffron: #EA580C;
      --gov-saffron-light: #FFF7ED;
      --gov-saffron-border: #FED7AA;
      --gov-green: #15803D;
      --gov-green-light: #F0FDF4;
      --gov-green-border: #BBF7D0;
      --gov-red: #DC2626;
      --gov-red-light: #FEF2F2;
      --gov-purple: #6D28D9;
      --gov-purple-light: #EDE9FE;
      --gov-canvas: #F8FAFC;
      --gov-surface: #FFFFFF;
      --gov-surface-alt: #F1F5F9;
      --gov-border: #CBD5E1;
      --gov-border-subtle: #E2E8F0;
      --gov-text-primary: #0F172A;
      --gov-text-secondary: #334155;
      --gov-text-muted: #64748B;
      --font-gov: 'Noto Sans', 'Inter', -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { font-size: 14px; }
    body {
      background: var(--gov-canvas);
      color: var(--gov-text-primary);
      font-family: var(--font-gov);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* Scrollbars */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: var(--gov-canvas); }
    ::-webkit-scrollbar-thumb { background: var(--gov-border); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--gov-blue-primary); }

    /* ------------------------------------------------------------------------
       2. Tier 1: GIGW 3.0 Accessibility & Utility Bar (Top 34px)
       ------------------------------------------------------------------------ */
    .gov-utility-bar {
      height: 34px;
      background: var(--gov-blue-dark);
      color: #E2E8F0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 20px;
      font-size: 0.76rem;
      z-index: 3000;
      flex-shrink: 0;
    }
    .gov-util-left, .gov-util-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .util-link {
      color: #CBD5E1;
      text-decoration: none;
      font-size: 0.74rem;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: color 0.15s;
    }
    .util-link:hover, .util-link:focus {
      color: #FFFFFF;
      text-decoration: underline;
    }
    .util-sep {
      color: rgba(255, 255, 255, 0.25);
      font-size: 0.72rem;
    }
    .ist-clock-pill {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      padding: 2px 8px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: #F8FAFC;
    }
    .util-selector-item {
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .util-selector-item label {
      font-size: 0.70rem;
      color: #94A3B8;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .util-select {
      background: #0D2D49;
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 0.74rem;
      font-weight: 600;
      outline: none;
      cursor: pointer;
    }
    .util-select option {
      background: #082136;
      color: #FFFFFF;
    }
    .font-controls {
      display: inline-flex;
      align-items: center;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 4px;
      overflow: hidden;
    }
    .font-btn {
      background: transparent;
      border: none;
      color: #E2E8F0;
      padding: 2px 7px;
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      border-right: 1px solid rgba(255, 255, 255, 0.15);
      transition: all 0.15s;
    }
    .font-btn:last-child { border-right: none; }
    .font-btn:hover, .font-btn.active {
      background: var(--gov-blue-primary);
      color: #FFFFFF;
    }
    .contrast-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #E2E8F0;
      border-radius: 4px;
      padding: 2px 8px;
      font-size: 0.72rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s;
    }
    .contrast-btn:hover {
      background: rgba(255, 255, 255, 0.18);
      color: #FFFFFF;
    }

    /* ------------------------------------------------------------------------
       3. Tier 2: Institutional Identity Masthead (White Surface)
       ------------------------------------------------------------------------ */
    .gov-masthead {
      background: var(--gov-surface);
      border-bottom: 2px solid var(--gov-border);
      padding: 8px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 2000;
      flex-shrink: 0;
      gap: 16px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    }
    .masthead-left {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-shrink: 0;
    }
    .emblem-container {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .ministry-title-block {
      display: flex;
      flex-direction: column;
    }
    .min-devanagari {
      font-size: 0.78rem;
      font-weight: 700;
      color: #1E293B;
      letter-spacing: -0.01em;
      line-height: 1.25;
    }
    .min-english {
      font-size: 0.72rem;
      font-weight: 600;
      color: #475569;
      line-height: 1.25;
    }
    .brand-title-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 2px;
    }
    .brand-main {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--gov-blue-primary);
      letter-spacing: -0.02em;
    }
    .brand-hindi {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--gov-saffron);
    }
    .brand-tag-gov {
      font-size: 0.62rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      background: var(--gov-saffron-light);
      color: var(--gov-saffron);
      border: 1px solid var(--gov-saffron-border);
      padding: 1px 6px;
      border-radius: 4px;
    }
    .brand-subline {
      font-size: 0.68rem;
      color: var(--gov-text-muted);
      font-weight: 500;
      line-height: 1.2;
    }

    /* Right Navigation Tabs & Portal Status */
    .masthead-right {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-shrink: 0;
    }
    .gov-nav-tabs {
      display: flex;
      align-items: center;
      gap: 4px;
      background: var(--gov-surface-alt);
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--gov-border-subtle);
    }
    .gov-tab {
      padding: 6px 13px;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 600;
      text-decoration: none;
      color: var(--gov-text-secondary);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      position: relative;
    }
    .gov-tab:hover {
      color: var(--gov-blue-primary);
      background: rgba(11, 60, 93, 0.06);
    }
    .gov-tab.active {
      background: var(--gov-blue-primary);
      color: #FFFFFF;
      box-shadow: 0 2px 6px rgba(11, 60, 93, 0.25);
      border-bottom: 3px solid var(--gov-saffron);
    }

    .live-gov-badge {
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--gov-saffron-light);
      border: 1px solid var(--gov-saffron-border);
      color: var(--gov-saffron);
      font-size: 0.74rem;
      font-weight: 700;
      padding: 5px 10px;
      border-radius: 6px;
      white-space: nowrap;
    }
    .dot-live {
      width: 8px;
      height: 8px;
      background: var(--gov-saffron);
      border-radius: 50%;
      box-shadow: 0 0 8px rgba(234, 88, 12, 0.6);
      animation: pulse-dot 2s infinite;
    }
    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.6; transform: scale(1.15); }
    }

    /* ------------------------------------------------------------------------
       4. Sub-Header: Institutional Banner & Program Metrics Bar
       ------------------------------------------------------------------------ */
    .inno-hero-banner {
      background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
      border-bottom: 1.5px solid var(--gov-border);
      padding: 24px 24px 18px;
    }
    .inno-hero-inner {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .inno-hero-title-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 14px;
    }
    .inno-hero-titles h1 {
      font-size: 1.50rem;
      font-weight: 800;
      color: var(--gov-blue-primary);
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: -0.01em;
    }
    .inno-hero-titles p {
      font-size: 0.84rem;
      color: var(--gov-text-secondary);
      margin-top: 4px;
      max-width: 880px;
      line-height: 1.5;
    }
    .badge-challenge-cohort {
      background: var(--gov-saffron-light);
      border: 1px solid var(--gov-saffron-border);
      color: var(--gov-saffron);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.70rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Program Metrics Bar (4 Compact Cards) */
    .inno-kpi-bar {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }
    @media (max-width: 900px) {
      .inno-kpi-bar { grid-template-columns: repeat(2, 1fr); }
    }
    .inno-kpi-card {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 8px;
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
      border-left: 3.5px solid var(--gov-blue-primary);
    }
    .inno-kpi-card:nth-child(1) { border-left-color: var(--gov-saffron); }
    .inno-kpi-card:nth-child(2) { border-left-color: var(--gov-green); }
    .inno-kpi-card:nth-child(3) { border-left-color: var(--gov-blue-primary); }
    .inno-kpi-card:nth-child(4) { border-left-color: var(--gov-purple); }

    .inno-kpi-icon {
      width: 40px;
      height: 40px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      background: var(--gov-surface-alt);
      flex-shrink: 0;
    }
    .inno-kpi-text {
      display: flex;
      flex-direction: column;
    }
    .inno-kpi-val {
      font-family: var(--font-mono);
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--gov-text-primary);
      line-height: 1.1;
    }
    .inno-kpi-lbl {
      font-size: 0.72rem;
      color: var(--gov-text-muted);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* ------------------------------------------------------------------------
       5. Tabbed Interface (Challenges, Research Grants, Pilot Tracker)
       ------------------------------------------------------------------------ */
    .inno-main-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 24px 24px 60px;
      width: 100%;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    /* Tab Navigation Header */
    .inno-tab-nav {
      display: flex;
      align-items: center;
      gap: 4px;
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 8px;
      padding: 4px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    }
    .inno-tab-btn {
      padding: 9px 18px;
      border: none;
      background: transparent;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--gov-text-secondary);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.15s ease;
    }
    .inno-tab-btn:hover {
      background: var(--gov-surface-alt);
      color: var(--gov-blue-primary);
    }
    .inno-tab-btn.active {
      background: var(--gov-blue-primary);
      color: #FFFFFF;
      box-shadow: 0 2px 6px rgba(11, 60, 93, 0.2);
    }

    /* Tab Content Panes */
    .tab-content-pane {
      display: none;
      flex-direction: column;
      gap: 20px;
      animation: fadeInPane 0.2s ease-out;
    }
    .tab-content-pane.active {
      display: flex;
    }
    @keyframes fadeInPane {
      from { opacity: 0; transform: translateY(3px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ------------------------------------------------------------------------
       Tab A: Active Innovation Challenges & Hackathons
       ------------------------------------------------------------------------ */
    .challenges-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
    }
    .challenge-card {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 10px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
      transition: all 0.2s;
      border-top: 4px solid var(--gov-blue-primary);
    }
    .challenge-card:hover {
      border-color: var(--gov-blue-primary);
      box-shadow: 0 8px 20px rgba(11, 60, 93, 0.09);
      transform: translateY(-2px);
    }
    .challenge-card-top {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .challenge-badge-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }
    .badge-dept {
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--gov-blue-light);
      color: var(--gov-blue-primary);
      border: 1px solid var(--gov-blue-border);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .badge-eligibility {
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--gov-green-light);
      color: var(--gov-green);
      border: 1px solid var(--gov-green-border);
    }
    .challenge-title {
      font-size: 1.10rem;
      font-weight: 800;
      color: var(--gov-blue-dark);
      line-height: 1.35;
      letter-spacing: -0.01em;
    }
    .challenge-desc {
      font-size: 0.82rem;
      color: var(--gov-text-secondary);
      line-height: 1.55;
    }

    .challenge-meta-box {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      background: var(--gov-surface-alt);
      border: 1px solid var(--gov-border-subtle);
      border-radius: 8px;
      padding: 10px 12px;
    }
    .meta-stat-item {
      display: flex;
      flex-direction: column;
    }
    .meta-stat-val {
      font-family: var(--font-mono);
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--gov-saffron);
    }
    .meta-stat-lbl {
      font-size: 0.68rem;
      color: var(--gov-text-muted);
      text-transform: uppercase;
      font-weight: 600;
    }

    .btn-submit-solution {
      background: var(--gov-blue-primary);
      color: #FFFFFF;
      border: none;
      padding: 9px 16px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.15s;
      width: 100%;
    }
    .btn-submit-solution:hover {
      background: var(--gov-saffron);
      box-shadow: 0 2px 8px rgba(234, 88, 12, 0.25);
    }

    /* ------------------------------------------------------------------------
       Tab B: Research Grants & Academic Fellowships
       ------------------------------------------------------------------------ */
    .grant-overview-card {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 10px;
      padding: 24px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
      display: flex;
      flex-direction: column;
      gap: 18px;
      border-left: 4px solid var(--gov-green);
    }
    .grant-header-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 14px;
    }
    .grant-header-text h2 {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--gov-blue-dark);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .grant-header-text p {
      font-size: 0.84rem;
      color: var(--gov-text-secondary);
      margin-top: 4px;
      max-width: 820px;
      line-height: 1.5;
    }
    .grant-actions-row {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .btn-download-guidelines {
      background: #FFFFFF;
      border: 1.5px solid var(--gov-blue-primary);
      color: var(--gov-blue-primary);
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.80rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .btn-download-guidelines:hover {
      background: var(--gov-blue-light);
    }
    .btn-apply-grant {
      background: var(--gov-green);
      color: #FFFFFF;
      border: none;
      padding: 8px 18px;
      border-radius: 6px;
      font-size: 0.80rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .btn-apply-grant:hover {
      background: #166534;
    }

    .grant-themes-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
    }
    .grant-theme-box {
      background: var(--gov-surface-alt);
      border: 1px solid var(--gov-border-subtle);
      border-radius: 8px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .grant-theme-box h4 {
      font-size: 0.90rem;
      font-weight: 700;
      color: var(--gov-blue-primary);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .grant-theme-box p {
      font-size: 0.78rem;
      color: var(--gov-text-secondary);
      line-height: 1.5;
    }

    .grant-footer-telemetry {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      font-size: 0.76rem;
      color: var(--gov-text-muted);
      border-top: 1px solid var(--gov-border-subtle);
      padding-top: 12px;
    }

    /* ------------------------------------------------------------------------
       Tab C: State Pilot Projects Tracker
       ------------------------------------------------------------------------ */
    .pilot-table-container {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 10px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
      overflow-x: auto;
    }
    .pilot-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.82rem;
      text-align: left;
    }
    .pilot-table th {
      background: var(--gov-surface-alt);
      color: var(--gov-text-primary);
      padding: 12px 16px;
      font-weight: 700;
      border-bottom: 2px solid var(--gov-border);
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .pilot-table td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--gov-border-subtle);
      color: var(--gov-text-secondary);
    }
    .pilot-table tr:last-child td { border-bottom: none; }
    .pilot-table tr:hover td { background: var(--gov-blue-light); }

    .district-tag {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: var(--gov-surface-alt);
      border: 1px solid var(--gov-border);
      border-radius: 4px;
      padding: 2px 7px;
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--gov-text-primary);
    }
    .status-pill {
      font-size: 0.70rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 12px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      display: inline-block;
    }
    .status-testing {
      background: #FEF3C7;
      color: #B45309;
      border: 1px solid #FDE68A;
    }
    .status-eval {
      background: var(--gov-blue-light);
      color: var(--gov-blue-primary);
      border: 1px solid var(--gov-blue-border);
    }
    .status-scaling {
      background: var(--gov-green-light);
      color: var(--gov-green);
      border: 1px solid var(--gov-green-border);
    }

    .progress-bar-wrap {
      width: 110px;
      height: 6px;
      background: #E2E8F0;
      border-radius: 3px;
      overflow: hidden;
      margin-top: 4px;
    }
    .progress-fill {
      height: 100%;
      background: var(--gov-green);
      border-radius: 3px;
    }

    /* ------------------------------------------------------------------------
       6. Modals & Notifications
       ------------------------------------------------------------------------ */
    .inno-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(4px);
      z-index: 9999;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .inno-modal-content {
      background: #FFFFFF;
      border-radius: 10px;
      max-width: 620px;
      width: 100%;
      padding: 26px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
      border-top: 4px solid var(--gov-blue-primary);
      max-height: 90vh;
      overflow-y: auto;
    }
    .inno-modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }
    .inno-modal-title {
      font-size: 1.10rem;
      font-weight: 800;
      color: var(--gov-blue-dark);
    }
    .inno-modal-close {
      background: transparent;
      border: none;
      font-size: 1.2rem;
      cursor: pointer;
      color: var(--gov-text-muted);
    }

    .form-group {
      margin-bottom: 14px;
    }
    .form-group label {
      display: block;
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--gov-text-secondary);
      margin-bottom: 4px;
    }
    .form-control {
      width: 100%;
      background: var(--gov-surface-alt);
      border: 1.5px solid var(--gov-border);
      border-radius: 6px;
      padding: 8px 10px;
      font-size: 0.82rem;
      font-family: inherit;
      color: var(--gov-text-primary);
      outline: none;
    }
    .form-control:focus {
      border-color: var(--gov-blue-primary);
      background: #FFFFFF;
    }
    .form-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }

    /* Toast Notification */
    .toast-notice {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--gov-blue-dark);
      border: 1.5px solid var(--gov-saffron);
      border-radius: 8px;
      padding: 12px 18px;
      color: #FFFFFF;
      font-size: 0.82rem;
      display: none;
      align-items: center;
      gap: 10px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      z-index: 10000;
    }

    /* ------------------------------------------------------------------------
       7. GIGW 3.0 Mandatory Compliance Footer
       ------------------------------------------------------------------------ */
    .gov-footer {
      height: 44px;
      background: var(--gov-blue-dark);
      color: #CBD5E1;
      border-top: 2px solid var(--gov-saffron);
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0 24px;
      font-size: 0.72rem;
      z-index: 2000;
      flex-shrink: 0;
      margin-top: auto;
    }
    .footer-left-audit {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .footer-sync-audit {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .sync-dot {
      width: 7px;
      height: 7px;
      background: #22C55E;
      border-radius: 50%;
      box-shadow: 0 0 6px #22C55E;
    }
    .footer-disclaimer-btn {
      color: #94A3B8;
      cursor: pointer;
      text-decoration: underline;
      font-size: 0.70rem;
    }
    .footer-disclaimer-btn:hover { color: #FFFFFF; }
    .footer-right-credits {
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.70rem;
      color: #94A3B8;
    }
    .footer-gigw-badge {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 1px 6px;
      border-radius: 3px;
      color: #FFFFFF;
      font-weight: 700;
      letter-spacing: 0.04em;
    }

    /* High Contrast Mode */
    body.gov-high-contrast {
      --gov-canvas: #090D16;
      --gov-surface: #111A2E;
      --gov-surface-alt: #16223B;
      --gov-border: #334155;
      --gov-border-subtle: #1E293B;
      --gov-text-primary: #FFFFFF;
      --gov-text-secondary: #E2E8F0;
      --gov-text-muted: #94A3B8;
      --gov-blue-light: #1E293B;
    }
    body.gov-high-contrast .gov-masthead {
      background: #0B1324;
      border-bottom-color: #334155;
    }
    body.gov-high-contrast .inno-hero-banner {
      background: #0E1626;
      border-bottom-color: #334155;
    }
    body.gov-high-contrast .inno-hero-titles h1 { color: #38BDF8; }
    body.gov-high-contrast .challenge-card,
    body.gov-high-contrast .grant-overview-card,
    body.gov-high-contrast .pilot-table-container,
    body.gov-high-contrast .inno-modal-content {
      background: #111A2E;
      color: #FFFFFF;
      border-color: #334155;
    }
    body.gov-high-contrast .challenge-title { color: #38BDF8; }
    body.gov-high-contrast .inno-kpi-card { background: #111A2E; border-color: #334155; }
    body.gov-high-contrast .inno-kpi-val { color: #FFFFFF; }
  </style>
</head>
<body>

  <!-- ======================================================================
       TIER 1: GIGW 3.0 ACCESSIBILITY & UTILITY BAR (TOP 34px)
       ====================================================================== -->
  <aside class="gov-utility-bar" aria-label="Accessibility and Utility Controls">
    <div class="gov-util-left">
      <a href="#innoMainContent" class="util-link" accesskey="s">Skip to Main Content</a>
      <span class="util-sep">|</span>
      <a href="javascript:void(0)" class="util-link" onclick="triggerScreenReaderAlert()" accesskey="r">Screen Reader Access</a>
      <span class="util-sep">|</span>
      <span class="ist-clock-pill" title="Indian Standard Time (IST) Synchronized Clock">
        <span>🕒</span>
        <span id="istClock">Loading IST...</span>
      </span>
    </div>

    <div class="gov-util-right">
      <!-- Role Switcher & RBAC (Req 17) -->
      <div class="util-selector-item">
        <label for="personaSelector">Role:</label>
        <select id="personaSelector" class="util-select" onchange="onPersonaChange(this.value)" aria-label="Persona Switcher">
          <option value="citizen">👤 Public Citizen</option>
          <option value="researcher">🔬 Academic Researcher</option>
          <option value="official">🏛️ DoLR Policy Official</option>
        </select>
      </div>

      <span class="util-sep">|</span>

      <!-- National State Selector (Req 7 & 10) -->
      <div class="util-selector-item">
        <label for="stateSelector">Jurisdiction:</label>
        <select id="stateSelector" class="util-select" onchange="onStateChange(this.value)" aria-label="National State Jurisdiction Selector">
          <option value="gujarat">Gujarat (Active Pilot)</option>
          <option value="up">Uttar Pradesh (Demo)</option>
          <option value="maharashtra">Maharashtra (Demo)</option>
        </select>
      </div>

      <span class="util-sep">|</span>

      <!-- Font Size Scalers [ A- | A | A+ ] -->
      <div class="font-controls" role="group" aria-label="Text size controls">
        <button class="font-btn" onclick="adjustFontSize(-1)" title="Decrease font size">A-</button>
        <button class="font-btn active" onclick="adjustFontSize(0)" title="Default font size">A</button>
        <button class="font-btn" onclick="adjustFontSize(1)" title="Increase font size">A+</button>
      </div>

      <span class="util-sep">|</span>

      <!-- Contrast Toggle -->
      <button class="contrast-btn" id="contrastToggleBtn" onclick="toggleContrast()" title="Toggle High Contrast Mode">
        <span>◑</span>
        <span id="contrastText">Contrast</span>
      </button>

      <span class="util-sep">|</span>

      <!-- Language Selector -->
      <select class="util-select" id="langSelector" onchange="onLangChange(this.value)" aria-label="Language Selector">
        <option value="en">English</option>
        <option value="hi">हिन्दी</option>
        <option value="gu">ગુજરાતી</option>
      </select>
    </div>
  </aside>

  <!-- ======================================================================
       TIER 2: INSTITUTIONAL IDENTITY MASTHEAD (WHITE SURFACE)
       ====================================================================== -->
  <header class="gov-masthead" role="banner">
    <!-- Left Lockup: Emblem of India & Ministry Bilingual Identity -->
    <div class="masthead-left">
      <div class="emblem-container" title="State Emblem of India">
        <svg viewBox="0 0 100 135" width="40" height="54" aria-hidden="true">
          <!-- Stylized Authentic Representation of Ashoka Lion Capital -->
          <path d="M50 8 C45 8 41 12 41 17 C41 20 43 23 45 24 C40 26 36 30 36 35 C36 38 38 41 40 43 C35 45 32 49 32 54 C32 60 37 65 43 66 C40 68 38 72 38 76 C38 82 43 86 50 87 C57 86 62 82 62 76 C62 72 60 68 57 66 C63 65 68 60 68 54 C68 49 65 45 60 43 C62 41 64 38 64 35 C64 30 60 26 55 24 C57 23 59 20 59 17 C59 12 55 8 50 8 Z" fill="#0B3C5D"/>
          <!-- Ashoka Chakra -->
          <circle cx="50" cy="98" r="9" fill="none" stroke="#0B3C5D" stroke-width="2"/>
          <circle cx="50" cy="98" r="2" fill="#0B3C5D"/>
          <line x1="50" y1="89" x2="50" y2="107" stroke="#0B3C5D" stroke-width="1"/>
          <line x1="41" y1="98" x2="59" y2="98" stroke="#0B3C5D" stroke-width="1"/>
          <line x1="43.6" y1="91.6" x2="56.4" y2="104.4" stroke="#0B3C5D" stroke-width="1"/>
          <line x1="56.4" y1="91.6" x2="43.6" y2="104.4" stroke="#0B3C5D" stroke-width="1"/>
          <!-- Base Platform -->
          <path d="M28 110 L72 110 L68 116 L32 116 Z" fill="#0B3C5D"/>
          <rect x="22" y="118" width="56" height="3" rx="1.5" fill="#EA580C"/>
          <text x="50" y="130" text-anchor="middle" font-size="8" font-family="'Noto Sans', sans-serif" font-weight="800" fill="#0B3C5D">सत्यमेव जयते</text>
        </svg>
      </div>

      <div class="ministry-title-block">
        <div class="min-devanagari">ग्रामीण विकास मंत्रालय, भूमि संसाधन विभाग</div>
        <div class="min-english">Ministry of Rural Development, Department of Land Resources</div>
        <div class="brand-title-wrap">
          <span class="brand-main">Bhumi-Niti</span>
          <span class="brand-hindi">(भूमि-नीति)</span>
          <span class="brand-tag-gov">Innovation Hub</span>
        </div>
        <div class="brand-subline">National Digital Platform for Evidence-Based Land Governance</div>
      </div>
    </div>

    <!-- Right Navigation Tabs & Status -->
    <div class="masthead-right">
      <nav class="gov-nav-tabs" role="navigation" aria-label="Portal Navigation">
        <a href="/" class="gov-tab">
          <span>🗺️</span>
          <span>Spatial GIS Platform</span>
        </a>
        <a href="/knowledge-base" class="gov-tab">
          <span>📚</span>
          <span>Policy Repository</span>
        </a>
        <a href="/innovation" class="gov-tab active" aria-current="page">
          <span>💡</span>
          <span>Innovation Hub</span>
        </a>
      </nav>

      <div class="live-gov-badge">
        <span class="dot-live"></span>
        <span>Problem Statement 26019 Active</span>
      </div>
    </div>
  </header>

  <!-- ======================================================================
       SUB-HEADER: INSTITUTIONAL BANNER & PROGRAM METRICS BAR
       ====================================================================== -->
  <section class="inno-hero-banner">
    <div class="inno-hero-inner">
      <div class="inno-hero-title-row">
        <div class="inno-hero-titles">
          <h1>
            <span>National Land Governance Innovation Hub & Applied Research Sandbox</span>
            <span class="badge-challenge-cohort">Cohort 2026-27</span>
          </h1>
          <p>
            Fostering academic collaboration, pilot project funding, and algorithmic solutions for land administration reforms under Department of Land Resources (MoRD). Connecting universities, think tanks, startups, and district administrations.
          </p>
        </div>
      </div>

      <!-- 4 Program Metric KPI Cards -->
      <div class="inno-kpi-bar">
        <div class="inno-kpi-card">
          <div class="inno-kpi-icon">🎯</div>
          <div class="inno-kpi-text">
            <div class="inno-kpi-val">4 Active</div>
            <div class="inno-kpi-lbl">National Challenges</div>
          </div>
        </div>

        <div class="inno-kpi-card">
          <div class="inno-kpi-icon">💰</div>
          <div class="inno-kpi-text">
            <div class="inno-kpi-val">₹2.40 Cr</div>
            <div class="inno-kpi-lbl">Sanctioned Grants</div>
          </div>
        </div>

        <div class="inno-kpi-card">
          <div class="inno-kpi-icon">🏛️</div>
          <div class="inno-kpi-text">
            <div class="inno-kpi-val">12 Partner</div>
            <div class="inno-kpi-lbl">Universities & IITs</div>
          </div>
        </div>

        <div class="inno-kpi-card">
          <div class="inno-kpi-icon">🚀</div>
          <div class="inno-kpi-text">
            <div class="inno-kpi-val">7 Pilots</div>
            <div class="inno-kpi-lbl">Deployed in Districts</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================================
       MAIN TABBED INTERFACE CONTAINER
       ====================================================================== -->
  <main class="inno-main-container" id="innoMainContent">
    
    <!-- Tab Controls Bar -->
    <nav class="inno-tab-nav" role="tablist" aria-label="Innovation Hub Modules">
      <button class="inno-tab-btn active" id="tabBtnChallenges" role="tab" aria-selected="true" aria-controls="paneChallenges" onclick="switchTab('challenges')">
        <span>🏆</span>
        <span>Active Innovation Challenges & Hackathons</span>
      </button>
      <button class="inno-tab-btn" id="tabBtnGrants" role="tab" aria-selected="false" aria-controls="paneGrants" onclick="switchTab('grants')">
        <span>🎓</span>
        <span>Research Grants & Academic Fellowships</span>
      </button>
      <button class="inno-tab-btn" id="tabBtnPilots" role="tab" aria-selected="false" aria-controls="panePilots" onclick="switchTab('pilots')">
        <span>📍</span>
        <span>State Pilot Projects Tracker</span>
      </button>
    </nav>

    <!-- --------------------------------------------------------------------
         TAB PANE A: ACTIVE INNOVATION CHALLENGES & HACKATHONS
         -------------------------------------------------------------------- -->
    <section class="tab-content-pane active" id="paneChallenges" role="tabpanel" aria-labelledby="tabBtnChallenges">
      <div class="challenges-grid">

        <!-- Challenge 1 -->
        <article class="challenge-card">
          <div class="challenge-card-top">
            <div class="challenge-badge-row">
              <span class="badge-dept">DoLR / BISAG-N</span>
              <span class="badge-eligibility">Universities & Startups</span>
            </div>
            <h2 class="challenge-title">Automated Cadastral Map Alignment using AI & High-Res Drone Imagery</h2>
            <p class="challenge-desc">
              Develop deep learning computer vision pipelines to auto-rectify, edge-detect, and vector-align legacy hand-drawn cadastral village sheets (Village Form 7/12 & Tipan) with sub-10cm drone orthophoto mosaics under SVAMITVA 2.0.
            </p>
          </div>
          <div>
            <div class="challenge-meta-box">
              <div class="meta-stat-item">
                <span class="meta-stat-val">₹35,00,000</span>
                <span class="meta-stat-lbl">Grant Value / Prize</span>
              </div>
              <div class="meta-stat-item">
                <span class="meta-stat-val">30 Nov 2026</span>
                <span class="meta-stat-lbl">Submission Deadline</span>
              </div>
            </div>
            <button class="btn-submit-solution" onclick="openChallengeModal('Automated Cadastral Map Alignment using AI & High-Res Drone Imagery', 'DoLR / BISAG-N')" style="margin-top:14px;">
              <span>🚀</span>
              <span>Submit Solution / Register Team</span>
            </button>
          </div>
        </article>

        <!-- Challenge 2 -->
        <article class="challenge-card">
          <div class="challenge-card-top">
            <div class="challenge-badge-row">
              <span class="badge-dept">Urban Development / CEPT</span>
              <span class="badge-eligibility">Academic Labs & Think Tanks</span>
            </div>
            <h2 class="challenge-title">Predictive Peri-Urban Sprawl & Agricultural Land Transition Modeling</h2>
            <p class="challenge-desc">
              Longitudinal satellite LULC analysis combined with road expansion vectors to predict speculative non-agricultural (NA) conversion hotspots, ribbon development along corridors, and agricultural ceiling boundary fragmentation.
            </p>
          </div>
          <div>
            <div class="challenge-meta-box">
              <div class="meta-stat-item">
                <span class="meta-stat-val">₹25,00,000</span>
                <span class="meta-stat-lbl">Grant Value / Prize</span>
              </div>
              <div class="meta-stat-item">
                <span class="meta-stat-val">15 Dec 2026</span>
                <span class="meta-stat-lbl">Submission Deadline</span>
              </div>
            </div>
            <button class="btn-submit-solution" onclick="openChallengeModal('Predictive Peri-Urban Sprawl & Agricultural Land Transition Modeling', 'Urban Development / CEPT')" style="margin-top:14px;">
              <span>🚀</span>
              <span>Submit Solution / Register Team</span>
            </button>
          </div>
        </article>

        <!-- Challenge 3 -->
        <article class="challenge-card">
          <div class="challenge-card-top">
            <div class="challenge-badge-row">
              <span class="badge-dept">Gujarat Revenue Dept / NIC</span>
              <span class="badge-eligibility">GovTech Consortia</span>
            </div>
            <h2 class="challenge-title">Smart Contract-based RTS Land Record Mutation System</h2>
            <p class="challenge-desc">
              Permissioned distributed ledger architecture automating Right to Service (RTS) timeline enforcement for inheritance mutations, registered sale deed endorsements, and automated 135-D notice circulation to khatedars.
            </p>
          </div>
          <div>
            <div class="challenge-meta-box">
              <div class="meta-stat-item">
                <span class="meta-stat-val">₹30,00,000</span>
                <span class="meta-stat-lbl">Grant Value / Prize</span>
              </div>
              <div class="meta-stat-item">
                <span class="meta-stat-val">15 Jan 2027</span>
                <span class="meta-stat-lbl">Submission Deadline</span>
              </div>
            </div>
            <button class="btn-submit-solution" onclick="openChallengeModal('Smart Contract-based RTS Land Record Mutation System', 'Gujarat Revenue Dept / NIC')" style="margin-top:14px;">
              <span>🚀</span>
              <span>Submit Solution / Register Team</span>
            </button>
          </div>
        </article>

        <!-- Challenge 4 -->
        <article class="challenge-card">
          <div class="challenge-card-top">
            <div class="challenge-badge-row">
              <span class="badge-dept">Survey of India / DoLR</span>
              <span class="badge-eligibility">Robotics & Drone Startups</span>
            </div>
            <h2 class="challenge-title">Drone-Based 3D Land Titling & Abadi Rooftop Delineation (SVAMITVA 2.0)</h2>
            <p class="challenge-desc">
              Automated point-cloud classification and mesh generation for high-density village abadi lands, delivering sub-5cm vertical accuracy, property card linking, and 3D boundary dispute containment.
            </p>
          </div>
          <div>
            <div class="challenge-meta-box">
              <div class="meta-stat-item">
                <span class="meta-stat-val">₹40,00,000</span>
                <span class="meta-stat-lbl">Grant Value / Prize</span>
              </div>
              <div class="meta-stat-item">
                <span class="meta-stat-val">28 Feb 2027</span>
                <span class="meta-stat-lbl">Submission Deadline</span>
              </div>
            </div>
            <button class="btn-submit-solution" onclick="openChallengeModal('Drone-Based 3D Land Titling & Abadi Rooftop Delineation', 'Survey of India / DoLR')" style="margin-top:14px;">
              <span>🚀</span>
              <span>Submit Solution / Register Team</span>
            </button>
          </div>
        </article>

      </div>
    </section>

    <!-- --------------------------------------------------------------------
         TAB PANE B: RESEARCH GRANTS & ACADEMIC FELLOWSHIPS
         -------------------------------------------------------------------- -->
    <section class="tab-content-pane" id="paneGrants" role="tabpanel" aria-labelledby="tabBtnGrants">
      <div class="grant-overview-card">
        <div class="grant-header-row">
          <div class="grant-header-text">
            <h2>🎓 Land Governance Research Grant Scheme (LGRGS) 2026-27</h2>
            <p>
              Direct institutional grant financing instituted by the Department of Land Resources (MoRD) for Indian Central Universities, IITs, IIMs, and National Law Universities to produce grounded, empirical statutory policy research.
            </p>
          </div>
          <div class="grant-actions-row">
            <button class="btn-download-guidelines" onclick="triggerDownloadGuidelines()">
              <span>📥</span>
              <span>Download Guidelines (PDF)</span>
            </button>
            <button class="btn-apply-grant" onclick="openGrantModal()">
              <span>📝</span>
              <span>Submit Grant Proposal</span>
            </button>
          </div>
        </div>

        <div class="grant-themes-grid">
          <div class="grant-theme-box">
            <h4>📊 Spatial Econometrics & Jantri Capture</h4>
            <p>Empirical evaluation of periodic Jantri revisions on municipal infrastructure buoyancy, stamp duty incidence, and affordable housing land reservations in peri-urban belts.</p>
          </div>
          <div class="grant-theme-box">
            <h4>🌾 Tenancy Formalization & Agricultural Yield</h4>
            <p>Assessing registered agricultural leaseholds under the Model Land Leasing Act versus informal oral tenancies in Saurashtra and Central Gujarat agro-climatic zones.</p>
          </div>
          <div class="grant-theme-box">
            <h4>🌲 Carbon Credit Agro-Forestry Cadastres</h4>
            <p>Geo-spatial verification (MRV) models for revenue wasteland afforestation, community grazing land (Gauchar) preservation, and institutional carbon offset allocations.</p>
          </div>
          <div class="grant-theme-box">
            <h4>🌊 Coastal Zone Regulation (CRZ) Compliance</h4>
            <p>Longitudinal satellite assessment of coastal revenue erosion, tidal inundation buffers, and CRZ notification enforcement around major industrial port clusters.</p>
          </div>
        </div>

        <div class="grant-footer-telemetry">
          <span>Grant Funding Range: <strong>₹15,00,000 to ₹50,00,000</strong> per sanctioned project</span>
          <span>Project Tenure: <strong>12 to 24 Months</strong> with empirical field validation</span>
          <span>Advisory Review Board: <strong>DoLR, MoRD & NITI Aayog Expert Council</strong></span>
        </div>
      </div>
    </section>

    <!-- --------------------------------------------------------------------
         TAB PANE C: STATE PILOT PROJECTS TRACKER
         -------------------------------------------------------------------- -->
    <section class="tab-content-pane" id="panePilots" role="tabpanel" aria-labelledby="tabBtnPilots">
      <div class="pilot-table-container">
        <table class="pilot-table">
          <thead>
            <tr>
              <th>District / Location</th>
              <th>Initiative / Pilot Title</th>
              <th>Implementing Institution</th>
              <th>Focus Area & Deliverables</th>
              <th>Completion Progress</th>
              <th>Current Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <span class="district-tag">📍 Sanand, Ahmedabad</span>
              </td>
              <td>
                <strong>Automated Industrial NA Spatial Fast-Track</strong>
                <div style="font-size:0.72rem; color:var(--gov-text-muted);">GLRC Section 65-B Integrated Workflow</div>
              </td>
              <td><strong>CEPT University</strong></td>
              <td>Digital buffer clearance check against irrigation canals and TP road master plan.</td>
              <td>
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="font-family:var(--font-mono); font-weight:700; font-size:0.76rem;">94.2%</span>
                  <div class="progress-bar-wrap"><div class="progress-fill" style="width:94.2%;"></div></div>
                </div>
              </td>
              <td><span class="status-pill status-scaling">Scaling to State</span></td>
            </tr>

            <tr>
              <td>
                <span class="district-tag">📍 Dholera, Ahmedabad</span>
              </td>
              <td>
                <strong>Dholera SIR Master Parcel Spatial Ledger</strong>
                <div style="font-size:0.72rem; color:var(--gov-text-muted);">Special Investment Region Cadastre</div>
              </td>
              <td><strong>IIT Gandhinagar</strong></td>
              <td>Drone LiDAR parcel boundary demarcation and 16-digit Bhu-Aadhaar linking.</td>
              <td>
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="font-family:var(--font-mono); font-weight:700; font-size:0.76rem;">88.0%</span>
                  <div class="progress-bar-wrap"><div class="progress-fill" style="width:88.0%;"></div></div>
                </div>
              </td>
              <td><span class="status-pill status-testing">Field Testing</span></td>
            </tr>

            <tr>
              <td>
                <span class="district-tag">📍 Kevadia, Narmada</span>
              </td>
              <td>
                <strong>Section 73AA Tribal Title Protection Cadastre</strong>
                <div style="font-size:0.72rem; color:var(--gov-text-muted);">Statutory Scheduled Area Audit</div>
              </td>
              <td><strong>Gujarat National Law University (GNLU)</strong></td>
              <td>Automated restriction alerts on non-tribal transfer attempts without Collector sanction.</td>
              <td>
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="font-family:var(--font-mono); font-weight:700; font-size:0.76rem;">100%</span>
                  <div class="progress-bar-wrap"><div class="progress-fill" style="width:100%;"></div></div>
                </div>
              </td>
              <td><span class="status-pill status-scaling">Scaling to State</span></td>
            </tr>

            <tr>
              <td>
                <span class="district-tag">📍 Gautam Buddha Nagar, UP</span>
              </td>
              <td>
                <strong>Peri-Urban Agricultural Ceiling Sentinel</strong>
                <div style="font-size:0.72rem; color:var(--gov-text-muted);">UP Revenue Code 2006 Pilot</div>
              </td>
              <td><strong>IIT Delhi / UP Board of Revenue</strong></td>
              <td>Satellite-driven unauthorized layout detection and illegal subdivision alerts.</td>
              <td>
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="font-family:var(--font-mono); font-weight:700; font-size:0.76rem;">76.5%</span>
                  <div class="progress-bar-wrap"><div class="progress-fill" style="width:76.5%;"></div></div>
                </div>
              </td>
              <td><span class="status-pill status-eval">Policy Evaluation</span></td>
            </tr>

            <tr>
              <td>
                <span class="district-tag">📍 Haveli, Pune, MH</span>
              </td>
              <td>
                <strong>E-Hakk Paperless Mutation RTS Engine</strong>
                <div style="font-size:0.72rem; color:var(--gov-text-muted);">Maharashtra Land Revenue Code</div>
              </td>
              <td><strong>IIT Bombay / Settlement Commissioner</strong></td>
              <td>Automated 15-day statutory objection period processing with digital notice serving.</td>
              <td>
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="font-family:var(--font-mono); font-weight:700; font-size:0.76rem;">82.4%</span>
                  <div class="progress-bar-wrap"><div class="progress-fill" style="width:82.4%;"></div></div>
                </div>
              </td>
              <td><span class="status-pill status-testing">Field Testing</span></td>
            </tr>

            <tr>
              <td>
                <span class="district-tag">📍 Ujjain, Madhya Pradesh</span>
              </td>
              <td>
                <strong>AI Crop Girdawari & Drone Yield Cadastre</strong>
                <div style="font-size:0.72rem; color:var(--gov-text-muted);">MP Saara Integration</div>
              </td>
              <td><strong>IIM Indore / MP Land Records HQ</strong></td>
              <td>Self-attested farmer crop survey validated against Sentinel-2 spectral indices.</td>
              <td>
                <div style="display:flex; align-items:center; gap:8px;">
                  <span style="font-family:var(--font-mono); font-weight:700; font-size:0.76rem;">91.0%</span>
                  <div class="progress-bar-wrap"><div class="progress-fill" style="width:91.0%;"></div></div>
                </div>
              </td>
              <td><span class="status-pill status-scaling">Scaling to State</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

  </main>

  <!-- ======================================================================
       CHALLENGE SUBMISSION MODAL
       ====================================================================== -->
  <div class="inno-modal" id="challengeModal" onclick="closeModalOnBackdrop(event, 'challengeModal')">
    <div class="inno-modal-content">
      <div class="inno-modal-header">
        <div>
          <div class="inno-modal-title" id="modalChallengeTitle">Submit Solution / Register Team</div>
          <p style="font-size:0.74rem; color:var(--gov-text-muted);" id="modalChallengeDept">DoLR National Innovation Pipeline • MoRD Problem Statement 26019</p>
        </div>
        <button class="inno-modal-close" onclick="closeModal('challengeModal')">&times;</button>
      </div>
      
      <form onsubmit="handleChallengeSubmit(event)">
        <div class="form-group">
          <label>Lead Applicant / Institution / Startup Name *</label>
          <input type="text" class="form-control" placeholder="e.g. Geospace Informatics Lab / IIT Bombay" required />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Primary Contact Email *</label>
            <input type="email" class="form-control" placeholder="lead.investigator@institute.ac.in" required />
          </div>
          <div class="form-group">
            <label>Applicant Category *</label>
            <select class="form-control">
              <option>Central / State University Research Lab</option>
              <option>IIT / IIM / NIT / NLU Research Consortium</option>
              <option>DPIIT-Recognized GovTech Startup</option>
              <option>Independent Researcher / Specialist</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label>Technical Methodology Abstract & Benchmark Target *</label>
          <textarea class="form-control" rows="3" placeholder="Summarize your architecture, spatial AI pipeline, accuracy metrics, and integration with state cadastral databases..." required></textarea>
        </div>

        <div class="form-group">
          <label>Prototype Code Repository / Whitepaper Link (GitHub or PDF URL) *</label>
          <input type="url" class="form-control" placeholder="https://github.com/your-team/cadastral-alignment" required />
        </div>

        <button type="submit" class="btn-submit-solution" style="padding:10px; margin-top:8px;">
          Submit Challenge Entry to DoLR Technical Committee
        </button>
      </form>
    </div>
  </div>

  <!-- ======================================================================
       GRANT APPLICATION MODAL
       ====================================================================== -->
  <div class="inno-modal" id="grantModal" onclick="closeModalOnBackdrop(event, 'grantModal')">
    <div class="inno-modal-content">
      <div class="inno-modal-header">
        <div>
          <div class="inno-modal-title">Land Governance Research Grant Proposal (LGRGS)</div>
          <p style="font-size:0.74rem; color:var(--gov-text-muted);">Department of Land Resources (MoRD) • Academic Fellowship Scheme 2026-27</p>
        </div>
        <button class="inno-modal-close" onclick="closeModal('grantModal')">&times;</button>
      </div>
      
      <form onsubmit="handleGrantSubmit(event)">
        <div class="form-group">
          <label>Principal Investigator (PI) Full Name & Designation *</label>
          <input type="text" class="form-control" placeholder="Prof. / Dr. Full Name, Designation" required />
        </div>

        <div class="form-group">
          <label>Host Institution / Central University / IIT *</label>
          <input type="text" class="form-control" placeholder="e.g. National Law School of India / CEPT / IIT Gandhinagar" required />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>Priority Research Theme *</label>
            <select class="form-control">
              <option>Spatial Econometrics & Jantri Capture</option>
              <option>Tenancy Law Formalization & Agricultural Yield</option>
              <option>Carbon Credit Agro-Forestry Cadastres</option>
              <option>CRZ & Coastal Cadastral Vulnerability</option>
              <option>Inter-State Digital Cadastre Harmonization</option>
            </select>
          </div>
          <div class="form-group">
            <label>Requested Grant Budget *</label>
            <select class="form-control">
              <option>₹15,00,000 (12 Months Study)</option>
              <option>₹25,00,000 (18 Months Empirical Field Pilot)</option>
              <option>₹50,00,000 (24 Months Multi-State Consortium)</option>
            </select>
          </div>
        </div>

        <div class="form-group">
          <label>Executive Proposal Abstract & Statutory Deliverables *</label>
          <textarea class="form-control" rows="3" placeholder="Define core empirical hypothesis, sample districts, data ingestion methodology, and policy reform deliverable for DoLR..." required></textarea>
        </div>

        <button type="submit" class="btn-apply-grant" style="width:100%; justify-content:center; padding:10px; margin-top:8px;">
          Submit Academic Proposal for Peer Review
        </button>
      </form>
    </div>
  </div>

  <!-- Statutory Legal Disclaimer Modal -->
  <div id="disclaimerModal" class="inno-modal" onclick="closeModalOnBackdrop(event, 'disclaimerModal')">
    <div class="inno-modal-content" style="max-width:560px;">
      <div class="inno-modal-header">
        <div class="inno-modal-title">Statutory Legal Disclaimer & Terms of Sandbox</div>
        <button class="inno-modal-close" onclick="closeModal('disclaimerModal')">&times;</button>
      </div>
      <div style="font-size:0.82rem; line-height:1.6; color:var(--gov-text-secondary);">
        <p style="margin-bottom:12px;"><strong>Department of Land Resources (DoLR), Ministry of Rural Development:</strong></p>
        <p style="margin-bottom:12px;">The Bhumi-Niti Innovation Hub operates under the Smart India Sandbox framework. Challenge entries, grant awards, and experimental pilots do not modify statutory land revenue ledgers or official records of rights unless formally adopted via state gazette notification.</p>
        <p style="margin-bottom:12px;">All algorithms submitted are evaluated against accuracy, privacy, and GIGW 3.0 cyber-security guidelines under the direction of the DoLR Technical Advisory Committee.</p>
        <div style="text-align:right; margin-top:16px;">
          <button class="btn-submit-solution" onclick="closeModal('disclaimerModal')" style="width:auto; padding:6px 16px;">Acknowledge & Close</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast Notification Feedback -->
  <div class="toast-notice" id="toastNotice">
    <span>✅</span>
    <span id="toastMsg">Action successfully completed</span>
  </div>

  <!-- ======================================================================
       TIER 3: GIGW 3.0 MANDATORY COMPLIANCE FOOTER
       ====================================================================== -->
  <footer class="gov-footer" role="contentinfo">
    <div class="footer-left-audit">
      <div class="footer-sync-audit">
        <span class="sync-dot" aria-hidden="true"></span>
        <span>Innovation sandbox connected with MyGov, SIH 2026, and DoLR Research Grants. Status: <strong>Active</strong>.</span>
      </div>
      <span class="util-sep">|</span>
      <span class="footer-disclaimer-btn" onclick="openDisclaimerModal()">Statutory Legal Disclaimer</span>
    </div>

    <div class="footer-right-credits">
      <span>Bhumi-Niti National Innovation Hub | Ministry of Rural Development, Government of India</span>
      <span class="footer-gigw-badge">GIGW 3.0 • WCAG 2.1 AA</span>
    </div>
  </footer>

  <!-- ======================================================================
       CLIENT JAVASCRIPT APPLICATION LOGIC
       ====================================================================== -->
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      initClock();
      syncUserPreferences();
    });

    // ------------------------------------------------------------------------
    // 1. Tab Switching Logic
    // ------------------------------------------------------------------------
    function switchTab(tabKey) {
      // Remove active from all tab buttons & panes
      const btns = document.querySelectorAll('.inno-tab-btn');
      const panes = document.querySelectorAll('.tab-content-pane');

      btns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      panes.forEach(p => p.classList.remove('active'));

      if (tabKey === 'challenges') {
        document.getElementById('tabBtnChallenges').classList.add('active');
        document.getElementById('tabBtnChallenges').setAttribute('aria-selected', 'true');
        document.getElementById('paneChallenges').classList.add('active');
      } else if (tabKey === 'grants') {
        document.getElementById('tabBtnGrants').classList.add('active');
        document.getElementById('tabBtnGrants').setAttribute('aria-selected', 'true');
        document.getElementById('paneGrants').classList.add('active');
      } else if (tabKey === 'pilots') {
        document.getElementById('tabBtnPilots').classList.add('active');
        document.getElementById('tabBtnPilots').setAttribute('aria-selected', 'true');
        document.getElementById('panePilots').classList.add('active');
      }
    }

    // ------------------------------------------------------------------------
    // 2. Modals & Actions
    // ------------------------------------------------------------------------
    function openChallengeModal(title, dept) {
      document.getElementById("modalChallengeTitle").textContent = `Submit Solution: ${title}`;
      document.getElementById("modalChallengeDept").textContent = `Issuing Authority: ${dept} • MoRD Problem Statement 26019`;
      document.getElementById("challengeModal").style.display = "flex";
    }

    function openGrantModal() {
      document.getElementById("grantModal").style.display = "flex";
    }

    function openDisclaimerModal() {
      document.getElementById("disclaimerModal").style.display = "flex";
    }

    function closeModal(id) {
      document.getElementById(id).style.display = "none";
    }

    function closeModalOnBackdrop(e, id) {
      if (e.target === document.getElementById(id)) {
        closeModal(id);
      }
    }

    function handleChallengeSubmit(e) {
      e.preventDefault();
      closeModal("challengeModal");
      const refId = "DoLR-CHAL-2026-" + Math.floor(1000 + Math.random() * 9000);
      showToast(`Challenge submission accepted! Registered under DoLR Docket ID: ${refId}`);
    }

    function handleGrantSubmit(e) {
      e.preventDefault();
      closeModal("grantModal");
      const grantId = "DoLR-FELLOW-2026-" + Math.floor(1000 + Math.random() * 9000);
      showToast(`Academic research proposal submitted! Queued for DoLR Advisory Review ID: ${grantId}`);
    }

    function triggerDownloadGuidelines() {
      showToast("Downloading Land Governance Research Grant Scheme (LGRGS) Guidelines PDF...");
    }

    function showToast(msg) {
      const t = document.getElementById("toastNotice");
      document.getElementById("toastMsg").textContent = msg;
      t.style.display = "flex";
      setTimeout(() => { t.style.display = "none"; }, 5000);
    }

    // ------------------------------------------------------------------------
    // 3. User Preferences (Role & State)
    // ------------------------------------------------------------------------
    function syncUserPreferences() {
      const savedPersona = localStorage.getItem("bhumi_persona") || "citizen";
      const savedState = localStorage.getItem("bhumi_state") || "gujarat";
      
      const pSel = document.getElementById("personaSelector");
      const sSel = document.getElementById("stateSelector");
      if (pSel) pSel.value = savedPersona;
      if (sSel) sSel.value = savedState;
    }

    function onPersonaChange(val) {
      localStorage.setItem("bhumi_persona", val);
      showToast(`Switched Role: ${val === 'citizen' ? 'Public Citizen' : (val === 'researcher' ? 'Academic Researcher' : 'DoLR Policy Official')}`);
    }

    function onStateChange(val) {
      localStorage.setItem("bhumi_state", val);
      showToast(`Selected Jurisdiction: ${val === 'gujarat' ? 'Gujarat (Active Pilot)' : (val === 'up' ? 'Uttar Pradesh (Demo)' : 'Maharashtra (Demo)')}`);
    }

    // ------------------------------------------------------------------------
    // 4. GIGW 3.0 Accessibility Controls
    // ------------------------------------------------------------------------
    function initClock() {
      function update() {
        const now = new Date();
        const istOffset = 5.5 * 60 * 60 * 1000;
        const istDate = new Date(now.getTime() + istOffset + (now.getTimezoneOffset() * 60000));
        const hours = String(istDate.getHours()).padStart(2, '0');
        const minutes = String(istDate.getMinutes()).padStart(2, '0');
        const seconds = String(istDate.getSeconds()).padStart(2, '0');
        const el = document.getElementById('istClock');
        if (el) el.textContent = `${hours}:${minutes}:${seconds} IST`;
      }
      update();
      setInterval(update, 1000);
    }

    let currentFontSizeStep = 0;
    function adjustFontSize(delta) {
      if (delta === 0) {
        currentFontSizeStep = 0;
      } else {
        currentFontSizeStep = Math.max(-1, Math.min(2, currentFontSizeStep + delta));
      }
      const sizes = ['13px', '14px', '15px', '16px'];
      document.documentElement.style.fontSize = sizes[currentFontSizeStep + 1];

      const btns = document.querySelectorAll('.font-btn');
      btns.forEach((btn, idx) => {
        btn.classList.toggle('active', (delta === 0 && idx === 1) || (delta === -1 && idx === 0) || (delta === 1 && idx === 2));
      });
    }

    function toggleContrast() {
      document.body.classList.toggle('gov-high-contrast');
      const isHigh = document.body.classList.contains('gov-high-contrast');
      const text = document.getElementById('contrastText');
      if (text) text.textContent = isHigh ? 'Normal' : 'Contrast';
    }

    function onLangChange(lang) {
      if (lang === 'hi') {
        showToast('हिन्दी भाषा संस्करण: नवाचार हब और अनुसंधान अनुदान लोड हो रहा है...');
      } else if (lang === 'gu') {
        showToast('ગુજરાતી ભાષા સંસ્કરણ: ઇનોવેશન હબ લોડ થઈ રહ્યું છે...');
      }
    }

    function triggerScreenReaderAlert() {
      alert("Screen Reader Mode Active. Use Tab / Shift+Tab to navigate between innovation challenges, research grants, and state pilot trackers.");
    }
  </script>

</body>
</html>
"""
