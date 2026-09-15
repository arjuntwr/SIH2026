import React, { useEffect, useRef, useState } from 'react';
import { Map, Info, AlertTriangle, CheckCircle2, Maximize2 } from 'lucide-react';
import L from 'leaflet';

export default function CadastralMap({ geojson, title = "Cadastral Boundary Viewer" }) {
  const mapContainerRef = useRef(null);
  const mapInstanceRef = useRef(null);
  const geojsonLayerRef = useRef(null);
  const [selectedParcel, setSelectedParcel] = useState(null);

  useEffect(() => {
    if (!mapContainerRef.current) return;

    // Clean up previous map instance if any
    if (mapInstanceRef.current) {
      mapInstanceRef.current.remove();
      mapInstanceRef.current = null;
    }

    // Default center (India)
    const map = L.map(mapContainerRef.current, {
      center: [25.3214, 82.8821],
      zoom: 14,
      zoomControl: true,
      attributionControl: true
    });

    mapInstanceRef.current = map;

    // Add high-resolution OpenStreetMap / Bhuvan-compatible base tile
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; National Land Governance Platform | OpenStreetMap contributors',
      maxZoom: 19
    }).addTo(map);

    // If GeoJSON is supplied, render polygons with interactive styling
    if (geojson && geojson.features && geojson.features.length > 0) {
      const geoLayer = L.geoJSON(geojson, {
        style: (feature) => {
          const isDisputed = feature.properties?.dispute_flag;
          return {
            color: isDisputed ? '#DC2626' : '#0B2545',
            weight: 2,
            opacity: 0.9,
            fillColor: isDisputed ? '#FCA5A5' : '#10B981',
            fillOpacity: 0.35,
            dashArray: isDisputed ? '4, 4' : null
          };
        },
        onEachFeature: (feature, layer) => {
          // Hover highlighting
          layer.on({
            mouseover: (e) => {
              const l = e.target;
              l.setStyle({
                weight: 4,
                fillOpacity: 0.6,
                color: '#D97706'
              });
              l.bringToFront();
            },
            mouseout: (e) => {
              geoLayer.resetStyle(e.target);
            },
            click: () => {
              setSelectedParcel(feature.properties);
            }
          });
        }
      }).addTo(map);

      geojsonLayerRef.current = geoLayer;

      // Fit map bounds to polygons
      const bounds = geoLayer.getBounds();
      if (bounds.isValid()) {
        map.fitBounds(bounds, { padding: [30, 30] });
      }

      // Default select first feature
      setSelectedParcel(geojson.features[0].properties);
    }

    // Force map resize check
    setTimeout(() => {
      map.invalidateSize();
    }, 200);

    return () => {
      if (mapInstanceRef.current) {
        mapInstanceRef.current.remove();
        mapInstanceRef.current = null;
      }
    };
  }, [geojson]);

  return (
    <div className="flex flex-col h-full bg-slate-50 rounded-lg overflow-hidden border border-slate-200">
      
      {/* Map Control Strip */}
      <div className="bg-slate-100 px-3 py-2 border-b border-slate-200 flex items-center justify-between text-xs">
        <div className="flex items-center space-x-2">
          <Map className="w-4 h-4 text-gov-navy" />
          <span className="font-bold text-slate-800">
            {title} (WGS-84 / EPSG:4326)
          </span>
        </div>
        <div className="flex items-center space-x-2 text-[11px]">
          <span className="flex items-center text-emerald-700">
            <span className="w-2.5 h-2.5 bg-emerald-500 rounded-sm mr-1"></span> Undisputed Parcel
          </span>
          <span className="flex items-center text-red-700">
            <span className="w-2.5 h-2.5 bg-red-500 rounded-sm mr-1"></span> e-Courts Disputed
          </span>
        </div>
      </div>

      {/* Map Canvas */}
      <div className="relative flex-1 min-h-[340px]">
        <div ref={mapContainerRef} className="absolute inset-0" />

        {/* Selected Parcel Overlay Inspector Box */}
        {selectedParcel && (
          <div className="absolute bottom-3 left-3 right-3 sm:right-auto sm:max-w-xs bg-white/95 backdrop-blur-md p-3 rounded-lg border border-slate-300 shadow-gov-md z-[1000] text-xs">
            <div className="flex items-center justify-between border-b border-slate-200 pb-1.5 mb-2">
              <span className="font-bold text-gov-navy">Parcel Cadastral Metadata</span>
              {selectedParcel.dispute_flag ? (
                <span className="bg-red-100 text-red-800 font-bold px-1.5 py-0.5 rounded text-[10px] flex items-center">
                  <AlertTriangle className="w-3 h-3 mr-0.5" /> Disputed
                </span>
              ) : (
                <span className="bg-emerald-100 text-emerald-800 font-bold px-1.5 py-0.5 rounded text-[10px] flex items-center">
                  <CheckCircle2 className="w-3 h-3 mr-0.5" /> Clear Title
                </span>
              )}
            </div>

            <div className="grid grid-cols-2 gap-y-1.5 text-[11px]">
              <div>
                <span className="text-slate-400 block text-[10px]">Survey / Khasra No</span>
                <span className="font-mono font-bold text-slate-800">{selectedParcel.survey_no || 'N/A'}</span>
              </div>
              <div>
                <span className="text-slate-400 block text-[10px]">Khata No (RoR)</span>
                <span className="font-mono font-bold text-slate-800">{selectedParcel.khata_no || 'N/A'}</span>
              </div>
              <div className="col-span-2">
                <span className="text-slate-400 block text-[10px]">ULPIN (Bhu-Aadhaar)</span>
                <span className="font-mono font-bold text-blue-700 bg-blue-50 px-1 rounded block truncate">
                  {selectedParcel.ulpin || 'PENDING SEEDING'}
                </span>
              </div>
              <div>
                <span className="text-slate-400 block text-[10px]">Area</span>
                <span className="font-semibold text-slate-800">
                  {selectedParcel.area_hectares ? `${selectedParcel.area_hectares} Ha` : `${selectedParcel.area_sq_m || 0} m²`}
                </span>
              </div>
              <div>
                <span className="text-slate-400 block text-[10px]">Land Tenure Class</span>
                <span className="font-semibold text-slate-800 truncate block">{selectedParcel.owner_type || 'Agricultural'}</span>
              </div>
            </div>
          </div>
        )}
      </div>

    </div>
  );
}
