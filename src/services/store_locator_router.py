from typing import List

from src.services.store_locator.base import Store
from src.services.store_locator import provigo, maxi, metro, iga


def find_nearby_stores(
    lat: float,
    lon: float,
    radius_km: float,
    providers: List[str],
) -> List[Store]:
    if radius_km <= 0:
        raise ValueError("radius_km must be > 0")

    provider_set = {p.strip().lower() for p in providers if p}

    results: List[Store] = []

    if "provigo" in provider_set:
        results.extend(provigo.find_nearby_stores(lat, lon, radius_km))
    if "maxi" in provider_set:
        results.extend(maxi.find_nearby_stores(lat, lon, radius_km))
    if "metro" in provider_set:
        results.extend(metro.find_nearby_stores(lat, lon, radius_km))
    if "iga" in provider_set:
        results.extend(iga.find_nearby_stores(lat, lon, radius_km))

    # Filter by radius (still useful even if providers return extra)
    results = [s for s in results if s["distance_km"] <= radius_km]

    # Sort by distance
    results.sort(key=lambda s: s["distance_km"])

    return results
