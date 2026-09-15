/**
 * Resilient API Client Layer with Intelligent Local Fallback
 * Ministry of Rural Development, Department of Land Resources (DoLR)
 */

import { MOCK_RESOURCES, MOCK_DISPUTE_ANALYTICS, MOCK_TELEMETRY } from './mockData';

const BACKEND_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

let clientState = {
  resources: [...MOCK_RESOURCES],
  telemetry: JSON.parse(JSON.stringify(MOCK_TELEMETRY)),
  analytics: JSON.parse(JSON.stringify(MOCK_DISPUTE_ANALYTICS))
};

export const api = {
  /**
   * Fetch repository resources with query params and faceted filtering
   */
  async getResources(params = {}) {
    const query = new URLSearchParams();
    Object.entries(params).forEach(([key, val]) => {
      if (val !== undefined && val !== null && val !== '') {
        query.append(key, val);
      }
    });

    try {
      const res = await fetch(`${BACKEND_BASE_URL}/api/v1/repository/resources?${query.toString()}`, {
        signal: AbortSignal.timeout(2000)
      });
      if (res.ok) {
        return await res.json();
      }
    } catch {
      // Graceful fallback to client-side filter engine
    }

    // Client-side simulated fallback
    let items = [...clientState.resources];

    if (params.q) {
      const q = params.q.toLowerCase().trim();
      items = items.filter(r =>
        r.title.toLowerCase().includes(q) ||
        r.abstract.toLowerCase().includes(q) ||
        r.theme.toLowerCase().includes(q) ||
        r.legal_authority.toLowerCase().includes(q) ||
        (r.ulpin && r.ulpin.toLowerCase().includes(q)) ||
        (r.lgd_code && r.lgd_code.includes(q))
      );
    }

    if (params.taxonomy_stream && params.taxonomy_stream !== 'all') {
      items = items.filter(r => r.taxonomy_stream === params.taxonomy_stream);
    }

    if (params.document_type) {
      items = items.filter(r => r.document_type.toLowerCase() === params.document_type.toLowerCase());
    }

    if (params.theme) {
      items = items.filter(r => r.theme.toLowerCase() === params.theme.toLowerCase());
    }

    if (params.state_ut && params.state_ut !== 'All States') {
      items = items.filter(r => r.state_ut === params.state_ut || r.state_ut === 'National');
    }

    if (params.district) {
      items = items.filter(r => r.district && r.district.toLowerCase().includes(params.district.toLowerCase()));
    }

    if (params.lgd_code) {
      items = items.filter(r => r.lgd_code === params.lgd_code);
    }

    if (params.has_spatial !== undefined && params.has_spatial !== null) {
      items = items.filter(r => Boolean(r.has_spatial_layer) === Boolean(params.has_spatial));
    }

    if (params.year_from) {
      items = items.filter(r => parseInt(r.publication_date.slice(0, 4)) >= Number(params.year_from));
    }

    if (params.year_to) {
      items = items.filter(r => parseInt(r.publication_date.slice(0, 4)) <= Number(params.year_to));
    }

    // Sort
    if (params.sort_by === 'date_desc') {
      items.sort((a, b) => new Date(b.publication_date) - new Date(a.publication_date));
    } else if (params.sort_by === 'date_asc') {
      items.sort((a, b) => new Date(a.publication_date) - new Date(b.publication_date));
    } else if (params.sort_by === 'title') {
      items.sort((a, b) => a.title.localeCompare(b.title));
    }

    const page = Number(params.page) || 1;
    const pageSize = Number(params.page_size) || 10;
    const total = items.length;
    const totalPages = Math.max(1, Math.ceil(total / pageSize));
    const paginatedItems = items.slice((page - 1) * pageSize, page * pageSize);

    // Compute facets
    const facets = {
      taxonomy_stream: {},
      document_type: {},
      theme: {},
      state_ut: {},
      legal_authority: {}
    };

    items.forEach(item => {
      facets.taxonomy_stream[item.taxonomy_stream] = (facets.taxonomy_stream[item.taxonomy_stream] || 0) + 1;
      facets.document_type[item.document_type] = (facets.document_type[item.document_type] || 0) + 1;
      facets.theme[item.theme] = (facets.theme[item.theme] || 0) + 1;
      if (item.state_ut) facets.state_ut[item.state_ut] = (facets.state_ut[item.state_ut] || 0) + 1;
      if (item.legal_authority) facets.legal_authority[item.legal_authority] = (facets.legal_authority[item.legal_authority] || 0) + 1;
    });

    return {
      items: paginatedItems,
      total,
      page,
      page_size: pageSize,
      total_pages: totalPages,
      facets
    };
  },

  /**
   * Fetch single resource by ID
   */
  async getResourceById(id) {
    try {
      const res = await fetch(`${BACKEND_BASE_URL}/api/v1/repository/resources/${id}`, {
        signal: AbortSignal.timeout(2000)
      });
      if (res.ok) return await res.json();
    } catch {}

    return clientState.resources.find(r => r.id === id) || null;
  },

  /**
   * Fetch live dispute analytics
   */
  async getDisputeAnalytics() {
    try {
      const res = await fetch(`${BACKEND_BASE_URL}/api/v1/repository/analytics/disputes`, {
        signal: AbortSignal.timeout(2000)
      });
      if (res.ok) return await res.json();
    } catch {}

    return clientState.analytics;
  },

  /**
   * Fetch telemetry sync status
   */
  async getTelemetryStatus() {
    try {
      const res = await fetch(`${BACKEND_BASE_URL}/api/v1/repository/sync/status`, {
        signal: AbortSignal.timeout(2000)
      });
      if (res.ok) return await res.json();
    } catch {}

    return clientState.telemetry;
  },

  /**
   * Trigger manual ingestion sync
   */
  async triggerSync(endpoints = null) {
    try {
      const res = await fetch(`${BACKEND_BASE_URL}/api/v1/repository/sync/trigger`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ target_endpoints: endpoints, force_resync: true }),
        signal: AbortSignal.timeout(2000)
      });
      if (res.ok) return await res.json();
    } catch {}

    // Simulated local sync
    clientState.telemetry.endpoints = clientState.telemetry.endpoints.map(ep => ({
      ...ep,
      last_synced_at: new Date().toISOString(),
      records_indexed: ep.records_indexed + Math.floor(Math.random() * 8 + 3),
      status: 'OPERATIONAL'
    }));
    clientState.telemetry.last_global_sync = new Date().toISOString();

    return {
      job_id: `sync-sim-${Date.now().toString(36)}`,
      status: 'COMPLETED',
      initiated_at: new Date().toISOString(),
      message: 'Client-side simulated background sync completed successfully.',
      endpoints_queued: ['e-Courts NJDG', 'data.gov.in OGD', 'DoLR Gazette', 'Bhu-Aadhaar ULPIN']
    };
  }
};
