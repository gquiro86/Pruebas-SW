import json
import sys
import time

# Function to load JSON data from a file
def load_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
        return None

# Function to compute total cost for all sales
def compute_total_cost(price_catalogue, sales_record):
    total_cost = 0
    for sale in sales_record:
        for item in sale['items']:
            product_id = item['product_id']
            quantity = item['quantity']
            if product_id in price_catalogue:
                total_cost += price_catalogue[product_id] * quantity
            else:
                print(f"Warning: Product ID {product_id} not found in price catalogue.")
    return total_cost

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py price_catalogue.json sales_record.json")
        sys.exit(1)

    start_time = time.time()

    # Load price catalogue and sales record from JSON files
    price_catalogue = load_json_file(sys.argv[1])
    sales_record = load_json_file(sys.argv[2])

    if price_catalogue is None or sales_record is None:
        sys.exit(1)

    # Compute total cost for all sales
    total_cost = compute_total_cost(price_catalogue, sales_record)

    # Output results to screen
    print(f"Total cost of all sales: ${total_cost:.2f}")

    # Output results to file
    with open('sales_results.txt', 'w') as results_file:
        results_file.write(f"Total cost of all sales: ${total_cost:.2f}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display elapsed time
    print(f"Execution time: {elapsed_time:.4f} seconds")
