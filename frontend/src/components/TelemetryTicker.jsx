import React from 'react';
import { Activity, RefreshCw, CheckCircle2, AlertCircle, Clock, Database, Radio } from 'lucide-react';

export default function TelemetryTicker({
  telemetry,
  onTriggerSync,
  isSyncing,
  onOpenSyncLogs
}) {
  const endpoints = telemetry?.endpoints || [];

  return (
    <div className="w-full bg-[#0B2545] text-white border-b border-slate-800 py-2 px-4 sm:px-6 lg:px-8 text-xs">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-2.5">
        
        {/* Status indicator heading */}
        <div className="flex items-center space-x-2 shrink-0">
          <div className="flex items-center space-x-1.5 bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded-full border border-emerald-500/40">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span className="font-bold tracking-wider uppercase text-[10px]">Live Govt Feeds</span>
          </div>
          <span className="text-slate-400 hidden lg:inline">|</span>
          <span className="text-slate-300 font-medium hidden lg:inline">
            Public Telemetry & Batch Ingestion Grid:
          </span>
        </div>

        {/* Dynamic Endpoint Badges */}
        <div className="flex flex-wrap items-center gap-2 sm:gap-3">
          {endpoints.map((ep, idx) => (
            <div
              key={idx}
              className="flex items-center space-x-1.5 bg-slate-900/80 hover:bg-slate-800/80 border border-slate-700/80 px-2 py-1 rounded transition-colors"
              title={`Target: ${ep.target_url}\nLatency: ${ep.response_time_ms}ms\nRecords: ${ep.records_indexed.toLocaleString()}`}
            >
              <span className={`w-1.5 h-1.5 rounded-full ${
                ep.status === 'OPERATIONAL' ? 'bg-emerald-400' :
                ep.status === 'SYNCING' ? 'bg-amber-400 animate-spin' : 'bg-red-400'
              }`} />
              <span className="font-semibold text-slate-200 text-[11px]">{ep.endpoint_category}:</span>
              <span className="text-emerald-400 font-mono text-[11px] font-medium">
                {ep.records_indexed > 1000000 
                  ? `${(ep.records_indexed / 1000000).toFixed(2)}M` 
                  : ep.records_indexed.toLocaleString()}
              </span>
              <span className="text-slate-500 text-[10px]">({ep.response_time_ms}ms)</span>
            </div>
          ))}
        </div>

        {/* Actions: Trigger Ingestion & View Logs */}
        <div className="flex items-center space-x-2 shrink-0 self-end md:self-auto">
          <button
            onClick={onTriggerSync}
            disabled={isSyncing}
            className={`flex items-center space-x-1.5 bg-amber-500 hover:bg-amber-400 text-slate-950 px-2.5 py-1 rounded font-bold text-[11px] transition-all shadow-sm ${
              isSyncing ? 'opacity-70 cursor-not-allowed' : 'active:scale-95'
            }`}
            title="Poll and trigger real-time harvest from e-Courts, data.gov.in and DoLR Gazettes"
          >
            <RefreshCw className={`w-3 h-3 ${isSyncing ? 'animate-spin' : ''}`} />
            <span>{isSyncing ? 'Syncing...' : 'Trigger Live Sync'}</span>
          </button>

          <button
            onClick={onOpenSyncLogs}
            className="text-slate-400 hover:text-white underline text-[11px] font-medium"
          >
            Telemetry Logs
          </button>
        </div>

      </div>
    </div>
  );
}
