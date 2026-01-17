# src/api_client.py
"""
API Client module to fetch store product data.
Currently reads mock JSON files from data/raw/ as if they were API responses.
The goal is to read real data from websites in your vicinity 
"""
import json
import os
from typing import List, Dict

# Optional: change this to match your project root if needed
RAW_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw")

# Reading a single store from the json files
def load_store_data(filename: str) -> Dict:
    path = os.path.join(RAW_DATA_PATH, filename)
    with open(path, "r", encoding="utf-8") as f:
        store_data = json.load(f)
    return store_data

# Reading and loading multiple JSON files and return as a list of dict
def load_all_stores(filenames: List[str]) -> List[Dict]:
    stores = []
    for file in filenames:
        stores.append(load_store_data(file))
    return stores

# Return list of products and their store info
def get_all_products(stores: List[Dict]) -> List[Dict]:

    all_products = []
    for store in stores:
        for product in store["products"]:
            product_copy = product.copy()
            product_copy["store"] = store["store"]
            all_products.append(product_copy)
    return all_products


