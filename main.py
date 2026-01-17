from src import api_client, parser, comparator
from src import output

def main():
    
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

if __name__ == "__main__":
    main()



