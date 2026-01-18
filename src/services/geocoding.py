from typing import Tuple
import requests


NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"


def geocode_postal_code(postal_code: str) -> Tuple[float, float]:
    """
    Convert a postal code into (latitude, longitude) using OSM Nominatim.
    """
    code = str(postal_code).strip()
    if not code:
        raise ValueError("postal_code is empty")

    params = {
        "q": f"{code}, Canada",
        "format": "json",
        "limit": 1,
    }

    headers = {
        # Nominatim requires a valid User-Agent (put your project name)
        "User-Agent": "grocery-price-comparator/1.0 (contact: dev)",
    }

    resp = requests.get(NOMINATIM_URL, params=params, headers=headers, timeout=10)
    resp.raise_for_status()

    data = resp.json()
    if not data:
        raise ValueError(f"No geocoding result for postal code: {code}")

    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon
