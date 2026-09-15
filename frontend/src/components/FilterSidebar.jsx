import React from 'react';
import { Filter, RotateCcw, MapPin, FileText, Layers, Calendar, Building, Map } from 'lucide-react';

export default function FilterSidebar({
  filters,
  onFilterChange,
  onResetFilters,
  facets = {},
  isHi = false
}) {
  const states = [
    "All States",
    "National",
    "Uttar Pradesh",
    "Maharashtra",
    "Odisha",
    "Madhya Pradesh",
    "Karnataka",
    "Andhra Pradesh",
    "Rajasthan",
    "Bihar"
  ];

  const docTypes = [
    "Manual / Framework",
    "Judgement",
    "Dataset",
    "Policy Brief",
    "Academic Paper",
    "Best Practice Report"
  ];

  const themes = [
    "Digital Cadastre & Resurvey",
    "Land Acquisition (RFCTLARR)",
    "Tenancy & Leasing Reforms",
    "Forest & Tribal Land Rights",
    "Urban-Rural Land Transition"
  ];

  const authorities = [
    "Department of Land Resources (DoLR)",
    "Supreme Court of India",
    "High Court of Judicature at Bombay",
    "Board of Revenue Uttar Pradesh",
    "Revenue & Disaster Management Dept, Odisha",
    "NITI Aayog",
    "Indian Institute of Management (IIM)"
  ];

  return (
    <aside className="w-full lg:w-72 bg-white rounded-xl border border-slate-200 shadow-gov-sm p-4 h-fit">
      <div className="flex items-center justify-between pb-3 border-b border-slate-200 mb-4">
        <div className="flex items-center space-x-2 text-gov-navy font-bold text-sm">
          <Filter className="w-4 h-4 text-gov-navy" />
          <span>{isHi ? "फ़िल्टर एवं वर्गीकरण" : "Faceted Repository Filters"}</span>
        </div>
        <button
          onClick={onResetFilters}
          className="text-xs text-slate-500 hover:text-blue-700 flex items-center space-x-1 font-medium transition-colors"
          title="Reset all filter parameters"
        >
          <RotateCcw className="w-3 h-3" />
          <span>{isHi ? "रीसेट करें" : "Reset"}</span>
        </button>
      </div>

      <div className="space-y-4 text-xs">
        
        {/* 1. Geography / State & LGD */}
        <div>
          <label className="font-bold text-slate-800 mb-1.5 flex items-center gap-1.5">
            <MapPin className="w-3.5 h-3.5 text-gov-green" />
            <span>{isHi ? "भूगोल एवं राज्य / संघ राज्य क्षेत्र" : "Jurisdiction & State/UT"}</span>
          </label>
          <select
            value={filters.state_ut || "All States"}
            onChange={(e) => onFilterChange('state_ut', e.target.value === "All States" ? "" : e.target.value)}
            className="w-full bg-slate-50 border border-slate-300 rounded-md p-2 text-slate-800 text-xs focus:ring-2 focus:ring-blue-500 focus:outline-none"
          >
            {states.map((st, i) => (
              <option key={i} value={st}>
                {st} {facets.state_ut?.[st] ? `(${facets.state_ut[st]})` : ''}
              </option>
            ))}
          </select>
        </div>

        {/* District & LGD Directory Code */}
        <div className="grid grid-cols-2 gap-2">
          <div>
            <label className="text-[11px] font-semibold text-slate-600 mb-1 block">
              District
            </label>
            <input
              type="text"
              placeholder="e.g. Varanasi"
              value={filters.district || ""}
              onChange={(e) => onFilterChange('district', e.target.value)}
              className="w-full bg-slate-50 border border-slate-300 rounded p-1.5 text-xs text-slate-800 focus:ring-1 focus:ring-blue-500"
            />
          </div>
          <div>
            <label className="text-[11px] font-semibold text-slate-600 mb-1 block" title="Local Government Directory Code">
              LGD Code
            </label>
            <input
              type="text"
              placeholder="e.g. 187"
              value={filters.lgd_code || ""}
              onChange={(e) => onFilterChange('lgd_code', e.target.value)}
              className="w-full bg-slate-50 border border-slate-300 rounded p-1.5 text-xs text-slate-800 focus:ring-1 focus:ring-blue-500"
            />
          </div>
        </div>

        {/* 2. Document Type */}
        <div className="pt-2 border-t border-slate-100">
          <label className="font-bold text-slate-800 mb-1.5 flex items-center gap-1.5">
            <FileText className="w-3.5 h-3.5 text-blue-600" />
            <span>{isHi ? "दस्तावेज़ का प्रकार" : "Document Classification"}</span>
          </label>
          <div className="space-y-1.5">
            <button
              onClick={() => onFilterChange('document_type', '')}
              className={`w-full text-left px-2 py-1 rounded text-xs transition-colors flex justify-between items-center ${
                !filters.document_type ? 'bg-blue-50 font-bold text-blue-900 border border-blue-200' : 'text-slate-600 hover:bg-slate-50'
              }`}
            >
              <span>All Document Types</span>
            </button>
            {docTypes.map((dt, i) => (
              <button
                key={i}
                onClick={() => onFilterChange('document_type', filters.document_type === dt ? '' : dt)}
                className={`w-full text-left px-2 py-1 rounded text-xs transition-colors flex justify-between items-center ${
                  filters.document_type === dt ? 'bg-blue-50 font-bold text-blue-900 border border-blue-200' : 'text-slate-600 hover:bg-slate-50'
                }`}
              >
                <span className="truncate">{dt}</span>
                {facets.document_type?.[dt] && (
                  <span className="text-[10px] bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded-full font-mono">
                    {facets.document_type[dt]}
                  </span>
                )}
              </button>
            ))}
          </div>
        </div>

        {/* 3. Theme Facet */}
        <div className="pt-2 border-t border-slate-100">
          <label className="font-bold text-slate-800 mb-1.5 flex items-center gap-1.5">
            <Layers className="w-3.5 h-3.5 text-amber-600" />
            <span>{isHi ? "विषयगत क्षेत्र (Theme)" : "Governance Theme"}</span>
          </label>
          <div className="space-y-1">
            {themes.map((theme, i) => (
              <label
                key={i}
                className="flex items-center space-x-2 py-0.5 cursor-pointer text-slate-700 hover:text-slate-900"
              >
                <input
                  type="checkbox"
                  checked={filters.theme === theme}
                  onChange={() => onFilterChange('theme', filters.theme === theme ? '' : theme)}
                  className="rounded border-slate-300 text-gov-navy focus:ring-blue-500"
                />
                <span className="truncate text-[11px]">{theme}</span>
              </label>
            ))}
          </div>
        </div>

        {/* 4. Spatial Layer Toggle */}
        <div className="pt-2 border-t border-slate-100">
          <label className="flex items-center justify-between cursor-pointer bg-slate-50 p-2 rounded border border-slate-200">
            <div className="flex items-center space-x-2">
              <Map className="w-4 h-4 text-emerald-600" />
              <div>
                <span className="font-semibold text-slate-800 block text-xs">GeoJSON Spatial Layer</span>
                <span className="text-[10px] text-slate-500">Only show items with map boundaries</span>
              </div>
            </div>
            <input
              type="checkbox"
              checked={Boolean(filters.has_spatial)}
              onChange={(e) => onFilterChange('has_spatial', e.target.checked ? true : '')}
              className="rounded border-slate-300 text-emerald-600 focus:ring-emerald-500"
            />
          </label>
        </div>

        {/* 5. Year Range Filter */}
        <div className="pt-2 border-t border-slate-100">
          <label className="font-bold text-slate-800 mb-1.5 flex items-center gap-1.5">
            <Calendar className="w-3.5 h-3.5 text-purple-600" />
            <span>{isHi ? "प्रकाशन वर्ष" : "Publication Year Range"}</span>
          </label>
          <div className="grid grid-cols-2 gap-2">
            <div>
              <span className="text-[10px] text-slate-500">From</span>
              <input
                type="number"
                min="1950"
                max="2026"
                placeholder="2020"
                value={filters.year_from || ""}
                onChange={(e) => onFilterChange('year_from', e.target.value)}
                className="w-full bg-slate-50 border border-slate-300 rounded p-1.5 text-xs text-slate-800 focus:ring-1 focus:ring-blue-500"
              />
            </div>
            <div>
              <span className="text-[10px] text-slate-500">To</span>
              <input
                type="number"
                min="1950"
                max="2026"
                placeholder="2026"
                value={filters.year_to || ""}
                onChange={(e) => onFilterChange('year_to', e.target.value)}
                className="w-full bg-slate-50 border border-slate-300 rounded p-1.5 text-xs text-slate-800 focus:ring-1 focus:ring-blue-500"
              />
            </div>
          </div>
        </div>

      </div>
    </aside>
  );
}
