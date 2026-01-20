from typing import List
from .base import Store


def find_nearby_stores(lat: float, lon: float, radius_km: float) -> List[Store]:
    return [
        {
            "provider": "metro",
            "store_id": "metro-001",
            "name": "Metro (Demo Store 001)",
            "address": "789 Demo Blvd, Montreal, QC",
            "lat": lat + 0.010,
            "lon": lon + 0.002,
            "distance_km": 2.4,
        }
    ]
