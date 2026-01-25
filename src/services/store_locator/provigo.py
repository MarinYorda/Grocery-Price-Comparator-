from __future__ import annotations

from typing import List
from pathlib import Path
from .base import Store

from src.services.geo_utils import haversine_km
import csv

# Path to offline store location data
PROVIGO_CSV_PATH = Path(__file__).resolve().parents[3] / "data" / "stores" / "provigo.csv"


def find_nearby_stores(lat: float, lon: float, radius_km: float) -> List[Store]:
    """
    Offline Provigo locator:
    
    - load store locations from local csv file
    - compute distance using haversine formula
    - filter within radius to only include stores that are in proximity of the user
    - sort by closest-first
    """

    stores = load_stores_from_csv(PROVIGO_CSV_PATH)

    results = []
    for s in stores:
        d = haversine_km(lat, lon, s["lat"], s["lon"])
        if d <= radius_km:
            # Copy to set the distance of the store
            store : Store = {
                "provider": "provigo",
                "store_id": s["store_id"],
                "name": s["name"],
                "address": s["address"],
                "lat": s["lat"],
                "lon": s["lon"],
                "distance_km": round(d, 2),
            }
            results.append(store)
    results.sort(key=lambda x: x["distance_km"])
    return results

def load_stores_from_csv(csv_path: Path) -> List[dict]:
    results = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            results.append({
                "store_id": row["store_id"],
                "name": row["name"],
                "address": row["address"],
                "lat": float(row["lat"]),
                "lon": float(row["lon"]),
            })
    return results

