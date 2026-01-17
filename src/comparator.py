from collections import defaultdict
from typing import Optional, Dict



def compare_one_product(products: list[dict], name: str) -> Optional[Dict]:
    # compare the prices for a single specified product by the user
    # return none if the product name is not found in the db

    target = name.strip().lower()

    filtered = [
        p for p in products
        if(str(p.get("name","")).strip().lower() == target)
    ]
    if not filtered:
        return None
    
    results = compare_all_products(filtered)
    return results[0] if results else None

def compare_all_products(products: list[dict]) -> list[dict]:
    groups = defaultdict(list)

    for product in products:
        name = product["name"]
        groups[name].append(product)

    results = []
    for name, group in groups.items():
        min_price = min(item["price_per_100"] for item in group)
        winners = []
        for item in group:
            if (item["price_per_100"] == min_price):
                winners.append(item)
        result = {}
        # adding the name of hte product
        result["name"] = name
        # noramlized unit for hte product
        result["normalized_unit"] = group[0]["normalized_unit"]
        # min price
        result["min_price_per_100"] = min_price
        # winners
        result["winners"] = [w["store"] for w in winners]
        # price in stores in decreasing order
        sorted_group = sorted(group, key=lambda item: item["price_per_100"])
        result["by_store"] = {
            item["store"]: item["price_per_100"] for item in sorted_group
        }
        results.append(result)
    return results

