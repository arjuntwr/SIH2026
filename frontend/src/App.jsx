import React, { useState } from 'react';
import GISMap from './components/GISMap';
import KnowledgeRepository from './components/KnowledgeRepository';
import { Map, BookOpen } from 'lucide-react';

export default function App() {
  const [activeView, setActiveView] = useState('gis'); // 'gis' | 'repository'

  return (
    <div className="h-screen w-screen flex flex-col relative overflow-hidden">
      {/* Global Navigation Switcher Pill */}
      <div className="fixed top-2.5 right-4 z-40 bg-slate-900/90 backdrop-blur-md p-1 rounded-lg border border-slate-700 shadow-xl flex items-center space-x-1 text-xs">
        <button
          onClick={() => setActiveView('gis')}
          className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-md font-bold transition cursor-pointer ${
            activeView === 'gis'
              ? 'bg-amber-500 text-slate-950 shadow-xs'
              : 'text-slate-300 hover:text-white hover:bg-slate-800'
          }`}
        >
          <Map className="w-3.5 h-3.5" />
          <span>GIS Map View</span>
        </button>

        <button
          onClick={() => setActiveView('repository')}
          className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-md font-bold transition cursor-pointer ${
            activeView === 'repository'
              ? 'bg-amber-500 text-slate-950 shadow-xs'
              : 'text-slate-300 hover:text-white hover:bg-slate-800'
          }`}
        >
          <BookOpen className="w-3.5 h-3.5" />
          <span>Catalog Repository</span>
        </button>
      </div>

      {/* Active Component */}
      <main className="flex-1 w-full h-full relative overflow-hidden">
        {activeView === 'gis' ? <GISMap /> : <KnowledgeRepository />}
      </main>
    </div>
  );
}
