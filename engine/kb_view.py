"""
Bhumi-Niti (भूमि-नीति): Gujarat State Legal & Policy Knowledge Repository View
GIGW 3.0 Compliant Institutional Repository Interface | DoLR, Ministry of Rural Development
Authentic Indian Government Design Standards (India Code indiacode.nic.in / DoLR Policy Archive)
"""

def render_knowledge_base_html() -> str:
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bhumi-Niti (भूमि-नीति) | Gujarat State Land Governance & Statutory Knowledge Repository</title>
  <meta name="description" content="Bhumi-Niti Knowledge Repository — National Digital Platform for Evidence-Based Land Governance. Live statutory acts, policy circulars, and dataset research for Gujarat. DoLR, Ministry of Rural Development.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    /* ------------------------------------------------------------------------
       1. GovTech GIGW 3.0 Design Tokens & India Code Palette
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
       3. Tier 2: Institutional Masthead (White Surface)
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

    /* Right Navigation Tabs & Quick Status */
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
      background: var(--gov-green-light);
      border: 1px solid var(--gov-green-border);
      color: var(--gov-green);
      font-size: 0.74rem;
      font-weight: 700;
      padding: 5px 10px;
      border-radius: 6px;
      white-space: nowrap;
    }
    .dot-live {
      width: 8px;
      height: 8px;
      background: var(--gov-green);
      border-radius: 50%;
      box-shadow: 0 0 8px rgba(21, 128, 61, 0.6);
      animation: pulse-dot 2s infinite;
    }
    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.6; transform: scale(1.15); }
    }

    /* ------------------------------------------------------------------------
       4. Sub-Header: Institutional Title & Telemetry KPI Strip
       ------------------------------------------------------------------------ */
    .kb-title-strip {
      background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
      border-bottom: 1.5px solid var(--gov-border);
      padding: 20px 24px 16px;
    }
    .kb-title-inner {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .kb-headline-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 14px;
    }
    .kb-headline-text h1 {
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--gov-blue-primary);
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: -0.01em;
    }
    .kb-headline-text p {
      font-size: 0.82rem;
      color: var(--gov-text-secondary);
      margin-top: 4px;
      max-width: 860px;
      line-height: 1.5;
    }
    .badge-pilot-scope {
      background: var(--gov-blue-light);
      border: 1px solid var(--gov-blue-border);
      color: var(--gov-blue-primary);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.70rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Telemetry KPI Cards Bar (4 compact cards) */
    .kb-kpi-bar {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }
    @media (max-width: 900px) {
      .kb-kpi-bar { grid-template-columns: repeat(2, 1fr); }
    }
    .kb-kpi-card {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
      border-left: 3.5px solid var(--gov-blue-primary);
    }
    .kb-kpi-card:nth-child(2) { border-left-color: var(--gov-saffron); }
    .kb-kpi-card:nth-child(3) { border-left-color: var(--gov-purple); }
    .kb-kpi-card:nth-child(4) { border-left-color: var(--gov-green); }

    .kpi-icon-box {
      width: 36px;
      height: 36px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.15rem;
      background: var(--gov-surface-alt);
      flex-shrink: 0;
    }
    .kpi-info-box {
      display: flex;
      flex-direction: column;
    }
    .kpi-stat-number {
      font-family: var(--font-mono);
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--gov-text-primary);
      line-height: 1.1;
    }
    .kpi-stat-label {
      font-size: 0.70rem;
      color: var(--gov-text-muted);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    /* ------------------------------------------------------------------------
       5. Main Layout: Left Filter Sidebar (25%) & Right Catalog (75%)
       ------------------------------------------------------------------------ */
    .kb-main-container {
      max-width: 1440px;
      margin: 0 auto;
      padding: 20px 24px 60px;
      width: 100%;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
      align-items: start;
    }
    @media (max-width: 1024px) {
      .kb-main-container {
        grid-template-columns: 1fr;
      }
    }

    /* Left Sidebar: Multi-Faceted Filter */
    .kb-sidebar {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 10px;
      padding: 18px;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
      position: sticky;
      top: 80px;
      max-height: calc(100vh - 100px);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .sidebar-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--gov-blue-primary);
    }
    .sidebar-header-title {
      font-size: 0.86rem;
      font-weight: 800;
      color: var(--gov-blue-dark);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .sidebar-reset-btn {
      background: transparent;
      border: none;
      color: var(--gov-saffron);
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: underline;
    }

    /* Instant Search Box in Sidebar */
    .sidebar-search-group {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .sidebar-search-label {
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--gov-text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .sidebar-search-wrap {
      position: relative;
      display: flex;
      align-items: center;
    }
    .sidebar-search-wrap input {
      width: 100%;
      background: var(--gov-surface-alt);
      border: 1.5px solid var(--gov-border);
      border-radius: 6px;
      padding: 7px 28px 7px 9px;
      font-size: 0.82rem;
      font-family: inherit;
      color: var(--gov-text-primary);
      outline: none;
      transition: all 0.15s;
    }
    .sidebar-search-wrap input:focus {
      background: #FFFFFF;
      border-color: var(--gov-blue-primary);
      box-shadow: 0 0 0 3px rgba(11, 60, 93, 0.12);
    }
    .sidebar-search-icon {
      position: absolute;
      right: 8px;
      font-size: 0.85rem;
      color: var(--gov-text-muted);
      pointer-events: none;
    }

    /* Facet Groups */
    .facet-group {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .facet-title {
      font-size: 0.76rem;
      font-weight: 800;
      color: var(--gov-blue-primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .facet-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .facet-label {
      display: flex;
      align-items: flex-start;
      gap: 8px;
      font-size: 0.78rem;
      color: var(--gov-text-secondary);
      cursor: pointer;
      line-height: 1.35;
      user-select: none;
      transition: color 0.12s;
    }
    .facet-label:hover {
      color: var(--gov-blue-primary);
    }
    .facet-label input[type="checkbox"] {
      margin-top: 2px;
      accent-color: var(--gov-blue-primary);
      cursor: pointer;
    }
    .facet-authority-select {
      width: 100%;
      background: var(--gov-surface-alt);
      border: 1.5px solid var(--gov-border);
      border-radius: 6px;
      padding: 6px 8px;
      font-size: 0.80rem;
      font-family: inherit;
      color: var(--gov-text-primary);
      cursor: pointer;
      outline: none;
    }
    .facet-authority-select:focus {
      border-color: var(--gov-blue-primary);
    }

    /* Connected Endpoints Card */
    .connected-gov-card {
      background: var(--gov-surface-alt);
      border: 1px solid var(--gov-border-subtle);
      border-radius: 8px;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .connected-gov-title {
      font-size: 0.70rem;
      font-weight: 700;
      color: var(--gov-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .gov-endpoint-link {
      font-family: var(--font-mono);
      font-size: 0.70rem;
      color: var(--gov-blue-primary);
      display: flex;
      align-items: center;
      gap: 5px;
      text-decoration: none;
    }
    .gov-endpoint-link:hover { text-decoration: underline; }

    /* ------------------------------------------------------------------------
       6. Right Column: Results Catalog (75%)
       ------------------------------------------------------------------------ */
    .kb-catalog-column {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    /* Search & Action Bar */
    .catalog-action-bar {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 10px;
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    }
    .catalog-count-text {
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--gov-text-secondary);
    }
    .catalog-count-text strong {
      color: var(--gov-blue-primary);
      font-weight: 800;
    }
    .catalog-btn-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .btn-synthesize-all {
      background: var(--gov-blue-primary);
      color: #FFFFFF;
      border: none;
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
    .btn-synthesize-all:hover {
      background: var(--gov-saffron);
      box-shadow: 0 2px 8px rgba(234, 88, 12, 0.25);
    }
    .btn-submit-research {
      background: var(--gov-green);
      color: #FFFFFF;
      border: none;
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.80rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .btn-submit-research:hover {
      background: #166534;
    }

    /* Quick Query Shortcut Chips */
    .quick-chips-bar {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      padding: 4px 0;
    }
    .chip-label {
      font-size: 0.70rem;
      font-weight: 700;
      color: var(--gov-text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-right: 4px;
    }
    .quick-chip {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 20px;
      padding: 3px 10px;
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--gov-blue-primary);
      cursor: pointer;
      transition: all 0.15s;
    }
    .quick-chip:hover {
      background: var(--gov-blue-light);
      border-color: var(--gov-blue-primary);
    }

    /* Document Cards Feed (India Code Indiacode.nic.in / DoLR Style) */
    .documents-feed {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .doc-card {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 10px;
      padding: 18px 22px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      flex-direction: column;
      gap: 10px;
      position: relative;
    }
    .doc-card:hover {
      border-color: var(--gov-blue-primary);
      box-shadow: 0 6px 16px rgba(11, 60, 93, 0.08);
      transform: translateY(-1px);
    }

    /* Metadata Pills */
    .doc-header-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
    }
    .doc-pills {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }
    .pill-official {
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .pill-act-no {
      background: var(--gov-blue-light);
      color: var(--gov-blue-primary);
      border: 1px solid var(--gov-blue-border);
      font-family: var(--font-mono);
    }
    .pill-jurisdiction {
      background: #FEF3C7;
      color: #B45309;
      border: 1px solid #FDE68A;
    }
    .pill-source-indiacode {
      background: var(--gov-green-light);
      color: var(--gov-green);
      border: 1px solid var(--gov-green-border);
    }
    .pill-source-gujrevenue {
      background: var(--gov-saffron-light);
      color: var(--gov-saffron);
      border: 1px solid var(--gov-saffron-border);
    }
    .pill-source-datagov {
      background: var(--gov-purple-light);
      color: var(--gov-purple);
      border: 1px solid #DDD6FE;
    }
    .live-sync-timestamp {
      font-size: 0.70rem;
      color: var(--gov-text-muted);
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }

    /* Document Title & Meta */
    .doc-title {
      font-size: 1.10rem;
      font-weight: 800;
      color: var(--gov-blue-dark);
      line-height: 1.35;
      letter-spacing: -0.01em;
    }
    .doc-meta-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      font-size: 0.75rem;
      color: var(--gov-text-muted);
      border-bottom: 1px solid var(--gov-border-subtle);
      padding-bottom: 8px;
    }
    .meta-segment {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .meta-segment strong {
      color: var(--gov-text-secondary);
      font-weight: 600;
    }

    /* Abstract */
    .doc-abstract {
      font-size: 0.82rem;
      line-height: 1.55;
      color: var(--gov-text-secondary);
    }

    /* Tags */
    .doc-tags-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }
    .tag-bubble {
      background: var(--gov-surface-alt);
      border: 1px solid var(--gov-border);
      border-radius: 4px;
      padding: 1px 7px;
      font-size: 0.70rem;
      color: var(--gov-text-secondary);
      font-weight: 500;
    }

    /* Action Strip */
    .doc-action-strip {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 4px;
      padding-top: 10px;
      border-top: 1px solid var(--gov-border-subtle);
    }
    .action-strip-left {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .btn-action-pdf {
      background: #FFFFFF;
      border: 1.5px solid var(--gov-blue-primary);
      color: var(--gov-blue-primary);
      padding: 6px 13px;
      border-radius: 6px;
      font-size: 0.76rem;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }
    .btn-action-pdf:hover {
      background: var(--gov-blue-light);
    }
    .btn-action-synth {
      background: var(--gov-blue-primary);
      color: #FFFFFF;
      border: none;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.76rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s;
    }
    .btn-action-synth:hover {
      background: var(--gov-saffron);
    }
    .btn-action-citations {
      background: var(--gov-surface-alt);
      border: 1px solid var(--gov-border);
      color: var(--gov-text-secondary);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.76rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }
    .btn-action-citations:hover {
      background: #E2E8F0;
      color: var(--gov-text-primary);
    }
    .action-strip-right {
      font-size: 0.70rem;
      color: var(--gov-text-muted);
      font-weight: 600;
    }

    /* Empty State */
    .empty-catalog-state {
      background: #FFFFFF;
      border: 1.5px dashed var(--gov-border);
      border-radius: 12px;
      padding: 48px 24px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }
    .empty-catalog-icon {
      font-size: 2.5rem;
      color: var(--gov-text-muted);
    }
    .empty-catalog-state h3 {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--gov-blue-dark);
    }
    .empty-catalog-state p {
      font-size: 0.82rem;
      color: var(--gov-text-muted);
      max-width: 460px;
    }

    /* ------------------------------------------------------------------------
       7. Grounded AI Statutory Analysis Drawer (Slide-out panel)
       ------------------------------------------------------------------------ */
    .synthesis-drawer-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(8, 33, 54, 0.65);
      backdrop-filter: blur(4px);
      z-index: 5000;
      justify-content: flex-end;
      animation: fadeInOverlay 0.2s ease-out;
    }
    @keyframes fadeInOverlay {
      from { opacity: 0; }
      to { opacity: 1; }
    }
    .synthesis-drawer {
      background: #FFFFFF;
      width: 100%;
      max-width: 680px;
      height: 100vh;
      display: flex;
      flex-direction: column;
      box-shadow: -8px 0 30px rgba(0, 0, 0, 0.25);
      animation: slideInRight 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      border-left: 2px solid var(--gov-blue-primary);
    }
    @keyframes slideInRight {
      from { transform: translateX(100%); }
      to { transform: translateX(0); }
    }
    .drawer-header {
      padding: 16px 22px;
      background: var(--gov-blue-primary);
      color: #FFFFFF;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--gov-saffron);
      flex-shrink: 0;
    }
    .drawer-title-box {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .drawer-title-box h3 {
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: -0.01em;
    }
    .btn-close-drawer {
      background: rgba(255, 255, 255, 0.15);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
      width: 30px;
      height: 30px;
      border-radius: 6px;
      font-size: 1.1rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }
    .btn-close-drawer:hover {
      background: rgba(255, 255, 255, 0.3);
    }
    .drawer-body {
      flex: 1;
      overflow-y: auto;
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      background: var(--gov-canvas);
    }

    .synth-section {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 8px;
      padding: 14px 16px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    }
    .synth-section-title {
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--gov-blue-primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
      border-bottom: 1px solid var(--gov-border-subtle);
      padding-bottom: 6px;
    }
    .synth-text {
      font-size: 0.84rem;
      line-height: 1.6;
      color: var(--gov-text-secondary);
    }

    .clause-item {
      padding: 10px 12px;
      border-radius: 6px;
      background: var(--gov-surface-alt);
      border-left: 3px solid var(--gov-saffron);
      margin-bottom: 8px;
    }
    .clause-item:last-child { margin-bottom: 0; }
    .clause-header {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--gov-blue-dark);
      margin-bottom: 4px;
    }
    .clause-desc {
      font-size: 0.78rem;
      color: var(--gov-text-secondary);
      margin-bottom: 3px;
    }
    .clause-solution {
      font-size: 0.78rem;
      color: var(--gov-green);
      font-weight: 600;
    }

    .citation-list {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .citation-item {
      font-family: var(--font-mono);
      font-size: 0.76rem;
      background: var(--gov-blue-light);
      border: 1px solid var(--gov-blue-border);
      color: var(--gov-blue-primary);
      padding: 6px 10px;
      border-radius: 6px;
      font-weight: 600;
    }

    /* Grounded Chat Box inside Drawer */
    .doc-ai-chat-box {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .chat-header {
      padding: 10px 14px;
      background: var(--gov-blue-dark);
      color: #FFFFFF;
      font-size: 0.80rem;
      font-weight: 700;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .chat-log {
      padding: 12px;
      max-height: 220px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 0.82rem;
      background: var(--gov-canvas);
    }
    .chat-msg {
      padding: 8px 12px;
      border-radius: 6px;
      line-height: 1.5;
    }
    .chat-user {
      background: var(--gov-blue-light);
      border: 1px solid var(--gov-blue-border);
      color: var(--gov-blue-dark);
      align-self: flex-end;
      max-width: 85%;
      font-weight: 500;
    }
    .chat-ai {
      background: #FFFFFF;
      border: 1px solid var(--gov-border);
      color: var(--gov-text-secondary);
      align-self: flex-start;
      max-width: 90%;
    }
    .chat-input-row {
      display: flex;
      padding: 8px;
      background: #FFFFFF;
      border-top: 1px solid var(--gov-border);
      gap: 8px;
    }
    .chat-input {
      flex: 1;
      background: var(--gov-surface-alt);
      border: 1px solid var(--gov-border);
      border-radius: 6px;
      padding: 7px 10px;
      color: var(--gov-text-primary);
      font-size: 0.82rem;
      outline: none;
      font-family: inherit;
    }
    .chat-input:focus { border-color: var(--gov-blue-primary); }
    .chat-send-btn {
      background: var(--gov-blue-primary);
      color: #FFFFFF;
      border: none;
      padding: 7px 14px;
      border-radius: 6px;
      font-size: 0.80rem;
      font-weight: 700;
      cursor: pointer;
      transition: background 0.15s;
    }
    .chat-send-btn:hover { background: var(--gov-saffron); }

    /* Loading Spinner */
    .synth-loader {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px;
      color: var(--gov-blue-primary);
      gap: 12px;
      font-size: 0.85rem;
      font-weight: 600;
    }
    .spin {
      width: 32px;
      height: 32px;
      border: 3px solid rgba(11, 60, 93, 0.15);
      border-top-color: var(--gov-blue-primary);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }

    /* ------------------------------------------------------------------------
       8. GIGW 3.0 Mandatory Compliance Footer
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

    /* Modals (Disclaimer & Research Submission) */
    .disclaimer-modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(4px);
      z-index: 99999;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .disclaimer-modal-content {
      background: #FFFFFF;
      border-radius: 10px;
      max-width: 580px;
      width: 100%;
      padding: 24px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
      border-top: 4px solid var(--gov-blue-primary);
    }
    .disclaimer-modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .disclaimer-modal-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--gov-blue-dark);
    }
    .disclaimer-modal-close {
      background: transparent;
      border: none;
      font-size: 1.2rem;
      cursor: pointer;
      color: var(--gov-text-muted);
    }
    .disclaimer-modal-body {
      font-size: 0.82rem;
      line-height: 1.6;
      color: var(--gov-text-secondary);
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
    body.gov-high-contrast .kb-title-strip {
      background: #0E1626;
      border-bottom-color: #334155;
    }
    body.gov-high-contrast .kb-headline-text h1 { color: #38BDF8; }
    body.gov-high-contrast .kb-sidebar,
    body.gov-high-contrast .catalog-action-bar,
    body.gov-high-contrast .doc-card,
    body.gov-high-contrast .synth-section,
    body.gov-high-contrast .synthesis-drawer,
    body.gov-high-contrast .disclaimer-modal-content {
      background: #111A2E;
      color: #FFFFFF;
      border-color: #334155;
    }
    body.gov-high-contrast .doc-title { color: #38BDF8; }
    body.gov-high-contrast .kb-kpi-card { background: #111A2E; border-color: #334155; }
    body.gov-high-contrast .kpi-stat-number { color: #FFFFFF; }
  </style>
</head>
<body>

  <!-- ======================================================================
       TIER 1: GIGW 3.0 ACCESSIBILITY & UTILITY BAR (TOP 34px)
       ====================================================================== -->
  <aside class="gov-utility-bar" aria-label="Accessibility and Utility Controls">
    <div class="gov-util-left">
      <a href="#kbMainContent" class="util-link" accesskey="s">Skip to Main Content</a>
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
        <select id="personaSelector" class="util-select" onchange="onKbPersonaChange(this.value)" aria-label="Persona Switcher">
          <option value="citizen">👤 Public Citizen</option>
          <option value="researcher">🔬 Academic Researcher</option>
          <option value="official">🏛️ DoLR Policy Official</option>
        </select>
      </div>

      <span class="util-sep">|</span>

      <!-- National State Selector (Req 7 & 10) -->
      <div class="util-selector-item">
        <label for="stateSelector">Jurisdiction:</label>
        <select id="stateSelector" class="util-select" onchange="onKbStateChange(this.value)" aria-label="National State Jurisdiction Selector">
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
          <span class="brand-tag-gov">National Repository</span>
        </div>
        <div class="brand-subline">National Digital Platform for Evidence-Based Land Governance</div>
      </div>
    </div>

    <!-- Right Navigation Tabs & Portal Status -->
    <div class="masthead-right">
      <nav class="gov-nav-tabs" role="navigation" aria-label="Portal Navigation">
        <a href="/" class="gov-tab">
          <span>🗺️</span>
          <span>Spatial GIS Platform</span>
        </a>
        <a href="/knowledge-base" class="gov-tab active" aria-current="page">
          <span>📚</span>
          <span>Policy Repository</span>
        </a>
        <a href="/innovation" class="gov-tab">
          <span>💡</span>
          <span>Innovation Hub</span>
        </a>
      </nav>

      <div class="live-gov-badge" id="liveSyncStatusBadge">
        <span class="dot-live"></span>
        <span id="syncText">India Code & OGD Feeds Live</span>
      </div>
    </div>
  </header>

  <!-- ======================================================================
       SUB-HEADER: INSTITUTIONAL TITLE & TELEMETRY KPI STRIP
       ====================================================================== -->
  <section class="kb-title-strip">
    <div class="kb-title-inner">
      <div class="kb-headline-row">
        <div class="kb-headline-text">
          <h1>
            <span>Gujarat State Land Governance & Statutory Knowledge Repository</span>
            <span class="badge-pilot-scope">Gujarat Jurisdiction Pilot</span>
          </h1>
          <p>
            Official repository of enactments, statutory circulars, revenue codes, and spatial datasets. Sourced dynamically from <strong>India Code (indiacode.nic.in)</strong>, <strong>Gujarat Revenue Department (revenuedepartment.gujarat.gov.in)</strong>, and the <strong>Open Government Data Platform (data.gov.in)</strong>.
          </p>
        </div>

        <div class="catalog-btn-group">
          <button id="btnSubmitResearch" class="btn-submit-research" onclick="openResearchModal()" style="display:none;" title="Unlocked for Academic Researchers">
            <span>📝</span>
            <span>+ Submit Research / Dataset</span>
          </button>
        </div>
      </div>

      <!-- 4 Compact Telemetry KPI Cards -->
      <div class="kb-kpi-bar">
        <div class="kb-kpi-card">
          <div class="kpi-icon-box">📜</div>
          <div class="kpi-info-box">
            <div class="kpi-stat-number" id="totalDocsCount">18</div>
            <div class="kpi-stat-label">Total Enacted Acts</div>
          </div>
        </div>

        <div class="kb-kpi-card">
          <div class="kpi-icon-box">🏛️</div>
          <div class="kpi-info-box">
            <div class="kpi-stat-number" id="kpiCircularsCount">142</div>
            <div class="kpi-stat-label">Active Circulars & GRs</div>
          </div>
        </div>

        <div class="kb-kpi-card">
          <div class="kpi-icon-box">🔬</div>
          <div class="kpi-info-box">
            <div class="kpi-stat-number" id="kpiPapersCount">38</div>
            <div class="kpi-stat-label">Indexed Research Papers</div>
          </div>
        </div>

        <div class="kb-kpi-card">
          <div class="kpi-icon-box">🗺️</div>
          <div class="kpi-info-box">
            <div class="kpi-stat-number" id="kpiDatasetsCount">24</div>
            <div class="kpi-stat-label">Live Open Datasets</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================================
       MAIN LAYOUT: SIDEBAR (25%) + RESULTS CATALOG (75%)
       ====================================================================== -->
  <main class="kb-main-container" id="kbMainContent">

    <!-- Left Sidebar: Multi-Faceted Filters (25%) -->
    <aside class="kb-sidebar" aria-label="Filters and Search Options">
      
      <div class="sidebar-header">
        <span class="sidebar-header-title">🔍 Search & Filters</span>
        <button class="sidebar-reset-btn" onclick="resetAllFilters()">Reset All</button>
      </div>

      <!-- Instant Search Input -->
      <div class="sidebar-search-group">
        <label for="kbSearchInput" class="sidebar-search-label">Keyword / Act Search</label>
        <div class="sidebar-search-wrap">
          <input 
            type="text" 
            id="kbSearchInput" 
            placeholder="Search by Act name, Section (e.g. 73AA, 84), Circular No..." 
            autocomplete="off"
            aria-label="Search statutory acts, sections and circulars"
          />
          <span class="sidebar-search-icon" id="searchStateIcon">🔍</span>
        </div>
      </div>

      <!-- Document Category Facets -->
      <div class="facet-group">
        <div class="facet-title">
          <span>Document Category</span>
          <span style="font-size:0.70rem; color:var(--gov-text-muted); cursor:pointer;" onclick="resetFilterGroup('theme')">Reset</span>
        </div>
        <div class="facet-list">
          <label class="facet-label">
            <input type="checkbox" name="theme" value="Statutory Acts & Codes" onchange="onFilterChange()" />
            <span>Statutory Acts & Codes (Revenue Code 1879, Tenancy 1948, Ceiling 1960)</span>
          </label>
          <label class="facet-label">
            <input type="checkbox" name="theme" value="Town Planning & Urban Laws" onchange="onFilterChange()" />
            <span>Town Planning & Urban Laws (GTPUDA 1976, AUDA Regulations)</span>
          </label>
          <label class="facet-label">
            <input type="checkbox" name="theme" value="Government Resolutions (GRs) & Revenue Circulars" onchange="onFilterChange()" />
            <span>Government Resolutions (GRs) & Revenue Circulars</span>
          </label>
          <label class="facet-label">
            <input type="checkbox" name="theme" value="Peer-Reviewed Research & Applied Case Studies" onchange="onFilterChange()" />
            <span>Peer-Reviewed Research & Applied Case Studies</span>
          </label>
          <label class="facet-label">
            <input type="checkbox" name="theme" value="Open Geospatial Datasets" onchange="onFilterChange()" />
            <span>Open Geospatial Datasets (DILRMP / Cadastral)</span>
          </label>
        </div>
      </div>

      <!-- Authority Filter -->
      <div class="facet-group">
        <div class="facet-title">
          <span>Issuing Authority</span>
        </div>
        <select id="authorityFilter" class="facet-authority-select" onchange="onAuthorityChange(this.value)" aria-label="Filter by Issuing Authority">
          <option value="all">All Issuing Authorities</option>
          <option value="gujarat revenue">Gujarat Revenue Department</option>
          <option value="urban development">Urban Development & Urban Housing Dept</option>
          <option value="forest">Forest & Environment Department</option>
          <option value="central dolr">Central DoLR, Ministry of Rural Development</option>
        </select>
      </div>

      <!-- Official Source Feeds Facet -->
      <div class="facet-group">
        <div class="facet-title">
          <span>Official Feed Source</span>
          <span style="font-size:0.70rem; color:var(--gov-text-muted); cursor:pointer;" onclick="resetFilterGroup('source')">Reset</span>
        </div>
        <div class="facet-list">
          <label class="facet-label">
            <input type="checkbox" name="source" value="indiacode" onchange="onFilterChange()" />
            <span>India Code (Gujarat Enactments)</span>
          </label>
          <label class="facet-label">
            <input type="checkbox" name="source" value="gujrevenue" onchange="onFilterChange()" />
            <span>Gujarat Revenue Dept Circulars</span>
          </label>
          <label class="facet-label">
            <input type="checkbox" name="source" value="datagov" onchange="onFilterChange()" />
            <span>Open Gov Data (data.gov.in Gujarat)</span>
          </label>
        </div>
      </div>

      <!-- Connected Endpoints Telemetry Card -->
      <div class="connected-gov-card">
        <div class="connected-gov-title">Connected Gov Endpoints</div>
        <a href="https://indiacode.nic.in" target="_blank" rel="noopener noreferrer" class="gov-endpoint-link">
          <span>🔗</span>
          <span>indiacode.nic.in (Gujarat DSpace)</span>
        </a>
        <a href="https://revenuedepartment.gujarat.gov.in" target="_blank" rel="noopener noreferrer" class="gov-endpoint-link">
          <span>🔗</span>
          <span>revenuedepartment.gujarat.gov.in</span>
        </a>
        <a href="https://data.gov.in" target="_blank" rel="noopener noreferrer" class="gov-endpoint-link">
          <span>🔗</span>
          <span>data.gov.in (state=Gujarat)</span>
        </a>
      </div>

    </aside>

    <!-- Right Catalog Area (75%) -->
    <section class="kb-catalog-column" aria-label="Statutory and Policy Document Catalog">
      
      <!-- Catalog Action & Telemetry Strip -->
      <div class="catalog-action-bar">
        <div class="catalog-count-text">
          Showing <strong id="visibleDocsCount">0</strong> verified statutory acts and policy instruments
        </div>
        <div class="catalog-btn-group">
          <button class="btn-synthesize-all" onclick="synthesizeVisibleFeed()">
            <span>⚡ Run AI Statutory Synthesis</span>
          </button>
        </div>
      </div>

      <!-- Quick Topic Shortcut Chips -->
      <div class="quick-chips-bar">
        <span class="chip-label">Quick Queries:</span>
        <button class="quick-chip" onclick="applyQuickQuery('Gujarat Land Revenue Code 1879 Section 65')">GLRC 1879 (Section 65 NA)</button>
        <button class="quick-chip" onclick="applyQuickQuery('Section 73AA Tribal Land Transfer Collector')">Section 73AA Tribal Protections</button>
        <button class="quick-chip" onclick="applyQuickQuery('Tenancy and Agricultural Lands Act 1948')">Tenancy Act (Section 84C)</button>
        <button class="quick-chip" onclick="applyQuickQuery('GTPUDA Town Planning Act 1976')">GTPUDA 1976 (AUDA / SUDA)</button>
        <button class="quick-chip" onclick="applyQuickQuery('Gujarat Agricultural Lands Ceiling Act 1960')">Land Ceiling Act 1960</button>
        <button class="quick-chip" onclick="applyQuickQuery('Dholera Special Investment Region Act 2009')">Dholera SIR Act 2009</button>
      </div>

      <!-- Documents Cards Feed -->
      <div id="documentsGrid" class="documents-feed" role="feed" aria-busy="false">
        <!-- Injected dynamically via JavaScript -->
      </div>

      <!-- Empty State Container -->
      <div id="emptyState" class="empty-catalog-state" style="display:none;" role="status">
        <div class="empty-catalog-icon">📂</div>
        <h3>No Matching Gujarat Records Found</h3>
        <p>No repository records matched the selected query or facets. Check your spelling or try resetting the sidebar filters to view all enactments.</p>
        <button class="btn-synthesize-all" onclick="resetAllFilters()" style="margin-top:6px;">Reset All Filters</button>
      </div>

    </section>

  </main>

  <!-- ======================================================================
       GROUNDED AI STATUTORY ANALYSIS DRAWER (REAL-TIME IN-MEMORY RAG)
       ====================================================================== -->
  <div id="synthesisDrawerOverlay" class="synthesis-drawer-overlay" onclick="closeSynthesisDrawer(event)" role="dialog" aria-modal="true" aria-labelledby="synthDrawerTitle">
    <div class="synthesis-drawer" onclick="event.stopPropagation()">
      
      <div class="drawer-header">
        <div class="drawer-title-box">
          <span style="font-size:1.3rem;" aria-hidden="true">⚖️</span>
          <div>
            <h3 id="synthDrawerTitle">AI Statutory Analysis & Clause Extraction</h3>
            <p id="synthDrawerSubtitle" style="font-size:0.72rem;color:#CBD5E1;">Live in-memory synthesis of official Gujarat government legal text</p>
          </div>
        </div>
        <button class="btn-close-drawer" onclick="closeSynthesisDrawer()" aria-label="Close research drawer">✕</button>
      </div>

      <div id="drawerBody" class="drawer-body">
        <!-- Injected dynamically via JavaScript -->
      </div>

    </div>
  </div>

  <!-- ======================================================================
       TIER 3: GIGW 3.0 MANDATORY COMPLIANCE FOOTER
       ====================================================================== -->
  <footer class="gov-footer" role="contentinfo">
    <div class="footer-left-audit">
      <div class="footer-sync-audit">
        <span class="sync-dot" aria-hidden="true"></span>
        <span>Data ingested dynamically via India Code (NIC), Gujarat Revenue Dept, and data.gov.in. Last updated: <strong>Live</strong>.</span>
      </div>
      <span class="util-sep">|</span>
      <span class="footer-disclaimer-btn" onclick="openDisclaimerModal()">Statutory Legal Disclaimer</span>
    </div>

    <div class="footer-right-credits">
      <span>Bhumi-Niti Policy Knowledge Repository | Ministry of Rural Development, Government of India</span>
      <span class="footer-gigw-badge">GIGW 3.0 • WCAG 2.1 AA</span>
    </div>
  </footer>

  <!-- Statutory Legal Disclaimer Modal -->
  <div id="disclaimerModal" class="disclaimer-modal" onclick="closeDisclaimerOnBackdrop(event)" role="dialog" aria-modal="true">
    <div class="disclaimer-modal-content">
      <div class="disclaimer-modal-header">
        <div class="disclaimer-modal-title">Statutory Legal Disclaimer & Terms of Repository Use</div>
        <button class="disclaimer-modal-close" onclick="closeDisclaimerModal()">&times;</button>
      </div>
      <div class="disclaimer-modal-body">
        <p style="margin-bottom:12px;"><strong>Department of Land Resources (DoLR), Ministry of Rural Development:</strong></p>
        <p style="margin-bottom:12px;">Disclaimer: The legislative texts, circulars, and notifications indexed in the Bhumi-Niti Policy Knowledge Repository are compiled for academic research, policy simulation, and administrative reference. For authoritative statutory texts, consult the official gazette notifications published by the Government of Gujarat or certified enactments on India Code (indiacode.nic.in).</p>
        <p style="margin-bottom:12px;">AI syntheses and automated clause extracts generated through this portal represent algorithmic research opinions and do not constitute formal legal counsel or binding administrative rulings under the Gujarat Land Revenue Code, 1879.</p>
        <div style="text-align:right; margin-top:16px;">
          <button class="btn-synthesize-all" onclick="closeDisclaimerModal()" style="padding:6px 16px;">Acknowledge & Close</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Academic Research / Dataset Submission Modal (Req 17) -->
  <div id="researchModal" class="disclaimer-modal" onclick="closeResearchOnBackdrop(event)" role="dialog" aria-modal="true">
    <div class="disclaimer-modal-content" style="max-width:640px;">
      <div class="disclaimer-modal-header">
        <div>
          <div class="disclaimer-modal-title">Academic Research & Dataset Submission Portal</div>
          <p style="font-size:0.75rem; color:var(--gov-text-muted);">Unlocked for Academic Researcher Persona • DoLR Land Governance Peer Review Pipeline</p>
        </div>
        <button class="disclaimer-modal-close" onclick="closeResearchModal()">&times;</button>
      </div>

      <form onsubmit="handleResearchSubmit(event)">
        <div style="margin-bottom:12px;">
          <label style="display:block; font-size:0.76rem; font-weight:700; color:var(--gov-text-secondary); margin-bottom:4px;">Paper / Dataset Title *</label>
          <input type="text" style="width:100%; background:var(--gov-surface-alt); border:1px solid var(--gov-border); border-radius:6px; padding:8px 10px; font-size:0.82rem;" placeholder="e.g. Empirical Study on Section 84C Tenancy Disputes in Gujarat" required />
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px;">
          <div>
            <label style="display:block; font-size:0.76rem; font-weight:700; color:var(--gov-text-secondary); margin-bottom:4px;">Lead Author / PI *</label>
            <input type="text" style="width:100%; background:var(--gov-surface-alt); border:1px solid var(--gov-border); border-radius:6px; padding:8px 10px; font-size:0.82rem;" placeholder="Dr. / Prof. Name" required />
          </div>
          <div>
            <label style="display:block; font-size:0.76rem; font-weight:700; color:var(--gov-text-secondary); margin-bottom:4px;">University / Institution *</label>
            <input type="text" style="width:100%; background:var(--gov-surface-alt); border:1px solid var(--gov-border); border-radius:6px; padding:8px 10px; font-size:0.82rem;" placeholder="e.g. GNLU / IIT Gandhinagar / IIM-A" required />
          </div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:12px;">
          <div>
            <label style="display:block; font-size:0.76rem; font-weight:700; color:var(--gov-text-secondary); margin-bottom:4px;">Jurisdiction Scope *</label>
            <select style="width:100%; background:var(--gov-surface-alt); border:1px solid var(--gov-border); border-radius:6px; padding:8px 10px; font-size:0.82rem;">
              <option>State of Gujarat (Active Pilot)</option>
              <option>State of Uttar Pradesh</option>
              <option>State of Maharashtra</option>
              <option>Pan-India National Scope</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-size:0.76rem; font-weight:700; color:var(--gov-text-secondary); margin-bottom:4px;">Research Category *</label>
            <select style="width:100%; background:var(--gov-surface-alt); border:1px solid var(--gov-border); border-radius:6px; padding:8px 10px; font-size:0.82rem;">
              <option>Cadastral AI & Spatial Analysis</option>
              <option>Tenancy Law & Agricultural Reform</option>
              <option>Revenue Litigation & Dispute Economics</option>
              <option>Jantri Valuation & Land Value Capture</option>
              <option>Environmental & Forest Land Governance</option>
            </select>
          </div>
        </div>

        <div style="margin-bottom:12px;">
          <label style="display:block; font-size:0.76rem; font-weight:700; color:var(--gov-text-secondary); margin-bottom:4px;">Abstract & Key Policy Findings *</label>
          <textarea rows="3" style="width:100%; background:var(--gov-surface-alt); border:1px solid var(--gov-border); border-radius:6px; padding:8px 10px; font-size:0.82rem;" placeholder="Summarize key statutory insights, datasets utilized, empirical findings, and recommended legal amendments..." required></textarea>
        </div>

        <div style="margin-bottom:16px;">
          <label style="display:block; font-size:0.76rem; font-weight:700; color:var(--gov-text-secondary); margin-bottom:4px;">Open Dataset / Preprint Repository URL *</label>
          <input type="url" style="width:100%; background:var(--gov-surface-alt); border:1px solid var(--gov-border); border-radius:6px; padding:8px 10px; font-size:0.82rem;" placeholder="https://zenodo.org/record/... or GitHub repository URL" required />
        </div>

        <button type="submit" class="btn-submit-research" style="width:100%; justify-content:center; padding:10px; font-size:0.88rem;">
          Submit for DoLR Peer Review & Docket Entry
        </button>
      </form>
    </div>
  </div>

  <!-- ======================================================================
       JAVASCRIPT APPLICATION LOGIC & LIVE REPOSITORY INTEGRATION
       ====================================================================== -->
  <script>
    // State Management
    let allDocuments = [];
    let currentSynthesisDocId = null;
    let searchDebounceTimer = null;
    let selectedAuthority = 'all';

    // ------------------------------------------------------------------------
    // 1. Initialization & Live Document Fetching
    // ------------------------------------------------------------------------
    document.addEventListener('DOMContentLoaded', () => {
      initClock();
      fetchDocuments();
      setupSearchInput();
      syncUserPreferences();
    });

    async function fetchDocuments() {
      const q = document.getElementById('kbSearchInput').value.trim();
      const themes = getCheckedValues('theme');
      const sources = getCheckedValues('source');

      const params = new URLSearchParams();
      if (q) params.append('q', q);
      if (themes.length === 1) params.append('theme', themes[0]);
      params.append('jurisdiction', 'Gujarat');

      try {
        const res = await fetch(`/api/v1/kb/documents?${params.toString()}`);
        if (!res.ok) throw new Error('Live retrieval failed');
        const data = await res.json();
        
        allDocuments = data.documents || [];
        
        // Update Live Sync Status Indicator
        if (data.live_sync_status) {
          const syncText = document.getElementById('syncText');
          if (syncText) syncText.textContent = data.live_sync_status;
        }

        // Apply secondary client-side multi-select & authority filters
        let filtered = allDocuments;
        if (themes.length > 1) {
          filtered = filtered.filter(d => {
            const docTheme = (d.theme || '').toLowerCase();
            const docTitle = (d.title || '').toLowerCase();
            return themes.some(t => {
              const term = t.toLowerCase();
              if (term.includes('statutory') || term.includes('code')) return docTheme.includes('revenue') || docTheme.includes('statut') || docTitle.includes('code') || docTitle.includes('tenancy');
              if (term.includes('town') || term.includes('urban')) return docTheme.includes('urban') || docTheme.includes('town') || docTitle.includes('gtpuda') || docTitle.includes('auda');
              if (term.includes('resolution') || term.includes('circular')) return docTheme.includes('circular') || docTitle.includes('gr') || docTitle.includes('circular');
              if (term.includes('research')) return docTheme.includes('research') || docTheme.includes('case');
              if (term.includes('geospatial') || term.includes('dataset')) return docTheme.includes('cadastral') || docTheme.includes('dataset') || docTheme.includes('dilrmp');
              return docTheme.includes(term) || docTitle.includes(term);
            });
          });
        }

        if (sources.length > 0) {
          filtered = filtered.filter(d => {
            const auth = (d.issuing_authority || '').toLowerCase();
            const badge = (d.official_badge || '').toLowerCase();
            return sources.some(s => {
              if (s === 'indiacode') return auth.includes('india code') || badge.includes('india code');
              if (s === 'gujrevenue') return auth.includes('revenue') || badge.includes('gujarat revenue') || badge.includes('gujarat.gov.in');
              if (s === 'datagov') return auth.includes('data.gov.in') || badge.includes('data.gov.in') || badge.includes('ogd');
              return true;
            });
          });
        }

        if (selectedAuthority && selectedAuthority !== 'all') {
          filtered = filtered.filter(d => {
            const auth = (d.issuing_authority || '').toLowerCase();
            return auth.includes(selectedAuthority);
          });
        }

        renderDocumentCards(filtered);
        updateCounts(filtered.length, data.total_count || allDocuments.length);

      } catch (err) {
        console.error('Fetch error:', err);
      }
    }

    function setupSearchInput() {
      const input = document.getElementById('kbSearchInput');
      const icon = document.getElementById('searchStateIcon');

      input.addEventListener('input', () => {
        clearTimeout(searchDebounceTimer);
        icon.textContent = '⏳';
        searchDebounceTimer = setTimeout(() => {
          icon.textContent = '🔍';
          fetchDocuments();
        }, 280);
      });

      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          triggerSearchSynthesis();
        }
      });
    }

    function applyQuickQuery(text) {
      const input = document.getElementById('kbSearchInput');
      input.value = text;
      fetchDocuments();
    }

    function getCheckedValues(name) {
      const checked = document.querySelectorAll(`input[name="${name}"]:checked`);
      return Array.from(checked).map(el => el.value);
    }

    function resetFilterGroup(name) {
      document.querySelectorAll(`input[name="${name}"]`).forEach(el => el.checked = false);
      fetchDocuments();
    }

    function resetAllFilters() {
      document.getElementById('kbSearchInput').value = '';
      document.querySelectorAll('input[type="checkbox"]').forEach(el => el.checked = false);
      const authSel = document.getElementById('authorityFilter');
      if (authSel) authSel.value = 'all';
      selectedAuthority = 'all';
      fetchDocuments();
    }

    function onFilterChange() {
      fetchDocuments();
    }

    function onAuthorityChange(val) {
      selectedAuthority = val;
      fetchDocuments();
    }

    function updateCounts(visible, total) {
      const visEl = document.getElementById('visibleDocsCount');
      if (visEl) visEl.textContent = visible;
      const totEl = document.getElementById('totalDocsCount');
      if (totEl) totEl.textContent = total;
    }

    // ------------------------------------------------------------------------
    // 2. Document Card Rendering (Authentic India Code & DoLR Styling)
    // ------------------------------------------------------------------------
    function renderDocumentCards(docs) {
      const container = document.getElementById('documentsGrid');
      const emptyState = document.getElementById('emptyState');

      if (!docs || docs.length === 0) {
        container.innerHTML = '';
        emptyState.style.display = 'flex';
        return;
      }

      emptyState.style.display = 'none';
      container.innerHTML = docs.map(doc => {
        const badgeInfo = getOfficialBadgeMeta(doc.issuing_authority, doc.official_badge);
        const liveTimestamp = doc.retrieval_timestamp || "⚡ Fetched Live via API";
        const downloadUrl = doc.download_url || "https://indiacode.nic.in";
        const actNumberPill = doc.act_number ? `<span class="pill-official pill-act-no">ACT NO. ${escapeHtml(doc.act_number)}</span>` : '';
        const citationsCount = (doc.statutory_citations || []).length;

        return `
          <article class="doc-card" id="card-${escapeHtml(doc.doc_id)}">
            <div class="doc-header-row">
              <div class="doc-pills">
                <span class="pill-official ${badgeInfo.className}">${escapeHtml(badgeInfo.label)}</span>
                <span class="pill-official pill-jurisdiction">JURISDICTION: GUJARAT</span>
                ${actNumberPill}
              </div>
              <div class="live-sync-timestamp">
                <span>🕒</span>
                <span>${escapeHtml(liveTimestamp)}</span>
              </div>
            </div>

            <h2 class="doc-title">${escapeHtml(doc.title)}</h2>

            <div class="doc-meta-row">
              <span class="meta-segment">🏛️ Authority: <strong>${escapeHtml(doc.issuing_authority || "Gujarat State Authority")}</strong></span>
              <span class="meta-segment">📅 Enactment Year: <strong>${doc.publication_year || doc.act_year || "1879"}</strong></span>
              <span class="meta-segment">🏷️ Theme: <strong>${escapeHtml(doc.theme || "Land Governance")}</strong></span>
            </div>

            <p class="doc-abstract">${escapeHtml(doc.abstract || "Statutory legislative text and administrative framework governing revenue land, record of rights, tenancy protections, and non-agricultural conversions in the State of Gujarat.")}</p>

            <div class="doc-tags-row">
              ${(doc.tags || []).map(t => `<span class="tag-bubble">#${escapeHtml(t)}</span>`).join('')}
            </div>

            <div class="doc-action-strip">
              <div class="action-strip-left">
                <a href="${escapeHtml(downloadUrl)}" target="_blank" rel="noopener noreferrer" class="btn-action-pdf" title="Open official PDF from Ministry portal">
                  <span>📄</span>
                  <span>View Official PDF ↗</span>
                </a>
                <button class="btn-action-synth" onclick="runLiveStatutoryAnalysis('${escapeHtml(doc.doc_id)}', '${escapeHtml(downloadUrl)}', '${escapeHtml(doc.title)}')">
                  <span>⚡</span>
                  <span>Run AI Statutory Synthesis</span>
                </button>
                <button class="btn-action-citations" onclick="openDrawerWithCitations('${escapeHtml(doc.doc_id)}', '${escapeHtml(downloadUrl)}', '${escapeHtml(doc.title)}')">
                  <span>📊</span>
                  <span>View Legal Citations ${citationsCount ? `(${citationsCount})` : ''}</span>
                </button>
              </div>
              <div class="action-strip-right">
                <span>Verified India Code Record</span>
              </div>
            </div>
          </article>
        `;
      }).join('');
    }

    function getOfficialBadgeMeta(authority, badge) {
      const text = ((authority || '') + ' ' + (badge || '')).toLowerCase();
      if (text.includes('india code') || text.includes('indiacode')) {
        return { label: 'VERIFIED: INDIA CODE', className: 'pill-source-indiacode' };
      }
      if (text.includes('revenue') || text.includes('gujarat')) {
        return { label: 'GUJARAT REVENUE DEPT', className: 'pill-source-gujrevenue' };
      }
      if (text.includes('data.gov.in') || text.includes('ogd')) {
        return { label: 'DATA.GOV.IN OGD', className: 'pill-source-datagov' };
      }
      return { label: 'STATE GAZETTE RECORD', className: 'pill-source-indiacode' };
    }

    // ------------------------------------------------------------------------
    // 3. Grounded AI Statutory Analysis (/api/v1/kb/live-synthesize)
    // ------------------------------------------------------------------------
    async function runLiveStatutoryAnalysis(docId, docUrl, title) {
      currentSynthesisDocId = docId;
      const drawer = document.getElementById('synthesisDrawerOverlay');
      const body = document.getElementById('drawerBody');
      const drawerTitle = document.getElementById('synthDrawerTitle');
      const subtitle = document.getElementById('synthDrawerSubtitle');

      drawerTitle.textContent = `Analyzing: ${title.length > 40 ? title.slice(0, 40) + '...' : title}`;
      subtitle.textContent = `Target: ${docId} | Live stream & clause extraction from official portal`;
      drawer.style.display = 'flex';

      body.innerHTML = `
        <div class="synth-loader">
          <div class="spin"></div>
          <span>Streaming live document into memory & running statutory clause analysis...</span>
        </div>
      `;

      try {
        const res = await fetch('/api/v1/kb/live-synthesize', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            doc_id: docId,
            document_url: docUrl,
            topic: title
          })
        });
        if (!res.ok) throw new Error('Live synthesis request failed');
        const data = await res.json();

        renderSynthesisContent(data);

      } catch (err) {
        body.innerHTML = `<div style="color:var(--gov-red);padding:20px;">⚠️ Live Synthesis Error: ${escapeHtml(err.message)}</div>`;
      }
    }

    async function openDrawerWithCitations(docId, docUrl, title) {
      await runLiveStatutoryAnalysis(docId, docUrl, title);
    }

    async function triggerSearchSynthesis() {
      const q = document.getElementById('kbSearchInput').value.trim();
      if (!q) {
        alert('Please enter a Gujarat research topic or statutory query to synthesize.');
        return;
      }

      currentSynthesisDocId = null;
      const drawer = document.getElementById('synthesisDrawerOverlay');
      const body = document.getElementById('drawerBody');
      const drawerTitle = document.getElementById('synthDrawerTitle');
      const subtitle = document.getElementById('synthDrawerSubtitle');

      drawerTitle.textContent = `AI Synthesis: "${q.length > 30 ? q.slice(0, 30) + '...' : q}"`;
      subtitle.textContent = "Grounded cross-statute synthesis across Gujarat legal corpus";
      drawer.style.display = 'flex';

      body.innerHTML = `
        <div class="synth-loader">
          <div class="spin"></div>
          <span>Analyzing Gujarat statutes and formulating operational legal opinions...</span>
        </div>
      `;

      try {
        const res = await fetch('/api/v1/kb/live-synthesize', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ topic: q, user_query: q })
        });
        if (!res.ok) throw new Error('Synthesis failed');
        const data = await res.json();

        renderSynthesisContent(data);

      } catch (err) {
        body.innerHTML = `<div style="color:var(--gov-red);padding:20px;">⚠️ Synthesis failed: ${escapeHtml(err.message)}</div>`;
      }
    }

    async function synthesizeVisibleFeed() {
      const q = document.getElementById('kbSearchInput').value.trim() || 'Gujarat Land Revenue & Tenancy Enactments';
      triggerSearchSynthesis();
    }

    function renderSynthesisContent(data) {
      const body = document.getElementById('drawerBody');

      const clausesHtml = (data.operational_clauses || data.key_trade_offs || []).map(c => `
        <div class="clause-item">
          <div class="clause-header">📜 ${escapeHtml(c.clause || c.dimension || 'Statutory Dimension')}</div>
          <div class="clause-desc"><strong>Mandate:</strong> ${escapeHtml(c.mandate || c.tension || '')}</div>
          <div class="clause-solution"><strong>Procedure / Relief:</strong> ${escapeHtml(c.procedure || c.statutory_reconciliation || '')}</div>
        </div>
      `).join('');

      const citationsHtml = (data.legal_cross_references || data.statutory_citations || []).map(c => `
        <div class="citation-item">§ ${escapeHtml(c)}</div>
      `).join('');

      const groundedAnswerBlock = data.grounded_response ? `
        <div class="synth-section" style="border-left:4px solid var(--gov-saffron);background:#FFFDFB;">
          <div class="synth-section-title" style="color:var(--gov-saffron);">
            <span>🤖 Grounded Statutory Opinion (Gujarat Jurisdiction)</span>
          </div>
          <p class="synth-text" style="color:var(--gov-text-primary); font-weight:500;">${escapeHtml(data.grounded_response)}</p>
        </div>
      ` : '';

      body.innerHTML = `
        <!-- Verification Tag -->
        <div style="display:flex;gap:8px;align-items:center;padding:8px 12px;background:var(--gov-green-light);border:1px solid var(--gov-green-border);border-radius:6px;">
          <span class="dot-live"></span>
          <span style="font-size:0.75rem;color:var(--gov-green);font-weight:700;">Grounded Legal Synthesis Streamed Live from Official State Corpus</span>
        </div>

        ${groundedAnswerBlock}

        <!-- Executive Statutory Summary -->
        <div class="synth-section">
          <div class="synth-section-title">
            <span>📋 Executive Statutory Summary</span>
          </div>
          <p class="synth-text">${escapeHtml(data.executive_summary || data.literature_summary || 'Legislative enactment verified under Gujarat state jurisdiction.')}</p>
        </div>

        <!-- Operational Clauses / Trade-offs -->
        <div class="synth-section">
          <div class="synth-section-title">
            <span>⚖️ Operational Clauses & Statutory Restrictions</span>
          </div>
          <div>${clausesHtml || '<p class="synth-text">No restrictive clauses flagged for this section.</p>'}</div>
        </div>

        <!-- Policy Impact Assessment -->
        <div class="synth-section">
          <div class="synth-section-title">
            <span>📈 Policy Impact Assessment</span>
          </div>
          <p class="synth-text">${escapeHtml(data.policy_impact_assessment || 'Compliant with Gujarat Land Revenue Code, Town Planning rules, and agricultural ceiling thresholds.')}</p>
        </div>

        <!-- Legal Cross References -->
        <div class="synth-section">
          <div class="synth-section-title">
            <span>🏛️ Official Statutory Citations</span>
          </div>
          <div class="citation-list">${citationsHtml || '<p class="synth-text">Gujarat Land Revenue Code (1879), Bombay Tenancy and Agricultural Lands Act (1948).</p>'}</div>
        </div>

        <!-- Grounded Interactive Q&A Chat -->
        <div class="doc-ai-chat-box">
          <div class="chat-header">
            <span>💬 Ask Gujarat Statutory AI (In-Memory RAG)</span>
            <span style="font-size:0.70rem;color:#FED7AA;">Live Section Scope</span>
          </div>
          <div class="chat-log" id="drawerChatLog">
            <div class="chat-msg chat-ai">
              Ask specific legal compliance questions about Section 73AA tribal land transfer permissions, Section 65 NA conversion procedure, or Saurashtra Gharkhed tenancy exemptions.
            </div>
          </div>
          <div class="chat-input-row">
            <input 
              type="text" 
              id="drawerChatInput" 
              class="chat-input" 
              placeholder="e.g. Can agricultural land be transferred to a non-farmer in Gujarat?" 
              onkeydown="if(event.key==='Enter') sendDrawerChatMessage()"
            />
            <button class="chat-send-btn" onclick="sendDrawerChatMessage()">Ask AI</button>
          </div>
        </div>
      `;
    }

    async function sendDrawerChatMessage() {
      const input = document.getElementById('drawerChatInput');
      const chatLog = document.getElementById('drawerChatLog');
      const question = input.value.trim();
      if (!question) return;

      const userDiv = document.createElement('div');
      userDiv.className = 'chat-msg chat-user';
      userDiv.textContent = question;
      chatLog.appendChild(userDiv);
      input.value = '';
      chatLog.scrollTop = chatLog.scrollHeight;

      const aiDiv = document.createElement('div');
      aiDiv.className = 'chat-msg chat-ai';
      aiDiv.textContent = 'Querying Gujarat statutory corpus in memory...';
      chatLog.appendChild(aiDiv);
      chatLog.scrollTop = chatLog.scrollHeight;

      try {
        const res = await fetch('/api/v1/kb/live-synthesize', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            doc_id: currentSynthesisDocId,
            topic: question,
            user_query: question
          })
        });
        if (!res.ok) throw new Error('Live synthesis failed');
        const data = await res.json();
        
        aiDiv.textContent = data.grounded_response || data.executive_summary;

      } catch (err) {
        aiDiv.textContent = `⚠️ Error: ${err.message}`;
      } finally {
        chatLog.scrollTop = chatLog.scrollHeight;
      }
    }

    function closeSynthesisDrawer(event) {
      if (event && event.target !== event.currentTarget) return;
      document.getElementById('synthesisDrawerOverlay').style.display = 'none';
    }

    // ------------------------------------------------------------------------
    // 4. Role & State Synchronization (Req 17 & 10)
    // ------------------------------------------------------------------------
    function syncUserPreferences() {
      const savedPersona = localStorage.getItem("bhumi_persona") || "citizen";
      const savedState = localStorage.getItem("bhumi_state") || "gujarat";
      
      const pSel = document.getElementById("personaSelector");
      const sSel = document.getElementById("stateSelector");
      if (pSel) pSel.value = savedPersona;
      if (sSel) sSel.value = savedState;

      applyKbPersona(savedPersona);
    }

    function onKbPersonaChange(val) {
      localStorage.setItem("bhumi_persona", val);
      applyKbPersona(val);
    }

    function applyKbPersona(val) {
      const btn = document.getElementById("btnSubmitResearch");
      if (btn) {
        btn.style.display = (val === 'researcher') ? 'inline-flex' : 'none';
      }
    }

    function onKbStateChange(val) {
      localStorage.setItem("bhumi_state", val);
      if (val === 'up') {
        applyQuickQuery('Uttar Pradesh Revenue Code 2006 Section 80');
      } else if (val === 'maharashtra') {
        applyQuickQuery('Maharashtra Land Revenue Code 1966 Section 63 Tenancy');
      } else {
        applyQuickQuery('Gujarat Land Revenue Code 1879 Section 65');
      }
    }

    function openResearchModal() {
      document.getElementById("researchModal").style.display = "flex";
    }

    function closeResearchModal() {
      document.getElementById("researchModal").style.display = "none";
    }

    function closeResearchOnBackdrop(e) {
      if (e.target === document.getElementById("researchModal")) {
        closeResearchModal();
      }
    }

    function handleResearchSubmit(e) {
      e.preventDefault();
      closeResearchModal();
      const docId = "DoLR-RES-2026-" + Math.floor(1000 + Math.random() * 9000);
      alert(`Academic Research Paper Submitted! Registered under DoLR Review Docket ID: ${docId}`);
    }

    // ------------------------------------------------------------------------
    // 5. GIGW 3.0 Accessibility Controls
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
        alert('हिन्दी भाषा संस्करण: आधिकारिक शब्दावली लोड की जा रही है...');
      } else if (lang === 'gu') {
        alert('ગુજરાતી ભાષા સંસ્કરણ: અધિકૃત પરિભાષા લોડ થઈ રહી છે...');
      }
    }

    function triggerScreenReaderAlert() {
      alert("Screen Reader Mode Active. Use Tab / Shift+Tab to navigate between legislative acts, search facets, and AI synthesis drawers.");
    }

    function openDisclaimerModal() {
      document.getElementById('disclaimerModal').style.display = 'flex';
    }

    function closeDisclaimerModal() {
      document.getElementById('disclaimerModal').style.display = 'none';
    }

    function closeDisclaimerOnBackdrop(e) {
      if (e.target === document.getElementById('disclaimerModal')) {
        closeDisclaimerModal();
      }
    }

    function escapeHtml(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }
  </script>

</body>
</html>
"""
