import React from 'react';
import GISMap from './GISMap';

/**
 * GISMapSection
 * Refactored clean GIS viewer adhering to the strict 3-layer architecture:
 * 1. Base Layer: ESRI World Imagery (Satellite)
 * 2. Thematic Overlay: ESRI Sentinel-2 10m LULC (0.25 default opacity)
 * 3. Boundary Layer: Clean glowing cyan vector outline (#0284c7 / #38bdf8)
 *
 * All extraneous layers (dispute pins, conflict markers, litigation heatmaps) purged.
 */
export default function GISMapSection() {
  return <GISMap />;
}
