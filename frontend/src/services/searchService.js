/**
 * High-Precision Geospatial Search & Boundary Resolution Service
 * Handles locality geocoding with exact polygon extraction, bbox synthesis,
 * intelligent multi-tier ranking, and dual backend/OSM fallback.
 */

const BACKEND_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

/**
 * Calculates geodesic bounding area in square kilometers and hectares
 */
export function calculateBBoxArea(bbox) {
  if (!bbox || bbox.length < 4) return { areaSqKm: 0, areaHectares: 0 };
  const [minLon, minLat, maxLon, maxLat] = bbox;
  const midLatRad = ((minLat + maxLat) / 2.0) * (Math.PI / 180);
  const widthKm = Math.abs(maxLon - minLon) * 111.32 * Math.cos(midLatRad);
  const heightKm = Math.abs(maxLat - minLat) * 110.57;
  const areaSqKm = Math.round(widthKm * heightKm * 100) / 100;
  const areaHectares = Math.round(areaSqKm * 100 * 10) / 10;
  return { areaSqKm, areaHectares };
}

/**
 * Synthesizes a closed GeoJSON Polygon from a bounding box array [minLon, minLat, maxLon, maxLat]
 */
export function bboxToPolygonGeometry(bbox) {
  const [minLon, minLat, maxLon, maxLat] = bbox;
  return {
    type: 'Polygon',
    coordinates: [[
      [minLon, minLat],
      [maxLon, minLat],
      [maxLon, maxLat],
      [minLon, maxLat],
      [minLon, minLat]
    ]]
  };
}

/**
 * Client-Side Nominatim Fallback Parser
 * Applies the exact ranking, locality filtering, and boundary construction
 */
async function searchNominatimDirect(query) {
  const params = new URLSearchParams({
    q: query.trim(),
    countrycodes: 'in',
    format: 'jsonv2',
    addressdetails: '1',
    extratags: '1',
    polygon_geojson: '1',
    limit: '10'
  });

  const resp = await fetch(`https://nominatim.openstreetmap.org/search?${params.toString()}`, {
    headers: {
      'Accept': 'application/json'
    }
  });

  if (!resp.ok) return [];
  const items = await resp.json();
  const qLower = query.toLowerCase().trim();
  const scored = [];

  for (const it of items) {
    const addr = it.address || {};
    const osmId = String(it.osm_id || '');
    const rawCat = (it.addresstype || it.type || '').toLowerCase();
    const osmClass = (it.class || '').toLowerCase();

    // Prioritize explicit OSM name tag first
    const rawName = (it.name || '').trim();
    const primaryName = (
      rawName ||
      addr.suburb ||
      addr.neighbourhood ||
      addr.quarter ||
      addr.village ||
      addr.town ||
      addr.city ||
      addr.hamlet ||
      addr.residential ||
      (it.display_name || '').split(',')[0].trim()
    );

    // Categorization
    let cat = 'locality';
    if (
      ['suburb', 'neighbourhood', 'neighborhood', 'quarter', 'residential', 'locality'].includes(rawCat) ||
      addr.suburb || addr.neighbourhood
    ) {
      cat = 'suburb';
    } else if (['village', 'hamlet'].includes(rawCat) || addr.village || addr.hamlet) {
      cat = 'village';
    } else if (['postcode', 'postal_code'].includes(rawCat) || (/^\d{6}$/.test(query.trim()))) {
      cat = 'pincode';
    } else if (rawCat === 'town' || addr.town) {
      cat = 'town';
    } else if (['city', 'municipality'].includes(rawCat) || addr.city) {
      cat = 'city';
    } else if (['district', 'county'].includes(rawCat) || addr.state_district) {
      cat = 'district';
    } else {
      cat = rawCat || 'locality';
    }

    const district = addr.state_district || addr.county || addr.city || '';
    const state = addr.state || 'India';
    const dispParts = (it.display_name || '').split(',').map(s => s.trim());
    const subText = dispParts.length > 2 ? dispParts.slice(1, 3).join(', ') : `${district}, ${state}`;
    const subtitle = `${subText} • ${cat.charAt(0).toUpperCase() + cat.slice(1)}`;

    // Geometry resolution
    const geo = it.geojson;
    const bb = it.boundingbox;
    let geometry = null;
    let bbox = null;
    let hasPolygon = false;

    if (geo && (geo.type === 'Polygon' || geo.type === 'MultiPolygon') && geo.coordinates?.length > 0) {
      geometry = geo;
      hasPolygon = true;
      if (bb && bb.length === 4) {
        bbox = [parseFloat(bb[2]), parseFloat(bb[0]), parseFloat(bb[3]), parseFloat(bb[1])];
      }
    } else if (bb && bb.length === 4) {
      let minLat = parseFloat(bb[0]);
      let maxLat = parseFloat(bb[1]);
      let minLon = parseFloat(bb[2]);
      let maxLon = parseFloat(bb[3]);
      if (minLat === maxLat) { minLat -= 0.008; maxLat += 0.008; }
      if (minLon === maxLon) { minLon -= 0.008; maxLon += 0.008; }
      bbox = [minLon, minLat, maxLon, maxLat];
      geometry = bboxToPolygonGeometry(bbox);
    } else {
      const lat = parseFloat(it.lat || 20.59);
      const lon = parseFloat(it.lon || 78.96);
      const d = 0.012;
      bbox = [lon - d, lat - d, lon + d, lat + d];
      geometry = bboxToPolygonGeometry(bbox);
    }

    const { areaSqKm, areaHectares } = calculateBBoxArea(bbox);
    const entityId = osmId ? `osm-${osmId}` : `osm-${primaryName.toLowerCase().replace(/\s+/g, '-')}`;

    // Scoring
    const nameLower = primaryName.toLowerCase();
    let score = 0;
    if (nameLower === qLower) {
      score += 150;
    } else if (nameLower.startsWith(qLower)) {
      score += 100;
    } else if (nameLower.includes(qLower)) {
      score += 60;
    } else {
      score += 20;
    }

    if (['suburb', 'neighbourhood', 'quarter', 'locality'].includes(cat)) {
      score += 50;
    } else if (['village', 'hamlet'].includes(cat)) {
      score += 45;
    } else if (cat === 'pincode') {
      score += 40;
    } else if (['town', 'city'].includes(cat)) {
      score += 20;
    }

    if (hasPolygon) {
      score += 25;
    }

    if (['railway', 'highway', 'transportation'].includes(osmClass) || ['station', 'halt', 'stop', 'bus_stop'].includes(rawCat)) {
      if (!qLower.includes('station') && !qLower.includes('railway')) {
        score -= 50;
      }
    }

    scored.push({
      score,
      item: {
        id: entityId,
        title: primaryName,
        subtitle,
        type: cat,
        bbox,
        lat: parseFloat(it.lat || ((bbox[1] + bbox[3]) / 2)),
        lon: parseFloat(it.lon || ((bbox[0] + bbox[2]) / 2)),
        district,
        state,
        area_sq_km: areaSqKm,
        area_hectares: areaHectares,
        geometry,
        osm_id: osmId
      }
    });
  }

  scored.sort((a, b) => b.score - a.score);

  // Deduplicate
  const seen = new Set();
  const results = [];
  for (const entry of scored) {
    const key = `${entry.item.title.toLowerCase()}::${entry.item.type}`;
    if (!seen.has(key)) {
      seen.add(key);
      results.push(entry.item);
    }
  }

  return results.slice(0, 10);
}

export const searchService = {
  /**
   * Omni-search for Indian localities, suburbs, villages, towns, PIN codes
   * Attempts FastAPI backend first, then falls back to direct client-side OSM query.
   */
  async searchPlaces(query) {
    if (!query || !query.trim() || query.trim().length < 2) {
      return [];
    }

    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 3500);

      const res = await fetch(
        `${BACKEND_BASE_URL}/api/v1/gis/search?q=${encodeURIComponent(query.trim())}`,
        { signal: controller.signal }
      );
      clearTimeout(timeoutId);

      if (res.ok) {
        const data = await res.json();
        if (Array.isArray(data) && data.length > 0) {
          return data;
        }
      }
    } catch {
      // Backend unreachable or timed out, fallback gracefully
    }

    // Direct Nominatim Client-Side Fallback
    try {
      return await searchNominatimDirect(query);
    } catch (err) {
      console.error('Direct Nominatim search failed:', err);
      return [];
    }
  },

  /**
   * Resolves the full GeoJSON Boundary Feature for an entity.
   * If geometry already exists on the entity object, returns it immediately.
   */
  async getBoundary(entity) {
    if (!entity) return null;

    // Check if the entity already contains full geometry & bbox
    if (entity.geometry && entity.bbox) {
      return {
        type: 'Feature',
        id: entity.id,
        properties: {
          name: entity.title,
          type: entity.type,
          district: entity.district,
          state: entity.state,
          area_sq_km: entity.area_sq_km,
          area_hectares: entity.area_hectares,
          lat: entity.lat,
          lon: entity.lon
        },
        geometry: entity.geometry,
        bbox: entity.bbox
      };
    }

    // Attempt Backend API
    try {
      const res = await fetch(
        `${BACKEND_BASE_URL}/api/v1/gis/boundary?type=${encodeURIComponent(entity.type || 'locality')}&id=${encodeURIComponent(entity.id)}`,
        { signal: AbortSignal.timeout(3000) }
      );
      if (res.ok) {
        const boundaryFeature = await res.json();
        return boundaryFeature;
      }
    } catch {
      // Fallback
    }

    // Fallback: Synthesize from bbox if available
    if (entity.bbox && entity.bbox.length === 4) {
      return {
        type: 'Feature',
        id: entity.id,
        properties: {
          name: entity.title,
          type: entity.type,
          district: entity.district,
          state: entity.state,
          area_sq_km: entity.area_sq_km,
          area_hectares: entity.area_hectares
        },
        geometry: bboxToPolygonGeometry(entity.bbox),
        bbox: entity.bbox
      };
    }

    // Fallback from coordinates
    if (entity.lat && entity.lon) {
      const d = 0.015;
      const bbox = [entity.lon - d, entity.lat - d, entity.lon + d, entity.lat + d];
      return {
        type: 'Feature',
        id: entity.id,
        properties: {
          name: entity.title,
          type: entity.type,
          district: entity.district,
          state: entity.state,
          area_sq_km: entity.area_sq_km || 4.2,
          area_hectares: entity.area_hectares || 420.0
        },
        geometry: bboxToPolygonGeometry(bbox),
        bbox
      };
    }

    return null;
  }
};
