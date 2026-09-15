import React, { useState, useEffect, useRef } from 'react';
import { 
  Search, 
  LayoutGrid, 
  Table as TableIcon, 
  X, 
  Sparkles, 
  ChevronLeft, 
  ChevronRight,
  SlidersHorizontal,
  ScrollText,
  BookOpen,
  Scale,
  Database,
  Award,
  Layers
} from 'lucide-react';
import ResourceCard from './ResourceCard';
import ResourceTable from './ResourceTable';
import { TAXONOMY_STREAMS } from '../services/mockData';

export default function ResourceCatalog({
  resources = [],
  total = 0,
  page = 1,
  totalPages = 1,
  onPageChange,
  filters,
  onFilterChange,
  onSelectResource,
  isHi = false
}) {
  const [viewMode, setViewMode] = useState('grid'); // 'grid' or 'table'
  const [searchInput, setSearchInput] = useState(filters.q || '');
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const searchContainerRef = useRef(null);

  // Sync external filter changes to searchInput
  useEffect(() => {
    setSearchInput(filters.q || '');
  }, [filters.q]);

  // Handle auto-suggestions
  useEffect(() => {
    if (searchInput.trim().length >= 2) {
      const q = searchInput.toLowerCase();
      const matches = resources
        .filter(r => r.title.toLowerCase().includes(q) || r.theme.toLowerCase().includes(q))
        .slice(0, 5)
        .map(r => ({
          label: r.title,
          id: r.id,
          type: r.document_type
        }));
      setSuggestions(matches);
    } else {
      setSuggestions([]);
    }
  }, [searchInput, resources]);

  // Click outside listener for suggestions
  useEffect(() => {
    const handleClickOutside = (e) => {
      if (searchContainerRef.current && !searchContainerRef.current.contains(e.target)) {
        setShowSuggestions(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSearchSubmit = (e) => {
    e?.preventDefault();
    setShowSuggestions(false);
    onFilterChange('q', searchInput);
  };

  const getStreamIcon = (iconName) => {
    switch (iconName) {
      case 'ScrollText': return <ScrollText className="w-4 h-4" />;
      case 'BookOpen': return <BookOpen className="w-4 h-4" />;
      case 'Scale': return <Scale className="w-4 h-4" />;
      case 'Database': return <Database className="w-4 h-4" />;
      case 'Award': return <Award className="w-4 h-4" />;
      default: return <Layers className="w-4 h-4" />;
    }
  };

  // Active filter tags for quick removal
  const activeFilters = [];
  if (filters.q) activeFilters.push({ key: 'q', label: `Search: "${filters.q}"` });
  if (filters.state_ut && filters.state_ut !== 'All States') activeFilters.push({ key: 'state_ut', label: `State: ${filters.state_ut}` });
  if (filters.document_type) activeFilters.push({ key: 'document_type', label: `Type: ${filters.document_type}` });
  if (filters.theme) activeFilters.push({ key: 'theme', label: `Theme: ${filters.theme}` });
  if (filters.district) activeFilters.push({ key: 'district', label: `District: ${filters.district}` });
  if (filters.has_spatial) activeFilters.push({ key: 'has_spatial', label: 'GIS Vector Only' });
  if (filters.year_from || filters.year_to) activeFilters.push({ key: 'year', label: `Year: ${filters.year_from || '1950'} - ${filters.year_to || '2026'}` });

  return (
    <div className="flex-1 space-y-4">
      
      {/* 5 TAXONOMY STREAM TABS */}
      <div className="bg-white rounded-xl border border-slate-200 p-1.5 shadow-gov-sm overflow-x-auto">
        <div className="flex space-x-1.5 min-w-max">
          {TAXONOMY_STREAMS.map((stream) => {
            const isSelected = (filters.taxonomy_stream || 'all') === stream.id;
            return (
              <button
                key={stream.id}
                onClick={() => onFilterChange('taxonomy_stream', stream.id)}
                className={`flex items-center space-x-2 px-3.5 py-2 rounded-lg text-xs font-bold transition-all ${
                  isSelected
                    ? 'bg-gov-navy text-white shadow-sm'
                    : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
                }`}
              >
                {getStreamIcon(stream.icon)}
                <span>{isHi ? stream.label_hi : stream.label}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* SEARCH AND CONTROLS BAR */}
      <div className="bg-white rounded-xl border border-slate-200 p-3 sm:p-4 shadow-gov-sm flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3">
        
        {/* Search Bar with Autocomplete */}
        <div ref={searchContainerRef} className="relative flex-1">
          <form onSubmit={handleSearchSubmit} className="relative flex items-center">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 pointer-events-none" />
            <input
              type="text"
              placeholder={isHi ? "शीर्षक, ULPIN, कानून, भूमि अधिग्रहण या विषय खोजें..." : "Search acts, judgements, ULPIN, cadastral datasets, or themes..."}
              value={searchInput}
              onChange={(e) => {
                setSearchInput(e.target.value);
                setShowSuggestions(true);
              }}
              onFocus={() => setShowSuggestions(true)}
              className="w-full bg-slate-50 border border-slate-300 rounded-lg pl-9 pr-16 py-2 text-xs text-slate-900 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all shadow-inner"
            />
            {searchInput && (
              <button
                type="button"
                onClick={() => {
                  setSearchInput('');
                  onFilterChange('q', '');
                }}
                className="absolute right-10 text-slate-400 hover:text-slate-600 p-1"
              >
                <X className="w-3.5 h-3.5" />
              </button>
            )}
            <button
              type="submit"
              className="absolute right-1.5 bg-gov-navy hover:bg-blue-800 text-white px-2.5 py-1 rounded text-xs font-bold transition-colors shadow-sm"
            >
              Search
            </button>
          </form>

          {/* Instant Auto-Suggestions Dropdown */}
          {showSuggestions && suggestions.length > 0 && (
            <div className="absolute top-full left-0 right-0 mt-1 bg-white rounded-lg border border-slate-200 shadow-xl z-30 divide-y divide-slate-100 overflow-hidden text-xs">
              <div className="bg-slate-50 px-3 py-1 text-[10px] font-bold uppercase text-slate-500 flex items-center gap-1">
                <Sparkles className="w-3 h-3 text-blue-600" />
                <span>Auto-Suggested Matches</span>
              </div>
              {suggestions.map((sug, idx) => (
                <button
                  key={idx}
                  onClick={() => {
                    setSearchInput(sug.label);
                    onFilterChange('q', sug.label);
                    setShowSuggestions(false);
                  }}
                  className="w-full text-left px-3 py-2 hover:bg-blue-50/80 transition-colors flex items-center justify-between text-slate-800"
                >
                  <span className="truncate pr-2 font-medium">{sug.label}</span>
                  <span className="text-[10px] bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded shrink-0 font-mono">
                    {sug.type}
                  </span>
                </button>
              ))}
            </div>
          )}
        </div>

        {/* View Controls: Sort & Grid/Table Toggle */}
        <div className="flex items-center justify-between sm:justify-end space-x-2 text-xs">
          
          {/* Sort Dropdown */}
          <div className="flex items-center space-x-1.5">
            <span className="text-slate-500 font-medium text-[11px] hidden sm:inline">Sort:</span>
            <select
              value={filters.sort_by || "date_desc"}
              onChange={(e) => onFilterChange('sort_by', e.target.value)}
              className="bg-slate-50 border border-slate-300 rounded-lg py-1.5 px-2 text-xs text-slate-800 font-medium focus:ring-1 focus:ring-blue-500"
            >
              <option value="date_desc">Newest First</option>
              <option value="date_asc">Oldest First</option>
              <option value="title">Title (A-Z)</option>
            </select>
          </div>

          {/* Grid / Table Toggle */}
          <div className="flex items-center bg-slate-100 p-1 rounded-lg border border-slate-200">
            <button
              onClick={() => setViewMode('grid')}
              className={`p-1.5 rounded transition-all ${
                viewMode === 'grid' ? 'bg-white shadow-sm text-gov-navy font-bold' : 'text-slate-500 hover:text-slate-800'
              }`}
              title="Grid Card View"
            >
              <LayoutGrid className="w-4 h-4" />
            </button>
            <button
              onClick={() => setViewMode('table')}
              className={`p-1.5 rounded transition-all ${
                viewMode === 'table' ? 'bg-white shadow-sm text-gov-navy font-bold' : 'text-slate-500 hover:text-slate-800'
              }`}
              title="Cadastral Tabular View"
            >
              <TableIcon className="w-4 h-4" />
            </button>
          </div>

        </div>

      </div>

      {/* ACTIVE FILTERS CHIP BAR */}
      {activeFilters.length > 0 && (
        <div className="flex flex-wrap items-center gap-1.5 py-1">
          <span className="text-xs text-slate-500 font-semibold mr-1">Active Filters:</span>
          {activeFilters.map((af, i) => (
            <span
              key={i}
              className="inline-flex items-center space-x-1 bg-blue-50 text-blue-900 border border-blue-200 px-2 py-0.5 rounded-full text-xs font-medium"
            >
              <span>{af.label}</span>
              <button
                onClick={() => {
                  if (af.key === 'year') {
                    onFilterChange('year_from', '');
                    onFilterChange('year_to', '');
                  } else {
                    onFilterChange(af.key, '');
                  }
                }}
                className="hover:text-red-700"
              >
                <X className="w-3 h-3" />
              </button>
            </span>
          ))}
          <button
            onClick={() => {
              ['q', 'state_ut', 'document_type', 'theme', 'district', 'has_spatial', 'year_from', 'year_to'].forEach(k => onFilterChange(k, ''));
            }}
            className="text-xs text-red-600 hover:underline font-semibold ml-2"
          >
            Clear All
          </button>
        </div>
      )}

      {/* RESULTS COUNT SUMMARY */}
      <div className="text-xs text-slate-500 font-medium px-1 flex justify-between items-center">
        <span>Showing <strong className="text-slate-800">{resources.length}</strong> of <strong className="text-slate-800">{total}</strong> indexed records</span>
        <span className="text-[11px] text-slate-400">Page {page} of {totalPages}</span>
      </div>

      {/* MAIN CONTENT VIEW (GRID OR TABLE) */}
      {viewMode === 'grid' ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {resources.map((res) => (
            <ResourceCard
              key={res.id}
              resource={res}
              onSelectResource={onSelectResource}
              isHi={isHi}
            />
          ))}
        </div>
      ) : (
        <ResourceTable
          resources={resources}
          onSelectResource={onSelectResource}
          isHi={isHi}
        />
      )}

      {/* PAGINATION CONTROLS */}
      {totalPages > 1 && (
        <div className="bg-white rounded-xl border border-slate-200 p-3 shadow-gov-sm flex items-center justify-between text-xs">
          <button
            onClick={() => onPageChange(page - 1)}
            disabled={page <= 1}
            className={`flex items-center space-x-1 px-3 py-1.5 rounded-md border font-semibold ${
              page <= 1 ? 'border-slate-200 text-slate-300 cursor-not-allowed' : 'border-slate-300 text-slate-700 hover:bg-slate-50'
            }`}
          >
            <ChevronLeft className="w-3.5 h-3.5" />
            <span>Previous</span>
          </button>

          <div className="flex items-center space-x-1 font-mono text-xs">
            {Array.from({ length: totalPages }, (_, i) => i + 1).map((p) => (
              <button
                key={p}
                onClick={() => onPageChange(p)}
                className={`w-7 h-7 rounded flex items-center justify-center font-bold ${
                  p === page ? 'bg-gov-navy text-white shadow-sm' : 'text-slate-600 hover:bg-slate-100'
                }`}
              >
                {p}
              </button>
            ))}
          </div>

          <button
            onClick={() => onPageChange(page + 1)}
            disabled={page >= totalPages}
            className={`flex items-center space-x-1 px-3 py-1.5 rounded-md border font-semibold ${
              page >= totalPages ? 'border-slate-200 text-slate-300 cursor-not-allowed' : 'border-slate-300 text-slate-700 hover:bg-slate-50'
            }`}
          >
            <span>Next</span>
            <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>
      )}

    </div>
  );
}
