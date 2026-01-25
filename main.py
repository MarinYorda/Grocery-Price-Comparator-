from src import api_client, parser, comparator
from src import output
from src.cli import parse_args
from src.services.geocoding import geocode_postal_code
from src.services.store_locator_router import find_nearby_stores
from src.services.geo_utils import haversine_km

def run_stage1():
    # List of my raw store files
    store_files = ["store_a.json", "store_b.json"]

    # Load the stores
    stores = api_client.load_all_stores(store_files)
    
    # flatten products in a list
    all_products = api_client.get_all_products(stores)

    # parse and normalize values too
    parsed_products = parser.parse_products(all_products)

    # load results
    results = comparator.compare_all_products(parsed_products)

    # output the comparison to see where to buy your groceries
    output.print_comparison(results)
    output.print_chocolate_cheapest(results)

    output.export_comparison_to_csv(results, "comparison_results.csv")
    print("\nSaved CSV: comparison_results.csv\n")
    milk = comparator.compare_one_product(parsed_products, "milk")
    print(milk)

def run_phase2_sub(args):
    print("\n--- Phase 2 ---")
    print("radius_km", args.radius_km)
    print("providers:", args.providers)
    print("limit:", args.limit)
    print("output:", args.output)
    print("csv_path:", args.csv_path)
    user_lat, user_lon = geocode_postal_code(args.postal_code)
    print("user_lat: ", user_lat)
    print("user_lon: ", user_lon)
    print("debug distance to provigo-0001:",
          haversine_km(user_lat, user_lon, 45.5085, -73.5650))

    stores = find_nearby_stores(user_lat, user_lon, args.radius_km, args.providers)

    print("\n--- Nearby stores (stub) ---")
    if not stores:
        print("No stores found in given radius.")
    else:
        for s in stores:
            print(f"- {s['provider'].upper()} | {s['name']} | {s['distance_km']} km")
            print(f"  {s['address']}")


def main():
    
    args = parse_args()

    if args.demo_json:
        run_stage1()
    else:
        if args.postal_code is None:
            print("Error: provide --postal-code for Phase 2, or use demo for stage 1.")
            return
        run_phase2_sub(args)

if __name__ == "__main__":
    main()



