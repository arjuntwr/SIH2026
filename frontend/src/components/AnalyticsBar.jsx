import React, { useState } from 'react';
import { Scale, TrendingUp, BookOpen, Database, CheckCircle, ChevronDown, ChevronUp, BarChart3 } from 'lucide-react';

export default function AnalyticsBar({ analytics }) {
  const [expanded, setExpanded] = useState(false);

  if (!analytics) return null;

  const {
    nationwide_active_disputes = 2409790,
    nationwide_disposal_rate = 74.2,
    total_indexed_literature = 4820,
    active_cadastral_datasets = 894,
    state_dispute_metrics = [],
    dispute_trend_monthly = [],
    top_dispute_themes = []
  } = analytics;

  return (
    <section className="w-full bg-white border-b border-slate-200 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
        {/* KPI Micro Summary Tiles */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
          
          {/* 1. Dispute Velocity & Volume */}
          <div className="bg-slate-50 border border-slate-200/80 rounded-lg p-3 hover:border-blue-300 transition-all">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">
                Active Land Disputes (NJDG)
              </span>
              <div className="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center text-blue-700">
                <Scale className="w-3.5 h-3.5" />
              </div>
            </div>
            <div className="mt-1 flex items-baseline space-x-2">
              <span className="text-xl font-extrabold text-gov-navy tracking-tight">
                {(nationwide_active_disputes / 1000000).toFixed(2)}M
              </span>
              <span className="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-1.5 py-0.5 rounded flex items-center">
                <TrendingUp className="w-2.5 h-2.5 mr-0.5" /> +4.7% MoM
              </span>
            </div>
            <div className="text-[10px] text-slate-500 mt-1">Across 748 District & Revenue Courts</div>
          </div>

          {/* 2. Disposal Rate Benchmark */}
          <div className="bg-slate-50 border border-slate-200/80 rounded-lg p-3 hover:border-emerald-300 transition-all">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">
                Overall Disposal Velocity
              </span>
              <div className="w-6 h-6 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-700">
                <CheckCircle className="w-3.5 h-3.5" />
              </div>
            </div>
            <div className="mt-1 flex items-baseline space-x-2">
              <span className="text-xl font-extrabold text-gov-green tracking-tight">
                {nationwide_disposal_rate}%
              </span>
              <span className="text-[10px] font-medium text-slate-500">
                Target: 80%
              </span>
            </div>
            {/* Progress bar */}
            <div className="w-full bg-slate-200 rounded-full h-1.5 mt-2 overflow-hidden">
              <div
                className="bg-gov-green h-1.5 rounded-full transition-all duration-500"
                style={{ width: `${nationwide_disposal_rate}%` }}
              ></div>
            </div>
          </div>

          {/* 3. Research Literature Indexed */}
          <div className="bg-slate-50 border border-slate-200/80 rounded-lg p-3 hover:border-amber-300 transition-all">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">
                Research & Policy Papers
              </span>
              <div className="w-6 h-6 rounded-full bg-amber-100 flex items-center justify-center text-amber-700">
                <BookOpen className="w-3.5 h-3.5" />
              </div>
            </div>
            <div className="mt-1 flex items-baseline space-x-2">
              <span className="text-xl font-extrabold text-slate-800 tracking-tight">
                {total_indexed_literature.toLocaleString()}
              </span>
              <span className="text-[10px] font-semibold text-amber-800 bg-amber-50 px-1.5 py-0.5 rounded">
                LandVoc Tagged
              </span>
            </div>
            <div className="text-[10px] text-slate-500 mt-1">Peer-reviewed studies & circulars</div>
          </div>

          {/* 4. Active Cadastral Datasets */}
          <div className="bg-slate-50 border border-slate-200/80 rounded-lg p-3 hover:border-purple-300 transition-all">
            <div className="flex items-center justify-between">
              <span className="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">
                Cadastral Spatial Baselines
              </span>
              <div className="w-6 h-6 rounded-full bg-purple-100 flex items-center justify-center text-purple-700">
                <Database className="w-3.5 h-3.5" />
              </div>
            </div>
            <div className="mt-1 flex items-baseline space-x-2">
              <span className="text-xl font-extrabold text-slate-800 tracking-tight">
                {active_cadastral_datasets.toLocaleString()}
              </span>
              <span className="text-[10px] font-semibold text-purple-800 bg-purple-50 px-1.5 py-0.5 rounded">
                GeoJSON / SHP
              </span>
            </div>
            <div className="text-[10px] text-slate-500 mt-1">Village RoR & Vector Maps</div>
          </div>

        </div>

        {/* Toggle Detailed Analytics Expand */}
        <div className="mt-2.5 flex justify-center">
          <button
            onClick={() => setExpanded(!expanded)}
            className="flex items-center space-x-1 text-xs font-semibold text-gov-navy hover:text-blue-700 transition-colors bg-slate-100/80 hover:bg-slate-200/80 px-3 py-1 rounded-full border border-slate-200"
          >
            <BarChart3 className="w-3.5 h-3.5" />
            <span>{expanded ? "Collapse Detailed Dispute & Reform Charts" : "View Live State Scorecards & Trend Velocity"}</span>
            {expanded ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
          </button>
        </div>

        {/* Expandable Deep Dive Analytics Drawer */}
        {expanded && (
          <div className="mt-4 pt-4 border-t border-slate-200 grid grid-cols-1 lg:grid-cols-3 gap-4">
            
            {/* 1. Monthly Dispute Velocity Chart */}
            <div className="bg-slate-50 p-3.5 rounded-lg border border-slate-200">
              <div className="flex items-center justify-between mb-2">
                <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wider">
                  NJDG Case Filing vs Disposal Velocity (Past 6 Months)
                </h4>
              </div>
              <div className="space-y-2 mt-3">
                {dispute_trend_monthly.map((trend, i) => (
                  <div key={i} className="text-xs">
                    <div className="flex justify-between text-[11px] font-medium text-slate-600 mb-0.5">
                      <span>{trend.month}</span>
                      <span className="text-slate-500 font-mono">
                        Filed: {trend.filed.toLocaleString()} | Disposed: {trend.disposed.toLocaleString()}
                      </span>
                    </div>
                    <div className="w-full bg-slate-200 rounded-full h-2 flex overflow-hidden">
                      <div
                        className="bg-blue-600 h-2"
                        style={{ width: `${(trend.filed / 50000) * 100}%` }}
                        title={`Filed: ${trend.filed}`}
                      />
                      <div
                        className="bg-emerald-500 h-2"
                        style={{ width: `${(trend.disposed / 50000) * 100}%` }}
                        title={`Disposed: ${trend.disposed}`}
                      />
                    </div>
                  </div>
                ))}
              </div>
              <div className="flex items-center justify-end space-x-4 mt-3 text-[10px] text-slate-500">
                <span className="flex items-center"><span className="w-2.5 h-2.5 bg-blue-600 rounded mr-1"></span> Cases Filed</span>
                <span className="flex items-center"><span className="w-2.5 h-2.5 bg-emerald-500 rounded mr-1"></span> Cases Disposed</span>
              </div>
            </div>

            {/* 2. Top Dispute Categories Breakdown */}
            <div className="bg-slate-50 p-3.5 rounded-lg border border-slate-200">
              <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">
                National Land Dispute Thematic Classification
              </h4>
              <div className="space-y-2.5 mt-3">
                {top_dispute_themes.map((theme, i) => (
                  <div key={i}>
                    <div className="flex justify-between text-[11px] mb-0.5">
                      <span className="font-semibold text-slate-700">{theme.theme}</span>
                      <span className="text-slate-500 font-mono">{theme.percentage}% ({(theme.count / 1000).toFixed(0)}k)</span>
                    </div>
                    <div className="w-full bg-slate-200 rounded-full h-1.5">
                      <div
                        className="bg-gov-navy h-1.5 rounded-full"
                        style={{ width: `${theme.percentage * 2}%` }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* 3. State Land Reform Scorecard */}
            <div className="bg-slate-50 p-3.5 rounded-lg border border-slate-200">
              <h4 className="text-xs font-bold text-slate-800 uppercase tracking-wider mb-2">
                State Land Reform & Bhu-Aadhaar Adoption Scorecard
              </h4>
              <div className="overflow-x-auto mt-2">
                <table className="w-full text-[11px] text-left">
                  <thead>
                    <tr className="text-slate-500 border-b border-slate-200">
                      <th className="pb-1.5 font-semibold">State/UT</th>
                      <th className="pb-1.5 font-semibold text-center">Bhu-Aadhaar %</th>
                      <th className="pb-1.5 font-semibold text-right">Reform Index</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-200/60">
                    {state_dispute_metrics.slice(0, 5).map((sm, i) => (
                      <tr key={i} className="hover:bg-white transition-colors">
                        <td className="py-1 font-medium text-slate-800">{sm.state_ut}</td>
                        <td className="py-1 text-center font-mono text-emerald-700 font-semibold">
                          {sm.bhu_aadhaar_seeding_percentage}%
                        </td>
                        <td className="py-1 text-right">
                          <span className={`px-1.5 py-0.5 rounded font-bold text-[10px] ${
                            sm.reform_adoption_score >= 90 ? 'bg-emerald-100 text-emerald-800' :
                            sm.reform_adoption_score >= 80 ? 'bg-blue-100 text-blue-800' :
                            'bg-amber-100 text-amber-800'
                          }`}>
                            {sm.reform_adoption_score}/100
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

          </div>
        )}

      </div>
    </section>
  );
}
