import React, { useState, useEffect, useRef } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import {
  Search,
  X,
  MapPin,
  Sliders,
  Layers,
  ChevronRight,
  Compass,
  Maximize2,
  Info,
  Check,
  Eye,
  EyeOff
} from 'lucide-react';
import { searchService } from '../services/searchService';

// ESRI 10m LULC 2020 Classes definition for the thematic legend
const LULC_CLASSES = [
  { name: 'Built Area', color: '#ea9999' },
  { name: 'Crops', color: '#ffd966' },
  { name: 'Trees', color: '#38761d' },
  { name: 'Water', color: '#004da8' },
  { name: 'Rangeland', color: '#e69138' },
  { name: 'Flooded Veg', color: '#00a884' },
  { name: 'Bare Ground', color: '#a64d79' },
  { name: 'Snow/Ice', color: '#d9d9d9' }
];

export default function GISMap() {
  const mapContainerRef = useRef(null);
  const mapInstanceRef = useRef(null);

  // Layer references stored on ref to persist across re-renders
  const layersRef = useRef({
    satellite: null,
    lulc: null,
    boundary: null
  });

  // State: Search & Autocomplete
  const [searchQuery, setSearchQuery] = useState('');
  const [isSearching, setIsSearching] = useState(false);
  const [suggestions, setSuggestions] = useState([]);
  const [showDropdown, setShowDropdown] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState(-1);
  const debounceTimerRef = useRef(null);
  const searchInputRef = useRef(null);

  // State: Selected Entity & Minimal Info Drawer
  const [selectedEntity, setSelectedEntity] = useState(null);
  const [isDrawerOpen, setIsDrawerOpen] = useState(false);

  // State: LULC Control
  const [lulcOpacity, setLulcOpacity] = useState(0.25); // Exactly 25% default
  const [isLulcVisible, setIsLulcVisible] = useState(true);
  const [showLegend, setShowLegend] = useState(false);

  // 1. Initialize Strict 3-Layer Leaflet Map
  useEffect(() => {
    if (!mapContainerRef.current || mapInstanceRef.current) return;

    // Centered on India [lat: 20.5937, lon: 78.9629], zoom 5
    const map = L.map(mapContainerRef.current, {
      center: [20.5937, 78.9629],
      zoom: 5,
      minZoom: 3,
      maxZoom: 19,
      zoomControl: false
    });

    L.control.zoom({ position: 'bottomright' }).addTo(map);

    // Layer 1: Base Layer - ESRI World Imagery (Satellite)
    const satelliteLayer = L.tileLayer(
      'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
      {
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
        maxZoom: 19,
        crossOrigin: true
      }
    ).addTo(map);
    layersRef.current.satellite = satelliteLayer;

    // Layer 2: Thematic Overlay - ESRI Sentinel-2 10m Land Cover V2 (Fixed 25% default opacity)
    const lulcLayer = L.tileLayer(
      'https://tiles.arcgis.com/tiles/P3ePLMYs2RVChkJx/arcgis/rest/services/Esri_2020_Land_Cover_V2/MapServer/tile/{z}/{y}/{x}',
      {
        attribution: 'Esri 2020 Land Cover &copy; Impact Observatory &amp; Esri Living Atlas',
        opacity: 0.25,
        maxZoom: 19,
        crossOrigin: true
      }
    ).addTo(map);
    layersRef.current.lulc = lulcLayer;

    // Layer 3: Dynamic Searched Location Boundary Layer
    const boundaryLayerGroup = L.layerGroup().addTo(map);
    layersRef.current.boundary = boundaryLayerGroup;

    mapInstanceRef.current = map;

    // Viewport layout fix
    const timer1 = setTimeout(() => map.invalidateSize(), 150);
    const timer2 = setTimeout(() => map.invalidateSize(), 500);

    let resizeObserver = null;
    if (typeof ResizeObserver !== 'undefined' && mapContainerRef.current) {
      resizeObserver = new ResizeObserver(() => {
        map.invalidateSize();
      });
      resizeObserver.observe(mapContainerRef.current);
    }

    return () => {
      clearTimeout(timer1);
      clearTimeout(timer2);
      if (resizeObserver) resizeObserver.disconnect();
      map.remove();
      mapInstanceRef.current = null;
    };
  }, []);

  // 2. Synchronize LULC Opacity & Visibility
  useEffect(() => {
    if (!layersRef.current.lulc || !mapInstanceRef.current) return;
    const lulc = layersRef.current.lulc;
    if (isLulcVisible) {
      if (!mapInstanceRef.current.hasLayer(lulc)) {
        lulc.addTo(mapInstanceRef.current);
      }
      lulc.setOpacity(lulcOpacity);
    } else {
      if (mapInstanceRef.current.hasLayer(lulc)) {
        mapInstanceRef.current.removeLayer(lulc);
      }
    }
  }, [lulcOpacity, isLulcVisible]);

  // 3. Debounced Search Autocomplete (300ms)
  useEffect(() => {
    if (!searchQuery.trim() || searchQuery.trim().length < 2) {
      setSuggestions([]);
      setShowDropdown(false);
      setIsSearching(false);
      return;
    }

    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
    }

    debounceTimerRef.current = setTimeout(async () => {
      setIsSearching(true);
      try {
        const results = await searchService.searchPlaces(searchQuery);
        setSuggestions(results);
        setShowDropdown(results.length > 0);
        setSelectedIndex(-1);
      } catch (err) {
        console.error('Search error:', err);
      } finally {
        setIsSearching(false);
      }
    }, 300);

    return () => {
      if (debounceTimerRef.current) clearTimeout(debounceTimerRef.current);
    };
  }, [searchQuery]);

  // 4. Keyboard Navigation in Search Dropdown
  const handleKeyDown = (e) => {
    if (!showDropdown || suggestions.length === 0) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev < suggestions.length - 1 ? prev + 1 : 0));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev > 0 ? prev - 1 : suggestions.length - 1));
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (selectedIndex >= 0 && selectedIndex < suggestions.length) {
        handleSelectLocation(suggestions[selectedIndex]);
      } else if (suggestions.length > 0) {
        handleSelectLocation(suggestions[0]);
      }
    } else if (e.key === 'Escape') {
      setShowDropdown(false);
    }
  };

  // 5. Location Selection & Exact Boundary Resolution
  const handleSelectLocation = async (item) => {
    setShowDropdown(false);
    setSearchQuery(item.title);
    setSelectedEntity(item);
    setIsDrawerOpen(true);

    try {
      const boundaryFeature = await searchService.getBoundary(item);

      if (layersRef.current.boundary) {
        layersRef.current.boundary.clearLayers();

        if (boundaryFeature && boundaryFeature.geometry) {
          // Clean glowing cyan/electric blue vector outline
          // Fill: #38bdf8 with 0.12 opacity
          // Outline: #0284c7 with line-width 2.5
          const geoLayer = L.geoJSON(boundaryFeature, {
            style: {
              color: '#0284c7',
              weight: 2.5,
              opacity: 0.95,
              fillColor: '#38bdf8',
              fillOpacity: 0.12,
              dashArray: '0'
            },
            onEachFeature: (f, layer) => {
              layer.bindTooltip(`
                <div class="font-sans text-xs bg-slate-950 text-white p-2 rounded-md shadow-2xl border border-sky-500/80">
                  <div class="text-[10px] uppercase font-bold text-sky-400 tracking-wider">Searched Location</div>
                  <div class="text-sm font-semibold text-white leading-tight mt-0.5">${item.title}</div>
                  <div class="text-[11px] text-slate-300 mt-1">${item.subtitle}</div>
                </div>
              `, { sticky: true, className: 'clean-gis-tooltip' });
            }
          });

          layersRef.current.boundary.addLayer(geoLayer);

          // Smooth fitBounds transition to exact boundary
          if (mapInstanceRef.current) {
            const bbox = boundaryFeature.bbox || item.bbox;
            if (bbox && bbox.length === 4) {
              const [minLon, minLat, maxLon, maxLat] = bbox;
              mapInstanceRef.current.fitBounds(
                [
                  [minLat, minLon],
                  [maxLat, maxLon]
                ],
                {
                  padding: [60, 60],
                  maxZoom: 15,
                  animate: true,
                  duration: 1.2
                }
              );
            } else if (item.lat && item.lon) {
              mapInstanceRef.current.flyTo([item.lat, item.lon], 14, { duration: 1.2 });
            }
          }
        }
      }
    } catch (err) {
      console.error('Failed to render location boundary:', err);
    }
  };

  // 6. Reset / Clear Search
  const handleClear = () => {
    setSearchQuery('');
    setSuggestions([]);
    setShowDropdown(false);
    setSelectedEntity(null);
    setIsDrawerOpen(false);

    if (layersRef.current.boundary) {
      layersRef.current.boundary.clearLayers();
    }

    if (mapInstanceRef.current) {
      mapInstanceRef.current.flyTo([20.5937, 78.9629], 5, { duration: 1.2 });
    }
  };

  // Helper: Badge styling for categories
  const getBadgeClass = (type) => {
    switch (type?.toLowerCase()) {
      case 'suburb':
      case 'neighbourhood':
      case 'locality':
        return 'bg-sky-500/20 text-sky-300 border-sky-500/40';
      case 'village':
      case 'hamlet':
        return 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40';
      case 'pincode':
        return 'bg-amber-500/20 text-amber-300 border-amber-500/40';
      case 'city':
      case 'town':
        return 'bg-purple-500/20 text-purple-300 border-purple-500/40';
      default:
        return 'bg-slate-700/50 text-slate-300 border-slate-600';
    }
  };

  return (
    <div className="relative w-full h-full overflow-hidden bg-slate-950 font-sans select-none">
      {/* 1. MAP CANVAS (Strict 3 Layers) */}
      <div ref={mapContainerRef} className="w-full h-full z-0 cursor-grab active:cursor-grabbing" />

      {/* 2. TOP-LEFT FLOATING SEARCH BAR & AUTOCOMPLETE */}
      <div className="absolute top-4 left-4 z-30 w-full max-w-md">
        <div className="relative bg-slate-900/90 backdrop-blur-md rounded-xl shadow-2xl border border-slate-700/80 transition-all duration-200 focus-within:border-sky-500 focus-within:ring-2 focus-within:ring-sky-500/30">
          <div className="flex items-center px-3.5 py-2.5">
            <Search className="w-4 h-4 text-sky-400 shrink-0 mr-2.5" />
            <input
              ref={searchInputRef}
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              onFocus={() => {
                if (suggestions.length > 0) setShowDropdown(true);
              }}
              placeholder="Search Indian locality, suburb, village, PIN code..."
              className="w-full bg-transparent text-sm text-slate-100 placeholder-slate-400 focus:outline-hidden font-medium"
            />
            {isSearching && (
              <div className="w-4 h-4 border-2 border-sky-400 border-t-transparent rounded-full animate-spin shrink-0 mx-1.5" />
            )}
            {searchQuery && (
              <button
                onClick={handleClear}
                className="p-1 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition cursor-pointer"
                title="Clear Search"
              >
                <X className="w-4 h-4" />
              </button>
            )}
          </div>

          {/* Autocomplete Suggestions Dropdown */}
          {showDropdown && suggestions.length > 0 && (
            <div className="border-t border-slate-800 max-h-80 overflow-y-auto divide-y divide-slate-800/60 rounded-b-xl">
              {suggestions.map((item, idx) => (
                <div
                  key={item.id || idx}
                  onClick={() => handleSelectLocation(item)}
                  onMouseEnter={() => setSelectedIndex(idx)}
                  className={`px-3.5 py-2.5 flex items-start justify-between gap-3 cursor-pointer transition ${
                    selectedIndex === idx ? 'bg-sky-950/60 text-white' : 'hover:bg-slate-800/60 text-slate-200'
                  }`}
                >
                  <div className="flex items-start gap-2.5 min-w-0">
                    <MapPin className="w-4 h-4 text-sky-400 shrink-0 mt-0.5" />
                    <div className="min-w-0">
                      <div className="text-sm font-semibold truncate text-slate-100">{item.title}</div>
                      <div className="text-xs text-slate-400 truncate mt-0.5">{item.subtitle}</div>
                    </div>
                  </div>
                  <span
                    className={`text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full border shrink-0 ${getBadgeClass(
                      item.type
                    )}`}
                  >
                    {item.type}
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* 3. TOP-RIGHT THEMATIC LULC CONTROLLER */}
      <div className="absolute top-4 right-16 z-30">
        <div className="bg-slate-900/90 backdrop-blur-md p-2.5 rounded-xl shadow-2xl border border-slate-700/80 flex flex-col gap-2.5 min-w-[240px]">
          <div className="flex items-center justify-between text-xs">
            <div className="flex items-center gap-1.5 font-semibold text-slate-200">
              <Layers className="w-3.5 h-3.5 text-emerald-400" />
              <span>ESRI Sentinel-2 LULC</span>
            </div>
            <button
              onClick={() => setIsLulcVisible(!isLulcVisible)}
              className={`p-1 rounded-md transition cursor-pointer ${
                isLulcVisible ? 'text-emerald-400 hover:bg-slate-800' : 'text-slate-500 hover:bg-slate-800'
              }`}
              title={isLulcVisible ? 'Hide LULC Overlay' : 'Show LULC Overlay'}
            >
              {isLulcVisible ? <Eye className="w-4 h-4" /> : <EyeOff className="w-4 h-4" />}
            </button>
          </div>

          {/* Opacity Slider */}
          <div className="flex items-center gap-2">
            <input
              type="range"
              min="0"
              max="1"
              step="0.01"
              value={lulcOpacity}
              disabled={!isLulcVisible}
              onChange={(e) => setLulcOpacity(parseFloat(e.target.value))}
              className="w-full h-1.5 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-emerald-400 disabled:opacity-40"
            />
            <span className="text-xs font-mono font-medium text-slate-300 w-10 text-right">
              {Math.round(lulcOpacity * 100)}%
            </span>
          </div>

          {/* Legend Toggle Button */}
          <button
            onClick={() => setShowLegend(!showLegend)}
            className="flex items-center justify-between text-[11px] text-slate-400 hover:text-slate-200 pt-1 border-t border-slate-800 cursor-pointer"
          >
            <span>Land Cover Legend</span>
            <span className="text-emerald-400 font-bold">{showLegend ? 'Hide' : 'Show'}</span>
          </button>

          {/* Collapsible Legend Grid */}
          {showLegend && (
            <div className="grid grid-cols-2 gap-1.5 pt-1.5 border-t border-slate-800/60">
              {LULC_CLASSES.map((cls) => (
                <div key={cls.name} className="flex items-center gap-1.5 text-[10px] text-slate-300">
                  <span
                    className="w-2.5 h-2.5 rounded-xs shrink-0 border border-black/40"
                    style={{ backgroundColor: cls.color }}
                  />
                  <span className="truncate">{cls.name}</span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* 4. MINIMAL RIGHT-SIDE INFO DRAWER (Locality Entity Card) */}
      {isDrawerOpen && selectedEntity && (
        <div className="absolute top-20 right-4 z-30 w-80 bg-slate-900/95 backdrop-blur-md rounded-2xl shadow-2xl border border-slate-700/80 overflow-hidden transition-all duration-300 animate-in fade-in slide-in-from-right-4">
          {/* Header */}
          <div className="p-4 border-b border-slate-800 flex items-start justify-between gap-2 bg-gradient-to-r from-sky-950/40 to-transparent">
            <div className="min-w-0">
              <span
                className={`text-[9px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full border inline-block mb-1.5 ${getBadgeClass(
                  selectedEntity.type
                )}`}
              >
                {selectedEntity.type}
              </span>
              <h3 className="text-base font-bold text-white leading-tight truncate">{selectedEntity.title}</h3>
              <p className="text-xs text-slate-400 truncate mt-0.5">{selectedEntity.subtitle}</p>
            </div>
            <button
              onClick={() => setIsDrawerOpen(false)}
              className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition cursor-pointer"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* Body Attributes */}
          <div className="p-4 space-y-3.5 text-xs text-slate-300">
            {/* Coordinates */}
            <div className="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/80 flex items-center justify-between">
              <div>
                <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Coordinates</div>
                <div className="font-mono text-slate-200 mt-0.5">
                  {selectedEntity.lat?.toFixed(5)}° N, {selectedEntity.lon?.toFixed(5)}° E
                </div>
              </div>
              <Compass className="w-4 h-4 text-sky-400 shrink-0" />
            </div>

            {/* Jurisdiction Hierarchy */}
            <div className="grid grid-cols-2 gap-2">
              <div className="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/80">
                <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">District / Taluka</div>
                <div className="font-semibold text-slate-200 truncate mt-0.5">
                  {selectedEntity.district || 'Localized'}
                </div>
              </div>

              <div className="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/80">
                <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">State</div>
                <div className="font-semibold text-slate-200 truncate mt-0.5">
                  {selectedEntity.state || 'India'}
                </div>
              </div>
            </div>

            {/* Bounding Dimensions & Area */}
            <div className="bg-slate-950/60 p-2.5 rounded-xl border border-slate-800/80">
              <div className="flex items-center justify-between">
                <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Estimated Area</div>
                <span className="text-[10px] text-sky-400 font-medium">Exact Bounding Polygon</span>
              </div>
              <div className="flex items-baseline gap-2 mt-1">
                <span className="text-lg font-bold text-white font-mono">
                  {selectedEntity.area_sq_km || 0}
                </span>
                <span className="text-slate-400 text-xs">km²</span>
                <span className="text-slate-600">•</span>
                <span className="text-sm font-semibold text-slate-300 font-mono">
                  {selectedEntity.area_hectares || 0}
                </span>
                <span className="text-slate-400 text-xs">ha</span>
              </div>
            </div>

            {/* Re-center / Focus Action */}
            <button
              onClick={() => {
                if (mapInstanceRef.current && selectedEntity.bbox) {
                  const [minLon, minLat, maxLon, maxLat] = selectedEntity.bbox;
                  mapInstanceRef.current.fitBounds(
                    [
                      [minLat, minLon],
                      [maxLat, maxLon]
                    ],
                    { padding: [60, 60], maxZoom: 15, animate: true, duration: 1.0 }
                  );
                }
              }}
              className="w-full flex items-center justify-center gap-2 py-2 px-3 bg-sky-600 hover:bg-sky-500 text-white font-semibold rounded-xl shadow-lg shadow-sky-600/20 transition cursor-pointer"
            >
              <Maximize2 className="w-3.5 h-3.5" />
              <span>Center on Boundary</span>
            </button>
          </div>
        </div>
      )}

      {/* 5. MINIMAL BOTTOM-LEFT BRANDING CHIP */}
      <div className="absolute bottom-3 left-4 z-20 pointer-events-none">
        <div className="flex items-center gap-2 bg-slate-900/80 backdrop-blur-sm px-3 py-1.5 rounded-lg border border-slate-800 text-[11px] text-slate-400 shadow-md">
          <span className="w-2 h-2 rounded-full bg-sky-400 animate-pulse" />
          <span className="font-semibold text-slate-300">Clean GIS Canvas</span>
          <span>•</span>
          <span>ESRI World Imagery + 10m LULC</span>
        </div>
      </div>
    </div>
  );
}
