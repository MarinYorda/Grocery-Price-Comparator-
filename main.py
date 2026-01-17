from src import api_client
from src import parser, comparator

def main():
    
    # List of my raw store files
    store_files = ["store_a.json", "store_b.json"]

    # Load the stores
    stores = api_client.load_all_stores(store_files)

    # Print Store name and how many products the have
    for store in stores:
        print(f"Store: {store['store']}, Products: {len(store['products'])}")
    
    # flatten products in a list
    all_products = api_client.get_all_products(stores)

    # Print first 5 products 
    print("\nFlatted products (first 5):")
    for product in all_products[:5]:
        print(product)

    print("\nFirst 5 flattened products from Store B:")
    store_b_products = [p for p in all_products if p["store"] == "Store B"]

    for product in store_b_products[:5]:
        print(product)

    
    # Print the total number of products a store has
    print(f"\nTotal products across all stores: {len(all_products)}")

    parsed_products = parser.parse_products(all_products)
    print(f"\nParsed products count: {len(parsed_products)}")
    print("First parsed product:", parsed_products[0])

    # TEMP: verify computed fields from Pydantic
    print("\n--- Normalization sanity check ---")
    first = parsed_products[0]
    print(first)
    print("price_per_100:", first["price_per_100"])
    print("normalized_unit:", first["normalized_unit"])

    comp = comparator.compare_all_products(parsed_products)
    compare_1 = comparator.compare_one_product(parsed_products, "Candy")
    print("\n---Price comparison of different products---")
    print(comp)
    print("\n---Where do I buy my chocolate the cheapest---")
    print(compare_1)





if __name__ == "__main__":
    main()



