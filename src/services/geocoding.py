# from typing import Tuple
# import requests

# NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
# HEADERS = {"User-Agent": "grocery-price-comparator/1.0 (contact: dev)"}

# def geocode_postal_code(postal_code: str) -> Tuple[float, float]:
#     code = str(postal_code).strip().upper()
#     if not code:
#         raise ValueError("postal_code is empty")

#     code_nospace = code.replace(" ", "")

#     # Try multiple query patterns (Nominatim can be picky)
#     attempts = [
#         {"postalcode": code_nospace, "country": "Canada"},
#         {"q": f"{code}, Montreal, Quebec, Canada"},
#         {"q": f"{code_nospace}, Montreal, Quebec, Canada"},
#         {"q": f"{code}, Quebec, Canada"},
#         {"q": f"{code}, Canada"},
#     ]

#     base_params = {
#         "format": "json",
#         "limit": 1,
#         "countrycodes": "ca",
#         "addressdetails": 1,
#     }

#     for a in attempts:
#         params = {**base_params, **a}
#         resp = requests.get(NOMINATIM_URL, params=params, headers=HEADERS, timeout=15)
#         resp.raise_for_status()
#         data = resp.json()

#         # DEBUG (temporarily): see what query was tried + whether it matched
#         # print("TRY:", params)
#         # print("URL:", resp.url)
#         # print("FOUND:", len(data))

#         if data:
#             return float(data[0]["lat"]), float(data[0]["lon"])

#     raise ValueError(f"No geocoding result for postal code: {code}")
FSA_TO_COORDS = {
    "H4E": (45.467, -73.626),  # Montreal (Verdun / Sud-Ouest-ish)
    "H2X": (45.514, -73.565),  # Plateau / Downtown-ish
    "H3Z": (45.497, -73.595),  # Westmount-ish
}

def geocode_postal_code(postal_code: str) -> tuple[float, float]:
    code = str(postal_code).strip().upper().replace(" ", "")
    if len(code) < 3:
        raise ValueError("postal_code too short")

    fsa = code[:3]
    if fsa in FSA_TO_COORDS:
        return FSA_TO_COORDS[fsa]

    raise ValueError(f"Unknown FSA for demo: {fsa}")
