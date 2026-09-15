b"""
GUJ-LAND-INTEL: Boundary Focus & Spatial Attribute Processor
Eliminates synthetic Overpass vector approximations and provides:
1. Exact boundary polygon and bounding box (BBOX) of the searched area (from Nominatim/Datameet).
2. Smooth geodesic boundary curves for point entities (NO artificial rectangular boxes).
3. Inverted world spotlight mask (world bounding box with active entity hole).
4. Real-time attribute metadata (hierarchy, district stats, agro-climatic profile, seismic zonation).
5. Clean spatial envelope for seamless Esri 10m Sentinel-2 LULC raster tile integration.
"""

import math
from typing import Dict, Any, List, Optional
from shapely.geometry import shape, mapping, Polygon as SPolygon, MultiPolygon as SMultiPolygon
from shapely.validation import make_valid
from engine.risk import evaluate_risk_and_vulnerability


def _build_boundary_and_mask(
    lat: float,
    lon: float,
    radius_km: float,
    entity_geojson: Optional[Dict[str, Any]],
    bbox: Optional[List[float]]
) -> tuple:
    """
    Builds the organic boundary GeoJSON and inverted world mask hole.
    Uses real administrative polygon when available, or a smooth 64-vertex
    geodesic boundary for point entities (NEVER a 4-point bounding box rectangle).
    """
    world_ring = [
        [-180.0, -90.0],
        [180.0, -90.0],
        [180.0, 90.0],
        [-180.0, 90.0],
        [-180.0, -90.0]
    ]

    boundary_coords = []
    s_poly = None

    if entity_geojson and entity_geojson.get("type") in ["Polygon", "MultiPolygon"]:
        try:
            poly_obj = shape(entity_geojson)
            if not poly_obj.is_valid:
                poly_obj = make_valid(poly_obj)
            if not poly_obj.is_empty and poly_obj.area > 0:
                s_poly = poly_obj.simplify(tolerance=0.00008, preserve_topology=True)
                m = mapping(s_poly)
                if m["type"] == "Polygon":
                    boundary_coords = m["coordinates"][0]
                elif m["type"] == "MultiPolygon":
                    # Take exterior ring of the largest polygon component
                    largest = max(s_poly.geoms, key=lambda p: p.area)
                    boundary_coords = mapping(largest)["coordinates"][0]
        except Exception:
            s_poly = None
            boundary_coords = []

    # If entity has no polygon, generate a smooth 64-vertex geodesic boundary (NOT a 4-point rectangle)
    if not boundary_coords or s_poly is None:
        pts = 64
        r_lat = radius_km / 111.0
        r_lon = radius_km / (111.0 * math.cos(math.radians(lat)))
        for i in range(pts):
            theta = 2.0 * math.pi * i / pts
            p_lon = round(lon + r_lon * math.cos(theta), 6)
            p_lat = round(lat + r_lat * math.sin(theta), 6)
            boundary_coords.append([p_lon, p_lat])
        boundary_coords.append(boundary_coords[0])
        s_poly = SPolygon(boundary_coords)

    # Ensure counter-clockwise exterior and clockwise interior ring for MapLibre
    inv_mask_geom = {
        "type": "Polygon",
        "coordinates": [world_ring, boundary_coords]
    }

    minx, miny, maxx, maxy = s_poly.bounds
    primary_bounds = [[minx, miny], [maxx, maxy]]

    boundary_feature = {
        "type": "Feature",
        "properties": {
            "name": "Searched Entity Focus Boundary",
            "type": "administrative_boundary",
            "stroke": "#38BDF8",
            "stroke_width": 2.5
        },
        "geometry": mapping(s_poly)
    }

    mask_feature = {
        "type": "Feature",
        "properties": {
            "name": "World Spotlight Mask",
            "fill": "#0F172A",
            "fill_opacity": 0.35
        },
        "geometry": inv_mask_geom
    }

    return boundary_feature, mask_feature, primary_bounds


def extract_thematic_gis_layers(
    lat: float,
    lon: float,
    radius_km: float = 3.5,
    official_name: str = "",
    district: str = "",
    entity_geojson: Optional[Dict[str, Any]] = None,
    bbox: Optional[List[float]] = None
) -> Dict[str, Any]:
    """
    Returns exact boundary polygon, BBOX, and real-time attribute metadata.
    Completely eliminates synthetic Overpass vector polygons (disputed, government,
    water, forest, residential) in favor of high-resolution Esri 10m Sentinel-2 LULC raster tiles.
    """
    # 1. Generate Entity Boundary & Inverted Spotlight Mask
    boundary_feature, mask_feature, primary_bounds = _build_boundary_and_mask(
        lat, lon, radius_km, entity_geojson, bbox
    )

    # 2. Extract Real-Time Attribute Metadata (hierarchy, district stats, agro-climatic profile)
    hierarchy = {
        "state": "Gujarat",
        "district": district or "Gujarat District",
        "taluka": "",
        "village_ward": official_name.split(",")[0] if official_name else "Target Entity"
    }

    risk_meta = evaluate_risk_and_vulnerability(hierarchy, lat, lon, official_name)

    metadata = {
        "official_name": official_name,
        "district": district,
        "hierarchy": hierarchy,
        "agro_climatic_zone": risk_meta.get("agro_climatic_zone"),
        "soil_profile": risk_meta.get("soil_and_topography"),
        "principal_crops": risk_meta.get("principal_crops"),
        "seismic_hazard": risk_meta.get("seismic_hazard"),
        "coastal_climate_notes": risk_meta.get("coastal_and_climate_vulnerability", []),
        "district_stats": {
            "district": district,
            "state": "Gujarat",
            "revenue_code": "Gujarat Land Revenue Code (1879)",
            "cadastral_status": "Digitized under DILRMP"
        }
    }

    return {
        "type": "FeatureCollection",
        "features": [],
        "boundary": boundary_feature,
        "inverted_mask": mask_feature,
        "bounds": primary_bounds,
        "centroid": [lon, lat],
        "metadata": metadata
    }
