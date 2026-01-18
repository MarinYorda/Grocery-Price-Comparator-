from src import api_client, parser, comparator
from src import output
from src.cli import parse_args
from src.services.geocoding import geocode_postal_code

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

def run_phase2_sub(args):
    print("\n--- Phase 2 ---")
    print("postal_code:", args.postal_code)
    print("radius_km", args.radius_km)
    print("providers:", args.providers)
    print("limit:", args.limit)
    print("output:", args.output)
    print("csv_path:", args.csv_path)
    lat, lon = geocode_postal_code(args.postal_code)
    print("lat: ", lat)
    print("lon: ", lon)

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



