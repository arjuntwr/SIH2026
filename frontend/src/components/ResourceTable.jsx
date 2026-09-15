import React from 'react';
import { Map, ShieldCheck, FileText, ChevronRight, Download, ExternalLink } from 'lucide-react';

export default function ResourceTable({ resources, onSelectResource, isHi = false }) {
  if (!resources || resources.length === 0) {
    return (
      <div className="bg-white rounded-xl border border-slate-200 p-8 text-center text-slate-500 text-sm">
        No matching records found in this repository stream.
      </div>
    );
  }

  const getStreamColor = (stream) => {
    switch (stream) {
      case 'policy-legislation': return 'text-blue-700 bg-blue-50';
      case 'academic-research': return 'text-emerald-700 bg-emerald-50';
      case 'judicial-records': return 'text-purple-700 bg-purple-50';
      case 'government-datasets': return 'text-amber-700 bg-amber-50';
      default: return 'text-cyan-700 bg-cyan-50';
    }
  };

  return (
    <div className="bg-white rounded-xl border border-slate-200 shadow-gov-sm overflow-hidden">
      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs">
          <thead className="bg-[#0B2545] text-white uppercase text-[10px] tracking-wider font-bold">
            <tr>
              <th className="py-3 px-4">Title & Classification</th>
              <th className="py-3 px-3">Jurisdiction</th>
              <th className="py-3 px-3">Authority / Agency</th>
              <th className="py-3 px-3">Date</th>
              <th className="py-3 px-3 text-center">GIS Layer</th>
              <th className="py-3 px-3">Integrity</th>
              <th className="py-3 px-3 text-right">Action</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-200 font-medium text-slate-700">
            {resources.map((item) => (
              <tr
                key={item.id}
                onClick={() => onSelectResource(item)}
                className="hover:bg-blue-50/50 cursor-pointer transition-colors"
              >
                {/* Title & Classification */}
                <td className="py-3 px-4 max-w-sm">
                  <div className="flex items-center space-x-2 mb-1">
                    <span className={`text-[10px] font-bold px-1.5 py-0.5 rounded ${getStreamColor(item.taxonomy_stream)}`}>
                      {item.document_type}
                    </span>
                    {item.ulpin && (
                      <span className="text-[10px] font-mono bg-slate-100 px-1 rounded text-slate-600">
                        {item.ulpin}
                      </span>
                    )}
                  </div>
                  <div className="font-bold text-gov-navy hover:text-blue-700 leading-snug line-clamp-2">
                    {isHi && item.title_hi ? item.title_hi : item.title}
                  </div>
                </td>

                {/* Jurisdiction */}
                <td className="py-3 px-3 whitespace-nowrap">
                  <div className="font-semibold text-slate-800">{item.state_ut || 'National'}</div>
                  {item.district && <div className="text-[10px] text-slate-500">{item.district}</div>}
                  {item.lgd_code && <div className="text-[10px] font-mono text-slate-400">LGD: {item.lgd_code}</div>}
                </td>

                {/* Authority */}
                <td className="py-3 px-3 max-w-xs">
                  <div className="text-slate-800 font-medium truncate" title={item.legal_authority}>
                    {item.legal_authority}
                  </div>
                  {item.case_number && (
                    <div className="text-[10px] font-mono text-slate-500 truncate">{item.case_number}</div>
                  )}
                </td>

                {/* Date */}
                <td className="py-3 px-3 whitespace-nowrap font-mono text-slate-600">
                  {item.publication_date}
                </td>

                {/* GIS Layer */}
                <td className="py-3 px-3 text-center whitespace-nowrap">
                  {item.has_spatial_layer ? (
                    <span className="inline-flex items-center text-emerald-700 bg-emerald-100/80 px-2 py-0.5 rounded-full text-[10px] font-bold">
                      <Map className="w-3 h-3 mr-1" /> Active Vector
                    </span>
                  ) : (
                    <span className="text-slate-400 text-[10px]">—</span>
                  )}
                </td>

                {/* Integrity & OCR */}
                <td className="py-3 px-3 whitespace-nowrap">
                  <div className="flex items-center text-emerald-700 text-[11px] font-semibold">
                    <ShieldCheck className="w-3.5 h-3.5 mr-1" />
                    <span>OCR {item.ocr_confidence}%</span>
                  </div>
                  <div className="text-[10px] font-mono text-slate-400">
                    {item.sha256_checksum.slice(0, 8)}...
                  </div>
                </td>

                {/* Action */}
                <td className="py-3 px-3 text-right whitespace-nowrap">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onSelectResource(item);
                    }}
                    className="bg-gov-navy hover:bg-blue-800 text-white font-semibold text-[11px] px-2.5 py-1 rounded transition-colors inline-flex items-center space-x-1"
                  >
                    <span>Inspect</span>
                    <ChevronRight className="w-3 h-3" />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
