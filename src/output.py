from typing import List, Dict
import csv


def print_comparison(results: List[Dict]) -> None:
    print("\n--- Price comparison of different products ---\n")

    for r in results:
        name = r["name"]
        unit = r["normalized_unit"]
        min_price = r["min_price_per_100"]
        winners = ", ".join(r["winners"])

        print(f"Product: {name}")
        print(f"Unit: {unit}")
        print(f"Min price per 100: {min_price}")
        print(f"Winner(s): {winners}")

        print("Prices by store:")
        for store, price in r["by_store"].items():
            print(f"  - {store}: {price}")

        print("-" * 40)


def print_chocolate_cheapest(results: List[Dict]) -> None:
    print("\n--- Where do I buy my chocolate the cheapest? ---\n")

    chocolate_names = {"Mars Bar", "Ferrero Rocher"}

    for r in results:
        if r["name"] in chocolate_names:
            name = r["name"]
            winners = ", ".join(r["winners"])
            min_price = r["min_price_per_100"]
            unit = r["normalized_unit"]

            print(f"{name}: cheapest at {winners} ({min_price} per {unit})")


def export_comparison_to_csv(results: List[Dict], filepath: str) -> None:
    """
    Each product has its own row

    Columns names are the following :
      - name, normalized_unit, min_price_per_100, winners
      - by_store (string showing all stores listed in increasing price list)
    """
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["name", "normalized_unit", "min_price_per_100", "winners", "by_store"],
        )
        writer.writeheader()

        for r in results:
            by_store_str = "; ".join([f"{store}:{price}" for store, price in r["by_store"].items()])
            writer.writerow(
                {
                    "name": r["name"],
                    "normalized_unit": r["normalized_unit"],
                    "min_price_per_100": r["min_price_per_100"],
                    "winners": ", ".join(r["winners"]),
                    "by_store": by_store_str,
                }
            )
