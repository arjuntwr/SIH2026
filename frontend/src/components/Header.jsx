import React from 'react';
import { Globe, Eye, Volume2, ShieldCheck, Search, BookOpen, Layers } from 'lucide-react';

export default function Header({
  lang,
  setLang,
  contrastMode,
  setContrastMode,
  fontSize,
  setFontSize
}) {
  const isHi = lang === 'hi';

  const adjustFont = (delta) => {
    setFontSize(prev => Math.min(18, Math.max(12, prev + delta)));
  };

  return (
    <header className="w-full bg-white border-b border-slate-200 shadow-gov-sm sticky top-0 z-40">
      {/* Indian Tricolor Accent Strip */}
      <div className="h-1.5 w-full grid grid-cols-3">
        <div className="bg-[#FF9933]"></div>
        <div className="bg-white"></div>
        <div className="bg-[#138808]"></div>
      </div>

      {/* Top Accessibility & Institutional Bar */}
      <div className="bg-[#06172B] text-slate-300 text-xs py-1.5 px-4 sm:px-6 lg:px-8 flex flex-wrap justify-between items-center gap-2 border-b border-slate-800">
        <div className="flex items-center space-x-3">
          <span className="font-semibold text-white tracking-wide">
            {isHi ? "भारत सरकार | ग्रामीण विकास मंत्रालय" : "GOVERNMENT OF INDIA | MINISTRY OF RURAL DEVELOPMENT"}
          </span>
          <span className="text-slate-500">|</span>
          <span className="text-slate-300 hidden md:inline">
            {isHi ? "भूमि संसाधन विभाग (DoLR)" : "DEPARTMENT OF LAND RESOURCES (DoLR)"}
          </span>
        </div>

        {/* Accessibility Tools */}
        <div className="flex items-center space-x-3 text-xs">
          {/* Font Sizer */}
          <div className="flex items-center space-x-1 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
            <button
              onClick={() => adjustFont(-1)}
              title="Decrease Font Size"
              className="hover:text-white px-1 text-[11px] font-bold"
            >
              A-
            </button>
            <button
              onClick={() => setFontSize(14)}
              title="Reset Font Size"
              className="hover:text-white px-1 font-semibold"
            >
              A
            </button>
            <button
              onClick={() => adjustFont(1)}
              title="Increase Font Size"
              className="hover:text-white px-1 text-[13px] font-bold"
            >
              A+
            </button>
          </div>

          {/* High Contrast Toggle */}
          <button
            onClick={() => setContrastMode(!contrastMode)}
            className={`flex items-center space-x-1 px-2 py-0.5 rounded border transition-colors ${
              contrastMode ? 'bg-amber-500 text-slate-900 border-amber-400 font-bold' : 'bg-slate-800/80 border-slate-700 hover:text-white'
            }`}
            title="Toggle High Contrast Mode"
          >
            <Eye className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">{contrastMode ? 'Normal' : 'High Contrast'}</span>
          </button>

          {/* Language Switcher */}
          <div className="flex items-center space-x-1 bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
            <Globe className="w-3.5 h-3.5 text-amber-400" />
            <button
              onClick={() => setLang('en')}
              className={`px-1.5 font-medium ${lang === 'en' ? 'text-amber-400 font-bold' : 'hover:text-white'}`}
            >
              English
            </button>
            <span className="text-slate-600">|</span>
            <button
              onClick={() => setLang('hi')}
              className={`px-1.5 font-medium ${lang === 'hi' ? 'text-amber-400 font-bold' : 'hover:text-white'}`}
            >
              हिन्दी
            </button>
          </div>
        </div>
      </div>

      {/* Main Branding Header Bar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap justify-between items-center gap-4">
        <div className="flex items-center space-x-4">
          {/* Emblem of India / Ashoka Lion Motif */}
          <div className="flex flex-col items-center justify-center p-1 border-r border-slate-200 pr-4">
            <div className="w-10 h-10 rounded-full bg-slate-100 border border-slate-300 flex items-center justify-center text-gov-navy shadow-inner font-serif font-black text-sm">
              🏛️
            </div>
            <span className="text-[9px] font-bold text-slate-600 tracking-tight mt-0.5">सत्यमेव जयते</span>
          </div>

          <div>
            <div className="flex items-center space-x-2">
              <span className="bg-blue-900 text-white text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded">
                National Portal
              </span>
              <span className="text-xs font-semibold text-gov-green flex items-center gap-1">
                <ShieldCheck className="w-3.5 h-3.5 text-gov-green" />
                DoLR Digital Governance Node
              </span>
            </div>
            <h1 className="text-lg sm:text-xl font-extrabold text-gov-navy tracking-tight leading-tight mt-0.5">
              {isHi
                ? "अनुसंधान, नीति नवाचार एवं साक्ष्य-आधारित भूमि शासन हेतु राष्ट्रीय डिजिटल मंच"
                : "National Digital Platform for Research, Policy Innovation & Land Governance"}
            </h1>
            <p className="text-xs text-slate-500 font-medium">
              {isHi
                ? "भूमि संसाधन विभाग | ग्रामीण विकास मंत्रालय, भारत सरकार"
                : "Department of Land Resources (DoLR) | Ministry of Rural Development, Govt. of India"}
            </p>
          </div>
        </div>

        {/* Quick Badges & National Initiatives */}
        <div className="hidden lg:flex items-center space-x-3 text-xs">
          <div className="bg-slate-50 border border-slate-200 rounded-lg p-2 flex items-center space-x-2.5 shadow-sm">
            <div className="w-8 h-8 rounded bg-emerald-100 flex items-center justify-center text-emerald-800 font-bold text-xs">
              भू
            </div>
            <div>
              <div className="text-[10px] text-slate-500 uppercase font-semibold">Flagship Standard</div>
              <div className="font-bold text-slate-800">Bhu-Aadhaar (ULPIN)</div>
            </div>
          </div>

          <div className="bg-slate-50 border border-slate-200 rounded-lg p-2 flex items-center space-x-2.5 shadow-sm">
            <div className="w-8 h-8 rounded bg-blue-100 flex items-center justify-center text-blue-800 font-bold text-xs">
              ⚖️
            </div>
            <div>
              <div className="text-[10px] text-slate-500 uppercase font-semibold">Dispute Telemetry</div>
              <div className="font-bold text-slate-800">e-Courts NJDG Sync</div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
