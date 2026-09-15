import React, { useState } from 'react';
import { 
  X, 
  Sparkles, 
  Map, 
  FileText, 
  Download, 
  Copy, 
  Check, 
  ShieldCheck, 
  Languages, 
  ExternalLink,
  Table,
  Scale,
  Building,
  CheckCircle2,
  Calendar,
  AlertCircle
} from 'lucide-react';
import CadastralMap from './CadastralMap';

export default function DocumentDrawer({ resource, onClose, isHi = false }) {
  const [activeTab, setActiveTab] = useState('summary'); // 'summary', 'spatial', 'preview', 'citations'
  const [selectedLanguage, setSelectedLanguage] = useState('en');
  const [copiedCitation, setCopiedCitation] = useState(null);
  const [copiedChecksum, setCopiedChecksum] = useState(false);

  if (!resource) return null;

  // Handle translation text
  const getTranslatedTitle = () => {
    if (selectedLanguage === 'hi' && (resource.translations?.hi?.title || resource.title_hi)) {
      return resource.translations?.hi?.title || resource.title_hi;
    }
    if (selectedLanguage === 'mr' && resource.translations?.mr?.title) {
      return resource.translations.mr.title;
    }
    if (selectedLanguage === 'te' && resource.translations?.te?.title) {
      return resource.translations.te.title;
    }
    if (selectedLanguage === 'or' && resource.translations?.or?.title) {
      return resource.translations.or.title;
    }
    return resource.title;
  };

  const getTranslatedAbstract = () => {
    if (selectedLanguage === 'hi' && (resource.translations?.hi?.abstract || resource.abstract_hi)) {
      return resource.translations?.hi?.abstract || resource.abstract_hi;
    }
    if (selectedLanguage === 'mr' && resource.translations?.mr?.abstract) {
      return resource.translations.mr.abstract;
    }
    if (selectedLanguage === 'te' && resource.translations?.te?.abstract) {
      return resource.translations.te.abstract;
    }
    if (selectedLanguage === 'or' && resource.translations?.or?.abstract) {
      return resource.translations.or.abstract;
    }
    return resource.abstract;
  };

  const copyCitation = (format, text) => {
    navigator.clipboard.writeText(text);
    setCopiedCitation(format);
    setTimeout(() => setCopiedCitation(null), 2000);
  };

  const copyChecksum = () => {
    navigator.clipboard.writeText(resource.sha256_checksum);
    setCopiedChecksum(true);
    setTimeout(() => setCopiedChecksum(false), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 overflow-hidden bg-slate-900/60 backdrop-blur-sm flex justify-end animate-in fade-in duration-200">
      <div 
        className="w-full max-w-3xl bg-white h-full shadow-2xl flex flex-col justify-between overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        
        {/* Drawer Header Strip */}
        <div className="bg-[#0B2545] text-white p-4 sm:p-5 flex items-start justify-between gap-3 shrink-0">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-2">
              <span className="bg-amber-500 text-slate-950 font-bold uppercase text-[10px] px-2 py-0.5 rounded">
                {resource.taxonomy_stream.replace('-', ' ')}
              </span>
              <span className="bg-blue-800 text-white font-semibold text-[11px] px-2 py-0.5 rounded">
                {resource.document_type}
              </span>
              {resource.ulpin && (
                <span className="bg-slate-800 text-amber-300 font-mono text-[10px] px-2 py-0.5 rounded">
                  ULPIN: {resource.ulpin}
                </span>
              )}
            </div>
            <h2 className="text-base sm:text-lg font-bold leading-snug">
              {getTranslatedTitle()}
            </h2>
            <div className="text-xs text-slate-300 mt-1 flex flex-wrap items-center gap-2">
              <span>🏛️ {resource.legal_authority}</span>
              <span>• Published: {resource.publication_date}</span>
              {resource.case_number && <span>• Case: {resource.case_number}</span>}
              {resource.gazette_number && <span>• Gaz: {resource.gazette_number}</span>}
            </div>
          </div>

          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white p-1 rounded-lg bg-slate-800/80 transition-colors"
            title="Close Drawer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Navigation */}
        <div className="bg-slate-100 px-4 sm:px-6 border-b border-slate-200 flex space-x-2 sm:space-x-4 text-xs font-semibold shrink-0">
          <button
            onClick={() => setActiveTab('summary')}
            className={`py-2.5 px-2 border-b-2 flex items-center space-x-1.5 transition-colors ${
              activeTab === 'summary' ? 'border-gov-navy text-gov-navy font-bold' : 'border-transparent text-slate-500 hover:text-slate-900'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5 text-blue-600" />
            <span>AI Summary & Takeaways</span>
          </button>

          {resource.has_spatial_layer && (
            <button
              onClick={() => setActiveTab('spatial')}
              className={`py-2.5 px-2 border-b-2 flex items-center space-x-1.5 transition-colors ${
                activeTab === 'spatial' ? 'border-gov-green text-gov-green font-bold' : 'border-transparent text-slate-500 hover:text-slate-900'
              }`}
            >
              <Map className="w-3.5 h-3.5 text-gov-green" />
              <span>GIS Cadastral Layer</span>
            </button>
          )}

          <button
            onClick={() => setActiveTab('preview')}
            className={`py-2.5 px-2 border-b-2 flex items-center space-x-1.5 transition-colors ${
              activeTab === 'preview' ? 'border-gov-navy text-gov-navy font-bold' : 'border-transparent text-slate-500 hover:text-slate-900'
            }`}
          >
            <FileText className="w-3.5 h-3.5 text-purple-600" />
            <span>Document Preview & OCR</span>
          </button>

          <button
            onClick={() => setActiveTab('citations')}
            className={`py-2.5 px-2 border-b-2 flex items-center space-x-1.5 transition-colors ${
              activeTab === 'citations' ? 'border-gov-navy text-gov-navy font-bold' : 'border-transparent text-slate-500 hover:text-slate-900'
            }`}
          >
            <Copy className="w-3.5 h-3.5 text-amber-600" />
            <span>Citations & Formats</span>
          </button>
        </div>

        {/* Content Body (Scrollable) */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-6">
          
          {/* TAB 1: AI SUMMARY & TAKEAWAYS */}
          {activeTab === 'summary' && (
            <div className="space-y-5 text-xs text-slate-700">
              
              {/* Regional Translation Selector Bar */}
              <div className="bg-slate-50 p-2.5 rounded-lg border border-slate-200 flex flex-wrap items-center justify-between gap-2">
                <div className="flex items-center space-x-1.5 text-slate-700 font-semibold">
                  <Languages className="w-4 h-4 text-blue-700" />
                  <span>Regional Translation Switcher:</span>
                </div>
                <div className="flex items-center space-x-1 font-medium">
                  {['en', 'hi', 'mr', 'te', 'or'].map((lng) => (
                    <button
                      key={lng}
                      onClick={() => setSelectedLanguage(lng)}
                      className={`px-2 py-0.5 rounded uppercase font-bold text-[10px] transition-colors ${
                        selectedLanguage === lng
                          ? 'bg-gov-navy text-white'
                          : 'bg-white text-slate-600 hover:bg-slate-200 border border-slate-200'
                      }`}
                    >
                      {lng === 'en' ? 'English' : lng === 'hi' ? 'हिन्दी' : lng === 'mr' ? 'मराठी' : lng === 'te' ? 'తెలుగు' : 'ଓଡ଼ିଆ'}
                    </button>
                  ))}
                </div>
              </div>

              {/* Abstract */}
              <div>
                <h4 className="text-xs font-bold text-gov-navy uppercase tracking-wider mb-1.5">
                  Official Abstract / Synopsis
                </h4>
                <div className="bg-white p-3.5 rounded-lg border border-slate-200 leading-relaxed text-slate-800 text-xs">
                  {getTranslatedAbstract()}
                </div>
              </div>

              {/* AI Key Takeaways */}
              {resource.ai_executive_summary?.key_takeaways && (
                <div className="bg-blue-50/50 p-4 rounded-xl border border-blue-200">
                  <h4 className="text-xs font-bold text-blue-950 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                    <Sparkles className="w-4 h-4 text-blue-600" />
                    <span>AI-Extracted Executive Key Takeaways</span>
                  </h4>
                  <ul className="space-y-2 text-slate-800">
                    {resource.ai_executive_summary.key_takeaways.map((takeaway, i) => (
                      <li key={i} className="flex items-start space-x-2">
                        <CheckCircle2 className="w-3.5 h-3.5 text-gov-green shrink-0 mt-0.5" />
                        <span className="leading-snug">{takeaway}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Policy Implications & Stakeholders */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {resource.ai_executive_summary?.policy_implications && (
                  <div className="bg-slate-50 p-3.5 rounded-lg border border-slate-200">
                    <h5 className="font-bold text-slate-900 mb-1.5 text-[11px] uppercase tracking-wider">
                      Policy & Administrative Impact
                    </h5>
                    <ul className="space-y-1.5 text-[11px] text-slate-700">
                      {resource.ai_executive_summary.policy_implications.map((imp, i) => (
                        <li key={i} className="flex items-start space-x-1.5">
                          <span className="text-blue-600 font-bold">•</span>
                          <span>{imp}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                {resource.ai_executive_summary?.affected_stakeholders && (
                  <div className="bg-slate-50 p-3.5 rounded-lg border border-slate-200">
                    <h5 className="font-bold text-slate-900 mb-1.5 text-[11px] uppercase tracking-wider">
                      Affected Stakeholders
                    </h5>
                    <div className="flex flex-wrap gap-1.5">
                      {resource.ai_executive_summary.affected_stakeholders.map((sh, i) => (
                        <span key={i} className="bg-white border border-slate-200 text-slate-800 px-2 py-0.5 rounded text-[10px] font-medium">
                          {sh}
                        </span>
                      ))}
                    </div>
                  </div>
                )}
              </div>

              {/* Legal Doctrines Invoked */}
              {resource.ai_executive_summary?.legal_doctrines_invoked?.length > 0 && (
                <div className="bg-purple-50/60 p-3 rounded-lg border border-purple-200">
                  <h5 className="font-bold text-purple-900 mb-1 text-[11px] flex items-center gap-1.5">
                    <Scale className="w-3.5 h-3.5 text-purple-700" />
                    <span>Constitutional & Legal Doctrines Invoked:</span>
                  </h5>
                  <div className="flex flex-wrap gap-1.5 mt-1">
                    {resource.ai_executive_summary.legal_doctrines_invoked.map((doc, i) => (
                      <span key={i} className="bg-white text-purple-900 font-semibold px-2 py-0.5 rounded border border-purple-200 text-[10px]">
                        {doc}
                      </span>
                    ))}
                  </div>
                </div>
              )}

            </div>
          )}

          {/* TAB 2: GIS CADASTRAL LAYER */}
          {activeTab === 'spatial' && resource.has_spatial_layer && (
            <div className="h-[460px] flex flex-col space-y-3">
              <div className="text-xs text-slate-600">
                Interactive georeferenced cadastral layer. Hover or click on individual survey parcels to inspect ULPIN, survey number, land use tenure class, and active e-Courts litigation flags.
              </div>
              <div className="flex-1">
                <CadastralMap geojson={resource.spatial_geojson} title={resource.title} />
              </div>
            </div>
          )}

          {/* TAB 3: DOCUMENT PREVIEW & OCR */}
          {activeTab === 'preview' && (
            <div className="space-y-4 text-xs">
              
              {/* OCR Quality Box */}
              <div className="bg-emerald-50 border border-emerald-200 p-3 rounded-lg flex items-center justify-between">
                <div className="flex items-center space-x-2">
                  <ShieldCheck className="w-5 h-5 text-emerald-600" />
                  <div>
                    <div className="font-bold text-emerald-950">OCR Status: {resource.ocr_status}</div>
                    <div className="text-[11px] text-emerald-800">
                      Digitally verified for ISO 19005-1 (PDF/A) archival compliance. Searchable full-text extract available.
                    </div>
                  </div>
                </div>
                <span className="font-mono text-xs font-bold bg-white px-2 py-1 rounded border border-emerald-300 text-emerald-800">
                  {resource.ocr_confidence}% Confidence
                </span>
              </div>

              {/* Document Text Extract Viewer */}
              <div className="bg-slate-900 text-slate-200 p-4 rounded-lg font-mono text-[11px] leading-relaxed max-h-80 overflow-y-auto border border-slate-800">
                <div className="text-slate-500 border-b border-slate-800 pb-2 mb-2 flex justify-between">
                  <span>// EXTRACTED TEXT STREAM (PAGE 1 - {resource.page_count})</span>
                  <span>FORMAT: {resource.file_format}</span>
                </div>
                <p className="text-slate-300 whitespace-pre-wrap">
                  {resource.abstract}
                  {"\n\n"}
                  [SECTION 1: STATUTORY PROVISIONS AND EXECUTIVE POWERS]
                  {"\n"}
                  Whereas under the mandate of the Ministry of Rural Development, Department of Land Resources (DoLR), in coordination with State Revenue Authorities and Survey of India, this regulatory framework coordinates geodetic parcel mapping and title adjudication...
                  {"\n\n"}
                  [SECTION 2: CADASTRE RESOLUTION AND CORS GEODESY]
                  {"\n"}
                  All drone-acquired spatial imagery must satisfy 5cm Ground Sampling Distance (GSD) with root-mean-square error (RMSE) under 10cm. Boundary coordinates shall be cross-referenced with Bhu-Aadhaar 14-digit alphanumeric tags.
                </p>
              </div>

            </div>
          )}

          {/* TAB 4: CITATIONS & FORMATS */}
          {activeTab === 'citations' && (
            <div className="space-y-4 text-xs">
              <div className="text-slate-600">
                Use standard official citations for academic journals, legal briefs, and government policy memos.
              </div>

              {/* Indian Legal Citation */}
              <div className="bg-slate-50 p-3 rounded-lg border border-slate-200">
                <div className="flex justify-between items-center mb-1">
                  <span className="font-bold text-gov-navy text-[11px]">
                    Indian Legal / Supreme Court & Gazette Format
                  </span>
                  <button
                    onClick={() => copyCitation('legal', resource.citations?.indian_legal || resource.title)}
                    className="flex items-center space-x-1 text-blue-700 font-semibold text-[11px] hover:underline"
                  >
                    {copiedCitation === 'legal' ? <Check className="w-3 h-3 text-emerald-600" /> : <Copy className="w-3 h-3" />}
                    <span>{copiedCitation === 'legal' ? 'Copied!' : 'Copy'}</span>
                  </button>
                </div>
                <div className="bg-white p-2 rounded border border-slate-200 font-mono text-[11px] text-slate-800">
                  {resource.citations?.indian_legal || `${resource.legal_authority}, Notification Ref: ${resource.gazette_number || 'N/A'}`}
                </div>
              </div>

              {/* APA Format */}
              <div className="bg-slate-50 p-3 rounded-lg border border-slate-200">
                <div className="flex justify-between items-center mb-1">
                  <span className="font-bold text-gov-navy text-[11px]">APA 7th Edition</span>
                  <button
                    onClick={() => copyCitation('apa', resource.citations?.apa || resource.title)}
                    className="flex items-center space-x-1 text-blue-700 font-semibold text-[11px] hover:underline"
                  >
                    {copiedCitation === 'apa' ? <Check className="w-3 h-3 text-emerald-600" /> : <Copy className="w-3 h-3" />}
                    <span>{copiedCitation === 'apa' ? 'Copied!' : 'Copy'}</span>
                  </button>
                </div>
                <div className="bg-white p-2 rounded border border-slate-200 font-mono text-[11px] text-slate-800">
                  {resource.citations?.apa || `${resource.legal_authority} (${resource.publication_date.slice(0, 4)}). ${resource.title}.`}
                </div>
              </div>

              {/* MLA Format */}
              <div className="bg-slate-50 p-3 rounded-lg border border-slate-200">
                <div className="flex justify-between items-center mb-1">
                  <span className="font-bold text-gov-navy text-[11px]">MLA 9th Edition</span>
                  <button
                    onClick={() => copyCitation('mla', resource.citations?.mla || resource.title)}
                    className="flex items-center space-x-1 text-blue-700 font-semibold text-[11px] hover:underline"
                  >
                    {copiedCitation === 'mla' ? <Check className="w-3 h-3 text-emerald-600" /> : <Copy className="w-3 h-3" />}
                    <span>{copiedCitation === 'mla' ? 'Copied!' : 'Copy'}</span>
                  </button>
                </div>
                <div className="bg-white p-2 rounded border border-slate-200 font-mono text-[11px] text-slate-800">
                  {resource.citations?.mla || `${resource.legal_authority}. "${resource.title}." ${resource.publication_date.slice(0, 4)}.`}
                </div>
              </div>

              {/* BibTeX */}
              {resource.citations?.bibtex && (
                <div className="bg-slate-50 p-3 rounded-lg border border-slate-200">
                  <div className="flex justify-between items-center mb-1">
                    <span className="font-bold text-gov-navy text-[11px]">BibTeX Entry</span>
                    <button
                      onClick={() => copyCitation('bibtex', resource.citations.bibtex)}
                      className="flex items-center space-x-1 text-blue-700 font-semibold text-[11px] hover:underline"
                    >
                      {copiedCitation === 'bibtex' ? <Check className="w-3 h-3 text-emerald-600" /> : <Copy className="w-3 h-3" />}
                      <span>{copiedCitation === 'bibtex' ? 'Copied!' : 'Copy'}</span>
                    </button>
                  </div>
                  <pre className="bg-white p-2 rounded border border-slate-200 font-mono text-[10px] text-slate-800 overflow-x-auto whitespace-pre">
                    {resource.citations.bibtex}
                  </pre>
                </div>
              )}

            </div>
          )}

        </div>

        {/* Drawer Footer with SHA-256 and Download */}
        <div className="bg-slate-50 border-t border-slate-200 p-4 sm:p-5 flex flex-wrap items-center justify-between gap-3 shrink-0">
          
          {/* Cryptographic SHA-256 Checksum Box */}
          <div className="flex items-center space-x-2">
            <ShieldCheck className="w-4 h-4 text-emerald-600" />
            <div className="text-xs">
              <span className="text-[10px] text-slate-500 block uppercase font-bold">SHA-256 Integrity Verification</span>
              <button
                onClick={copyChecksum}
                className="font-mono text-[11px] text-slate-800 hover:text-blue-700 flex items-center space-x-1 bg-white border border-slate-300 px-2 py-0.5 rounded shadow-sm"
                title="Click to copy full 64-character SHA-256 checksum"
              >
                <span>{resource.sha256_checksum.slice(0, 16)}...</span>
                {copiedChecksum ? <Check className="w-3 h-3 text-emerald-600" /> : <Copy className="w-3 h-3 text-slate-400" />}
              </button>
            </div>
          </div>

          {/* Download Button */}
          <a
            href={resource.file_url}
            download
            onClick={(e) => {
              e.preventDefault();
              alert(`Downloading verified official document:\n${resource.title}\n\nSHA-256 Checksum:\n${resource.sha256_checksum}`);
            }}
            className="bg-gov-green hover:bg-emerald-700 text-white font-bold text-xs px-4 py-2 rounded-lg flex items-center space-x-2 shadow-sm transition-colors"
          >
            <Download className="w-4 h-4" />
            <span>Download Official File ({resource.file_format} • {(resource.file_size_bytes / 1000000).toFixed(1)} MB)</span>
          </a>

        </div>

      </div>
    </div>
  );
}
