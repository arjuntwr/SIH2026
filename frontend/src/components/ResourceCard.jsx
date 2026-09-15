import React, { useState } from 'react';
import { 
  FileText, 
  Map, 
  Download, 
  Eye, 
  Copy, 
  Check, 
  ShieldCheck, 
  Scale, 
  Layers, 
  Share2, 
  ExternalLink,
  ChevronRight,
  Sparkles
} from 'lucide-react';

export default function ResourceCard({ resource, onSelectResource, isHi = false }) {
  const [copiedSha, setCopiedSha] = useState(false);

  const getStreamBadge = (stream) => {
    switch (stream) {
      case 'policy-legislation':
        return { label: 'Policy & Legislation', color: 'bg-blue-100 text-blue-900 border-blue-200' };
      case 'academic-research':
        return { label: 'Academic & Research', color: 'bg-emerald-100 text-emerald-900 border-emerald-200' };
      case 'judicial-records':
        return { label: 'Judicial & Disputes', color: 'bg-purple-100 text-purple-900 border-purple-200' };
      case 'government-datasets':
        return { label: 'Cadastral Dataset', color: 'bg-amber-100 text-amber-900 border-amber-200' };
      case 'pilot-case-studies':
        return { label: 'Pilot Case Study', color: 'bg-cyan-100 text-cyan-900 border-cyan-200' };
      default:
        return { label: 'Repository Item', color: 'bg-slate-100 text-slate-900 border-slate-200' };
    }
  };

  const badge = getStreamBadge(resource.taxonomy_stream);

  const copyChecksum = (e) => {
    e.stopPropagation();
    navigator.clipboard.writeText(resource.sha256_checksum);
    setCopiedSha(true);
    setTimeout(() => setCopiedSha(false), 2000);
  };

  return (
    <article
      onClick={() => onSelectResource(resource)}
      className="bg-white rounded-xl border border-slate-200 hover:border-blue-400 shadow-gov-sm hover:shadow-gov-md transition-all cursor-pointer flex flex-col justify-between overflow-hidden group"
    >
      {/* Top Header Card Strip */}
      <div className="p-4 sm:p-5">
        <div className="flex flex-wrap items-center justify-between gap-2 mb-2.5">
          <div className="flex items-center space-x-2">
            <span className={`text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded border ${badge.color}`}>
              {badge.label}
            </span>
            <span className="text-[11px] font-semibold text-slate-600 bg-slate-100 px-2 py-0.5 rounded">
              {resource.document_type}
            </span>
          </div>

          {/* Geography / State / LGD Badge */}
          <div className="flex items-center space-x-1.5 text-[11px] text-slate-500 font-medium">
            <span className="text-slate-700 font-semibold">{resource.state_ut || 'National'}</span>
            {resource.district && <span>• {resource.district}</span>}
            {resource.lgd_code && (
              <span className="bg-slate-100 text-slate-600 font-mono text-[10px] px-1 rounded" title="LGD Directory Code">
                LGD:{resource.lgd_code}
              </span>
            )}
          </div>
        </div>

        {/* Title */}
        <h3 className="text-sm sm:text-base font-bold text-gov-navy group-hover:text-blue-700 transition-colors leading-snug line-clamp-2 mb-1.5">
          {isHi && resource.title_hi ? resource.title_hi : resource.title}
        </h3>

        {/* Legal Authority / Originating Body */}
        <div className="text-xs text-slate-600 font-medium mb-3 flex items-center gap-1.5">
          <span className="text-gov-green font-semibold">🏛️ {resource.legal_authority}</span>
          {resource.case_number && <span className="text-slate-400 font-mono text-[11px]">| {resource.case_number}</span>}
          {resource.gazette_number && <span className="text-slate-400 font-mono text-[11px]">| {resource.gazette_number}</span>}
        </div>

        {/* Abstract */}
        <p className="text-xs text-slate-600 leading-relaxed line-clamp-3 mb-3">
          {isHi && resource.abstract_hi ? resource.abstract_hi : resource.abstract}
        </p>

        {/* AI Key Takeaway Highlight (if present) */}
        {resource.ai_executive_summary?.key_takeaways?.[0] && (
          <div className="bg-blue-50/80 border-l-2 border-blue-600 p-2 rounded-r text-[11px] text-slate-700 mb-3 flex items-start space-x-1.5">
            <Sparkles className="w-3.5 h-3.5 text-blue-600 shrink-0 mt-0.5" />
            <span className="line-clamp-2">
              <strong className="text-blue-950 font-semibold">AI Takeaway: </strong>
              {resource.ai_executive_summary.key_takeaways[0]}
            </span>
          </div>
        )}

        {/* Metadata Badges: Spatial, ULPIN, OCR */}
        <div className="flex flex-wrap items-center gap-2 text-[10px]">
          {resource.has_spatial_layer && (
            <span className="inline-flex items-center space-x-1 bg-emerald-50 text-emerald-800 border border-emerald-200 px-2 py-0.5 rounded font-bold">
              <Map className="w-3 h-3 text-emerald-600" />
              <span>Cadastral GIS Vector Layer</span>
            </span>
          )}

          {resource.ulpin && (
            <span className="inline-flex items-center space-x-1 bg-slate-100 text-slate-700 font-mono px-2 py-0.5 rounded">
              <span>Bhu-Aadhaar:</span>
              <strong className="text-slate-900">{resource.ulpin}</strong>
            </span>
          )}

          <span className="inline-flex items-center space-x-1 bg-slate-100 text-slate-600 px-1.5 py-0.5 rounded" title={`Confidence: ${resource.ocr_confidence}%`}>
            <ShieldCheck className="w-3 h-3 text-emerald-600" />
            <span>OCR {resource.ocr_confidence}%</span>
          </span>
        </div>
      </div>

      {/* Card Footer with SHA-256 Checksum and Action */}
      <div className="bg-slate-50 border-t border-slate-100 px-4 py-2.5 flex items-center justify-between text-xs">
        
        {/* Checksum Tool */}
        <button
          onClick={copyChecksum}
          className="flex items-center space-x-1 text-[10px] font-mono text-slate-500 hover:text-slate-800 bg-white border border-slate-200 px-1.5 py-0.5 rounded transition-colors"
          title={`Click to copy SHA-256 Checksum: ${resource.sha256_checksum}`}
        >
          {copiedSha ? <Check className="w-2.5 h-2.5 text-emerald-600" /> : <Copy className="w-2.5 h-2.5" />}
          <span>SHA-256: {resource.sha256_checksum.slice(0, 8)}...</span>
        </button>

        {/* Primary CTA */}
        <div className="flex items-center space-x-2 text-gov-navy font-bold text-xs group-hover:text-blue-700">
          <span>{isHi ? "दस्तावेज़ साक्ष्य देखें" : "Inspect Evidence"}</span>
          <ChevronRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
        </div>

      </div>
    </article>
  );
}
