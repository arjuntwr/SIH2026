import React, { useState, useEffect, useRef } from 'react';
import {
  Search,
  MapPin,
  Building2,
  Wheat,
  Mail,
  X,
  ChevronRight,
  FileText,
  Scale,
  ShieldCheck,
  AlertTriangle,
  Zap,
  Users,
  GraduationCap,
  Trees,
  Droplets,
  Layers,
  Copy,
  Check,
  Download,
  ExternalLink,
  Sliders,
  Compass,
  CheckCircle2,
  Clock
} from 'lucide-react';

const BACKEND_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function GISSearchAndInspect({
  mapInstance,
  onSelectEntity,
  onClearSearch,
  onViewPdf
}) {
  // Search State
  const [searchQuery, setSearchQuery] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [isSearching, setIsSearching] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState(-1);
  const [showDropdown, setShowDropdown] = useState(false);
  const [activeEntity, setActiveEntity] = useState(null);

  // Inspector State
  const [activeTab, setActiveTab] = useState('demographics'); // 'demographics' | 'disputes' | 'lulc' | 'cadastre'
  const [metrics, setMetrics] = useState(null);
  const [loadingMetrics, setLoadingMetrics] = useState(false);
  const [isInspectorOpen, setIsInspectorOpen] = useState(false);
  const [copiedCitation, setCopiedCitation] = useState(false);

  // Search input ref & debounce timer
  const searchInputRef = useRef(null);
  const debounceTimerRef = useRef(null);
  const dropdownRef = useRef(null);

  // 1. Debounced Search Ingestion (300ms)
  useEffect(() => {
    if (!searchQuery.trim()) {
      setSuggestions([]);
      setShowDropdown(false);
      return;
    }

    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
    }

    debounceTimerRef.current = setTimeout(async () => {
      setIsSearching(true);
      try {
        const res = await fetch(
          `${BACKEND_BASE_URL}/api/v1/gis/search?q=${encodeURIComponent(searchQuery.trim())}`
        );
        if (res.ok) {
          const data = await res.json();
          setSuggestions(data || []);
          setShowDropdown(data && data.length > 0);
          setSelectedIndex(-1);
        }
      } catch (err) {
        console.error('Omni-search error:', err);
      } finally {
        setIsSearching(false);
      }
    }, 300);

    return () => {
      if (debounceTimerRef.current) {
        clearTimeout(debounceTimerRef.current);
      }
    };
  }, [searchQuery]);

  // 2. Keyboard Navigation in Autocomplete
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
        handleSelectSuggestion(suggestions[selectedIndex]);
      }
    } else if (e.key === 'Escape') {
      setShowDropdown(false);
    }
  };

  // 3. Selection Handler
  const handleSelectSuggestion = async (item) => {
    setShowDropdown(false);
    setSearchQuery(item.title);
    setActiveEntity(item);
    setIsInspectorOpen(true);

    // Notify parent to fetch & highlight boundary
    if (onSelectEntity) {
      onSelectEntity(item);
    }

    // Fetch 4-tab Jurisdiction Intelligence Dossier
    setLoadingMetrics(true);
    try {
      const res = await fetch(
        `${BACKEND_BASE_URL}/api/v1/gis/jurisdiction-metrics?type=${encodeURIComponent(
          item.type
        )}&id=${encodeURIComponent(item.id)}`
      );
      if (res.ok) {
        const data = await res.json();
        setMetrics(data);
      }
    } catch (err) {
      console.error('Failed to fetch jurisdiction metrics:', err);
    } finally {
      setLoadingMetrics(false);
    }
  };

  // Clear search and reset highlights
  const handleClear = () => {
    setSearchQuery('');
    setSuggestions([]);
    setShowDropdown(false);
    setActiveEntity(null);
    setMetrics(null);
    setIsInspectorOpen(false);
    if (onClearSearch) {
      onClearSearch();
    }
  };

  const copyCitation = (text) => {
    navigator.clipboard.writeText(text);
    setCopiedCitation(true);
    setTimeout(() => setCopiedCitation(false), 2000);
  };

  // Category Badge Helper
  const getBadgeStyle = (type) => {
    switch (type) {
      case 'pincode':
        return 'bg-amber-950 text-amber-300 border-amber-800';
      case 'village':
        return 'bg-emerald-950 text-emerald-300 border-emerald-800';
      case 'city':
        return 'bg-blue-950 text-cyan-300 border-cyan-800';
      case 'district':
        return 'bg-purple-950 text-purple-300 border-purple-800';
      default:
        return 'bg-slate-800 text-slate-300 border-slate-700';
    }
  };

  const getBadgeIcon = (type) => {
    switch (type) {
      case 'pincode':
        return <Mail className="w-3 h-3" />;
      case 'village':
        return <Wheat className="w-3 h-3" />;
      case 'city':
        return <Building2 className="w-3 h-3" />;
      default:
        return <MapPin className="w-3 h-3" />;
    }
  };

  return (
    <>
      {/* 1. Floating Omni-Search Box (Top-Left on Map Canvas) */}
      <div className="absolute top-4 left-4 z-30 w-80 sm:w-96">
        <div className="relative bg-slate-900/95 backdrop-blur-md rounded-xl border border-slate-700 shadow-2xl overflow-visible">
          
          <div className="flex items-center px-3 py-2.5">
            <Search className={`w-4 h-4 text-slate-400 mr-2 shrink-0 ${isSearching ? 'animate-pulse text-amber-400' : ''}`} />
            
            <input
              ref={searchInputRef}
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyDown={handleKeyDown}
              onFocus={() => {
                if (suggestions.length > 0) setShowDropdown(true);
              }}
              placeholder="Search City, Village, or 6-digit PIN..."
              className="w-full bg-transparent text-xs font-semibold text-white placeholder-slate-400 focus:outline-none"
            />

            {searchQuery && (
              <button
                onClick={handleClear}
                className="p-1 text-slate-400 hover:text-white rounded-md hover:bg-slate-800 transition shrink-0 ml-1 cursor-pointer"
                title="Clear Search"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
          </div>

          {/* Autocomplete Dropdown */}
          {showDropdown && suggestions.length > 0 && (
            <div
              ref={dropdownRef}
              className="absolute left-0 right-0 top-full mt-1.5 bg-slate-900/95 backdrop-blur-xl rounded-xl border border-slate-700 shadow-2xl overflow-hidden divide-y divide-slate-800 max-h-80 overflow-y-auto animate-in fade-in duration-150 z-40"
            >
              <div className="px-3 py-1.5 bg-slate-950/80 text-[10px] font-bold uppercase tracking-wider text-slate-400 flex items-center justify-between">
                <span>Matching Jurisdictions</span>
                <span className="font-mono text-amber-400">{suggestions.length} Results</span>
              </div>

              {suggestions.map((item, index) => (
                <div
                  key={item.id || index}
                  onClick={() => handleSelectSuggestion(item)}
                  onMouseEnter={() => setSelectedIndex(index)}
                  className={`p-3 flex items-start space-x-2.5 cursor-pointer transition ${
                    selectedIndex === index
                      ? 'bg-slate-800/90 text-white'
                      : 'hover:bg-slate-800/60 text-slate-200'
                  }`}
                >
                  <div className="mt-0.5 shrink-0 text-slate-400">
                    {getBadgeIcon(item.type)}
                  </div>

                  <div className="flex-1 min-w-0">
                    <div className="flex items-center space-x-2">
                      <span className="text-xs font-bold text-white truncate">
                        {item.title}
                      </span>
                      <span
                        className={`text-[9px] font-bold uppercase tracking-wider px-1.5 py-0.5 rounded border shrink-0 ${getBadgeStyle(
                          item.type
                        )}`}
                      >
                        {item.type}
                      </span>
                    </div>

                    <div className="text-[11px] text-slate-400 truncate mt-0.5">
                      {item.subtitle}
                    </div>
                  </div>

                  <ChevronRight className="w-3.5 h-3.5 text-slate-500 shrink-0 self-center" />
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* 2. Slide-Over Jurisdiction Intelligence Inspector (Right-Side Drawer) */}
      {isInspectorOpen && activeEntity && (
        <aside className="absolute right-0 top-0 bottom-0 w-full sm:w-[450px] lg:w-[480px] bg-slate-900 border-l border-slate-800 flex flex-col h-full z-30 shadow-2xl transition-all duration-300 animate-in slide-in-from-right">
          
          {/* Header */}
          <div className="p-3.5 bg-slate-950 border-b border-slate-800 flex items-center justify-between shrink-0">
            <div className="min-w-0 pr-2">
              <div className="flex items-center space-x-2">
                <span
                  className={`text-[9px] font-bold uppercase tracking-wider px-1.5 py-0.5 rounded border ${getBadgeStyle(
                    activeEntity.type
                  )}`}
                >
                  {activeEntity.type}
                </span>
                <span className="text-[10px] text-emerald-400 font-semibold flex items-center gap-1">
                  <ShieldCheck className="w-3 h-3" />
                  <span>Boundary Resolved</span>
                </span>
              </div>
              <h2 className="text-sm sm:text-base font-bold text-white truncate mt-1">
                {metrics?.demographics?.title || activeEntity.title}
              </h2>
              <div className="text-[11px] text-slate-400 truncate">
                {activeEntity.subtitle}
              </div>
            </div>

            <button
              onClick={() => setIsInspectorOpen(false)}
              className="p-1 rounded text-slate-400 hover:text-white hover:bg-slate-800 transition shrink-0 cursor-pointer"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          {/* 4 Analytical Tabs Navigation */}
          <div className="grid grid-cols-4 border-b border-slate-800 bg-slate-900/90 text-xs shrink-0 font-bold">
            <button
              onClick={() => setActiveTab('demographics')}
              className={`py-2.5 flex flex-col items-center justify-center space-y-1 border-b-2 transition cursor-pointer ${
                activeTab === 'demographics'
                  ? 'border-emerald-500 text-emerald-400 bg-emerald-950/20'
                  : 'border-transparent text-slate-400 hover:text-slate-200'
              }`}
            >
              <Users className="w-3.5 h-3.5" />
              <span className="text-[10px]">Demographics</span>
            </button>

            <button
              onClick={() => setActiveTab('disputes')}
              className={`py-2.5 flex flex-col items-center justify-center space-y-1 border-b-2 transition cursor-pointer ${
                activeTab === 'disputes'
                  ? 'border-rose-500 text-rose-400 bg-rose-950/20'
                  : 'border-transparent text-slate-400 hover:text-slate-200'
              }`}
            >
              <Scale className="w-3.5 h-3.5" />
              <span className="text-[10px]">Disputes</span>
            </button>

            <button
              onClick={() => setActiveTab('lulc')}
              className={`py-2.5 flex flex-col items-center justify-center space-y-1 border-b-2 transition cursor-pointer ${
                activeTab === 'lulc'
                  ? 'border-amber-500 text-amber-400 bg-amber-950/20'
                  : 'border-transparent text-slate-400 hover:text-slate-200'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span className="text-[10px]">LULC & Risk</span>
            </button>

            <button
              onClick={() => setActiveTab('cadastre')}
              className={`py-2.5 flex flex-col items-center justify-center space-y-1 border-b-2 transition cursor-pointer ${
                activeTab === 'cadastre'
                  ? 'border-blue-500 text-cyan-400 bg-blue-950/20'
                  : 'border-transparent text-slate-400 hover:text-slate-200'
              }`}
            >
              <FileText className="w-3.5 h-3.5" />
              <span className="text-[10px]">Cadastre</span>
            </button>
          </div>

          {/* Drawer Body Content */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4 text-xs">
            {loadingMetrics ? (
              <div className="py-20 flex flex-col items-center justify-center space-y-3 text-slate-400">
                <div className="w-6 h-6 border-2 border-amber-500 border-t-transparent rounded-full animate-spin"></div>
                <p className="text-xs">Aggregating Jurisdiction Intelligence...</p>
              </div>
            ) : metrics ? (
              <>
                {/* TAB 1: Demographics & Socioeconomic Profile */}
                {activeTab === 'demographics' && (
                  <div className="space-y-3.5 animate-in fade-in duration-150">
                    <div className="bg-slate-800/80 border border-slate-700/80 rounded-xl p-3">
                      <div className="flex items-center justify-between text-[11px] text-slate-400 mb-1">
                        <span className="font-semibold uppercase tracking-wider">Classification</span>
                        <span className="font-mono text-emerald-400">
                          {metrics.demographics.rural_urban_class}
                        </span>
                      </div>
                      <div className="text-sm font-bold text-white">
                        Estimated Population: {metrics.demographics.population?.toLocaleString()}
                      </div>
                      <div className="text-[11px] text-slate-400 mt-1 flex items-center space-x-3">
                        <span>Sex Ratio: <strong className="text-white">{metrics.demographics.gender_ratio}</strong> / 1000</span>
                        <span>•</span>
                        <span>Households: <strong className="text-white">{metrics.demographics.households?.toLocaleString()}</strong></span>
                      </div>
                    </div>

                    <div className="grid grid-cols-2 gap-2.5">
                      <div className="bg-slate-800/60 border border-slate-700/60 p-2.5 rounded-lg">
                        <div className="flex items-center justify-between text-slate-400 text-[10px] font-semibold uppercase">
                          <span>Electrification</span>
                          <Zap className="w-3.5 h-3.5 text-emerald-400" />
                        </div>
                        <div className="text-lg font-black text-emerald-400 mt-0.5">
                          {metrics.demographics.electrification_pct}%
                        </div>
                        <div className="w-full bg-slate-700 rounded-full h-1.5 mt-1 overflow-hidden">
                          <div
                            className="bg-emerald-400 h-1.5 rounded-full"
                            style={{ width: `${metrics.demographics.electrification_pct}%` }}
                          />
                        </div>
                      </div>

                      <div className="bg-slate-800/60 border border-slate-700/60 p-2.5 rounded-lg">
                        <div className="flex items-center justify-between text-slate-400 text-[10px] font-semibold uppercase">
                          <span>Female Literacy</span>
                          <GraduationCap className="w-3.5 h-3.5 text-purple-400" />
                        </div>
                        <div className="text-lg font-black text-purple-400 mt-0.5">
                          {metrics.demographics.female_literacy_pct}%
                        </div>
                        <div className="w-full bg-slate-700 rounded-full h-1.5 mt-1 overflow-hidden">
                          <div
                            className="bg-purple-400 h-1.5 rounded-full"
                            style={{ width: `${metrics.demographics.female_literacy_pct}%` }}
                          />
                        </div>
                      </div>

                      <div className="bg-slate-800/60 border border-slate-700/60 p-2.5 rounded-lg">
                        <div className="flex items-center justify-between text-slate-400 text-[10px] font-semibold uppercase">
                          <span>Agri Workforce</span>
                          <Wheat className="w-3.5 h-3.5 text-amber-400" />
                        </div>
                        <div className="text-lg font-black text-amber-400 mt-0.5">
                          {metrics.demographics.agri_workforce_pct}%
                        </div>
                        <span className="text-[9px] text-slate-400">Direct Land Dependency</span>
                      </div>

                      <div className="bg-slate-800/60 border border-slate-700/60 p-2.5 rounded-lg">
                        <div className="flex items-center justify-between text-slate-400 text-[10px] font-semibold uppercase">
                          <span>Source Index</span>
                          <ShieldCheck className="w-3.5 h-3.5 text-cyan-400" />
                        </div>
                        <div className="text-xs font-bold text-cyan-300 mt-1">
                          SHRUG v1.5 / Census
                        </div>
                        <span className="text-[9px] text-slate-400">Development Data Lab</span>
                      </div>
                    </div>
                  </div>
                )}

                {/* TAB 2: Land Disputes & Judicial Friction */}
                {activeTab === 'disputes' && (
                  <div className="space-y-3.5 animate-in fade-in duration-150">
                    <div className="bg-rose-950/40 border border-rose-900/60 rounded-xl p-3 flex items-center justify-between">
                      <div>
                        <span className="text-[10px] font-bold uppercase tracking-wider text-rose-400">
                          Active Litigation Density
                        </span>
                        <div className="text-lg font-black text-white mt-0.5">
                          {metrics.disputes.active_disputes_count} Court Hotspots
                        </div>
                      </div>
                      <div className="text-right">
                        <span className="text-[10px] text-slate-400 block">Locked Hectares</span>
                        <span className="text-base font-bold text-rose-300">
                          {metrics.disputes.disputed_hectares}
                        </span>
                      </div>
                    </div>

                    {/* Statutes Invoked */}
                    <div className="bg-slate-800/80 border border-slate-700 rounded-xl p-3 space-y-2">
                      <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">
                        Statutes Invoked in Jurisdiction
                      </span>
                      <div className="space-y-1.5">
                        {metrics.disputes.acts_invoked.map((item, idx) => (
                          <div
                            key={idx}
                            className="flex items-center justify-between bg-slate-900/80 p-2 rounded border border-slate-800 text-[11px]"
                          >
                            <span className="text-slate-300 font-medium">{item.statute}</span>
                            <span className="font-mono font-bold text-amber-400 bg-slate-800 px-1.5 py-0.5 rounded">
                              {item.count} Cases
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>

                    {/* Precedents with 1-Click PDF Stream */}
                    <div className="space-y-2.5">
                      <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">
                        Landmark Judicial Precedents
                      </span>
                      {metrics.disputes.landmark_precedents.map((prec) => (
                        <div
                          key={prec.id}
                          className="bg-slate-800/70 border border-slate-700 p-3 rounded-xl space-y-2 hover:border-slate-600 transition"
                        >
                          <h4 className="text-xs font-bold text-white leading-snug">
                            {prec.title}
                          </h4>
                          <div className="text-[11px] text-slate-400">{prec.authority}</div>
                          <div className="font-mono text-[9px] text-slate-400 bg-slate-900 p-1.5 rounded border border-slate-800">
                            {prec.citation}
                          </div>
                          <div className="flex items-center justify-between pt-1">
                            <button
                              onClick={() => copyCitation(prec.citation)}
                              className="text-slate-400 hover:text-slate-200 text-[10px] flex items-center space-x-1 cursor-pointer"
                            >
                              {copiedCitation ? (
                                <Check className="w-3 h-3 text-emerald-400" />
                              ) : (
                                <Copy className="w-3 h-3" />
                              )}
                              <span>{copiedCitation ? 'Copied' : 'Copy Citation'}</span>
                            </button>

                            <button
                              onClick={() => onViewPdf && onViewPdf(prec)}
                              className="inline-flex items-center space-x-1.5 bg-amber-500 hover:bg-amber-600 text-slate-950 text-xs font-bold px-2.5 py-1 rounded shadow-xs transition cursor-pointer"
                            >
                              <FileText className="w-3.5 h-3.5" />
                              <span>View PDF (In-App)</span>
                            </button>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* TAB 3: Real-Time LULC & Climate Resilience */}
                {activeTab === 'lulc' && (
                  <div className="space-y-3.5 animate-in fade-in duration-150">
                    <div className="bg-slate-800/80 border border-slate-700 rounded-xl p-3 space-y-2">
                      <div className="flex items-center justify-between">
                        <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400">
                          Sentinel-2 10m LULC Breakdown
                        </span>
                        <span className="text-[9px] font-mono text-emerald-400 bg-emerald-950 px-1.5 py-0.5 rounded border border-emerald-800">
                          Impact Observatory
                        </span>
                      </div>

                      {/* LULC Breakdown Bars */}
                      <div className="space-y-2 pt-1 text-[11px]">
                        <div>
                          <div className="flex items-center justify-between text-slate-300 mb-1">
                            <span className="flex items-center space-x-1.5">
                              <span className="w-2.5 h-2.5 rounded-xs" style={{ backgroundColor: '#FFDB5C' }}></span>
                              <span>Crops & Farmland</span>
                            </span>
                            <span className="font-mono font-bold text-amber-300">
                              {metrics.lulc.farmland_pct}%
                            </span>
                          </div>
                          <div className="w-full bg-slate-700 rounded-full h-1.5 overflow-hidden">
                            <div
                              className="h-1.5 rounded-full"
                              style={{ width: `${metrics.lulc.farmland_pct}%`, backgroundColor: '#FFDB5C' }}
                            />
                          </div>
                        </div>

                        <div>
                          <div className="flex items-center justify-between text-slate-300 mb-1">
                            <span className="flex items-center space-x-1.5">
                              <span className="w-2.5 h-2.5 rounded-xs" style={{ backgroundColor: '#358221' }}></span>
                              <span>Forest & Tree Canopy</span>
                            </span>
                            <span className="font-mono font-bold text-green-400">
                              {metrics.lulc.forest_pct}%
                            </span>
                          </div>
                          <div className="w-full bg-slate-700 rounded-full h-1.5 overflow-hidden">
                            <div
                              className="h-1.5 rounded-full"
                              style={{ width: `${metrics.lulc.forest_pct}%`, backgroundColor: '#358221' }}
                            />
                          </div>
                        </div>

                        <div>
                          <div className="flex items-center justify-between text-slate-300 mb-1">
                            <span className="flex items-center space-x-1.5">
                              <span className="w-2.5 h-2.5 rounded-xs" style={{ backgroundColor: '#ED022A' }}></span>
                              <span>Residential / Built-Up</span>
                            </span>
                            <span className="font-mono font-bold text-rose-400">
                              {metrics.lulc.built_up_pct}%
                            </span>
                          </div>
                          <div className="w-full bg-slate-700 rounded-full h-1.5 overflow-hidden">
                            <div
                              className="h-1.5 rounded-full"
                              style={{ width: `${metrics.lulc.built_up_pct}%`, backgroundColor: '#ED022A' }}
                            />
                          </div>
                        </div>

                        <div>
                          <div className="flex items-center justify-between text-slate-300 mb-1">
                            <span className="flex items-center space-x-1.5">
                              <span className="w-2.5 h-2.5 rounded-xs" style={{ backgroundColor: '#1A5BAB' }}></span>
                              <span>Water Bodies & Rivers</span>
                            </span>
                            <span className="font-mono font-bold text-blue-400">
                              {metrics.lulc.water_pct}%
                            </span>
                          </div>
                          <div className="w-full bg-slate-700 rounded-full h-1.5 overflow-hidden">
                            <div
                              className="h-1.5 rounded-full"
                              style={{ width: `${metrics.lulc.water_pct}%`, backgroundColor: '#1A5BAB' }}
                            />
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* Climate Vulnerability */}
                    <div className="grid grid-cols-2 gap-2.5">
                      <div className="bg-slate-800/60 border border-slate-700 p-2.5 rounded-lg">
                        <div className="flex items-center space-x-1.5 text-[10px] font-semibold text-slate-400 uppercase">
                          <Droplets className="w-3.5 h-3.5 text-blue-400" />
                          <span>Flood Vulnerability</span>
                        </div>
                        <div className="text-xs font-bold text-blue-300 mt-1">
                          {metrics.lulc.flood_vulnerability_index}
                        </div>
                        <span className="text-[9px] text-slate-400">CWC Hydro-Morphology</span>
                      </div>

                      <div className="bg-slate-800/60 border border-slate-700 p-2.5 rounded-lg">
                        <div className="flex items-center space-x-1.5 text-[10px] font-semibold text-slate-400 uppercase">
                          <AlertTriangle className="w-3.5 h-3.5 text-amber-400" />
                          <span>Drought Risk</span>
                        </div>
                        <div className="text-xs font-bold text-amber-300 mt-1">
                          {metrics.lulc.drought_risk_index}
                        </div>
                        <span className="text-[9px] text-slate-400">IMD Aridity Index</span>
                      </div>
                    </div>
                  </div>
                )}

                {/* TAB 4: Cadastral Reforms & Scheme Rollout */}
                {activeTab === 'cadastre' && (
                  <div className="space-y-3.5 animate-in fade-in duration-150">
                    <div className="bg-slate-800/80 border border-slate-700 rounded-xl p-3 space-y-2.5">
                      <div className="flex items-center justify-between text-slate-400 text-[10px] font-bold uppercase">
                        <span>DILRMP 3.0 & Bhu-Aadhaar Coverage</span>
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                      </div>

                      <div className="space-y-2">
                        <div>
                          <div className="flex items-center justify-between text-xs text-slate-300 mb-1">
                            <span>Bhu-Aadhaar (14-Digit ULPIN)</span>
                            <span className="font-bold text-emerald-400">
                              {metrics.cadastral_reforms.bhu_aadhaar_ulpin_coverage_pct}%
                            </span>
                          </div>
                          <div className="w-full bg-slate-700 rounded-full h-1.5 overflow-hidden">
                            <div
                              className="bg-emerald-400 h-1.5 rounded-full"
                              style={{
                                width: `${metrics.cadastral_reforms.bhu_aadhaar_ulpin_coverage_pct}%`
                              }}
                            />
                          </div>
                        </div>

                        <div>
                          <div className="flex items-center justify-between text-xs text-slate-300 mb-1">
                            <span>Cadastral Map Digitization</span>
                            <span className="font-bold text-cyan-400">
                              {metrics.cadastral_reforms.dilrmp_coverage_pct}%
                            </span>
                          </div>
                          <div className="w-full bg-slate-700 rounded-full h-1.5 overflow-hidden">
                            <div
                              className="bg-cyan-400 h-1.5 rounded-full"
                              style={{ width: `${metrics.cadastral_reforms.dilrmp_coverage_pct}%` }}
                            />
                          </div>
                        </div>
                      </div>
                    </div>

                    {/* SVAMITVA Scheme Status */}
                    <div className="bg-slate-800/60 border border-slate-700 p-3 rounded-xl space-y-2">
                      <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">
                        SVAMITVA Scheme Execution Status
                      </span>

                      <div className="grid grid-cols-2 gap-2 text-[11px]">
                        <div className="bg-slate-900/80 p-2 rounded border border-slate-800">
                          <span className="text-slate-400 block text-[10px]">Drone Survey:</span>
                          <span className="text-emerald-400 font-bold flex items-center gap-1 mt-0.5">
                            <CheckCircle2 className="w-3 h-3" />
                            <span>Completed</span>
                          </span>
                        </div>
                        <div className="bg-slate-900/80 p-2 rounded border border-slate-800">
                          <span className="text-slate-400 block text-[10px]">Spatial Map 1:</span>
                          <span className="text-emerald-400 font-bold flex items-center gap-1 mt-0.5">
                            <CheckCircle2 className="w-3 h-3" />
                            <span>Generated</span>
                          </span>
                        </div>
                      </div>

                      <div className="bg-slate-900/80 p-2 rounded border border-slate-800 flex items-center justify-between text-[11px]">
                        <span className="text-slate-300">Property Cards Issued:</span>
                        <span className="font-mono font-bold text-amber-400">
                          {metrics.cadastral_reforms.svamitva_status.property_cards_distributed?.toLocaleString()}{' '}
                          Cards
                        </span>
                      </div>
                    </div>

                    {/* Circle Rates */}
                    <div className="bg-slate-800/40 border border-slate-700 p-3 rounded-xl space-y-1">
                      <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">
                        Official Ready Reckoner / Circle Rates
                      </span>
                      <div className="text-xs font-bold text-white">
                        {metrics.cadastral_reforms.jantri_circle_rate_index}
                      </div>
                      <span className="text-[10px] text-slate-400">
                        Revenue Department Statutory Valuation Schedule
                      </span>
                    </div>
                  </div>
                )}
              </>
            ) : null}
          </div>
        </aside>
      )}
    </>
  );
}
