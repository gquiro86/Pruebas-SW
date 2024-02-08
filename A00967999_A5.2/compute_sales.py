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

# Function to create a price dictionary from the price catalogue
def create_price_dictionary(price_catalogue):
    price_dict = {}
    for item in price_catalogue:
        title = item['title']
        price = item['price']
        price_dict[title] = price
    return price_dict

# Function to compute total cost for all sales
def compute_total_cost(price_catalogue, sales_record):
    total_cost = 0
    sale_details = []
    for sale in sales_record:
        sale_info = {}
        sale_info['SALE_ID'] = sale['SALE_ID']
        sale_info['SALE_Date'] = sale['SALE_Date']
        sale_info['Total_Cost'] = 0
        items_cost = []
        product_name = sale['Product']
        quantity = sale['Quantity']
        if product_name in price_catalogue:
            item_cost = price_catalogue[product_name] * quantity
            items_cost.append({'Product': product_name, 'Quantity': quantity, 'Item_Cost': price_catalogue[product_name], 'Total_Sale': item_cost})
            sale_info['Total_Cost'] += item_cost
        else:
            print(f"Warning: Product '{product_name}' not found in price catalogue.")
        sale_info['Items'] = items_cost
        total_cost += sale_info['Total_Cost']
        sale_details.append(sale_info)
    return total_cost, sale_details

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

    # Create price dictionary from the price catalogue
    price_dict = create_price_dictionary(price_catalogue)

    # Compute total cost for all sales and get sale details
    total_cost, sale_details = compute_total_cost(price_dict, sales_record)

    # Output results to screen
    print(f"Total cost of all sales: ${total_cost:.2f}")
    print("Sales Details:")
    print("{:<20} {:<10} {:<15} {:<15}".format("Product", "Quantity", "Price Item", "Total Sale"))
    for sale_info in sale_details:
        print(f"Sale ID: {sale_info['SALE_ID']}, Sale Date: {sale_info['SALE_Date']}, Total Cost: ${sale_info['Total_Cost']:.2f}")
        for item in sale_info['Items']:
            print("{:<20} {:<10} ${:<15.2f} ${:<15.2f}".format(item['Product'], item['Quantity'], item['Item_Cost'], item['Total_Sale']))

    # Output results to file
    with open('sales_results.txt', 'w') as results_file:
        results_file.write(f"Total cost of all sales: ${total_cost:.2f}\n")
        results_file.write("Sales Details:\n")
        for sale_info in sale_details:
            results_file.write(f"Sale ID: {sale_info['SALE_ID']}, Sale Date: {sale_info['SALE_Date']}, Total Cost: ${sale_info['Total_Cost']:.2f}\n")
            for item in sale_info['Items']:
                results_file.write("{:<20} {:<10} ${:<15.2f} ${:<15.2f}\n".format(item['Product'], item['Quantity'], item['Item_Cost'], item['Total_Sale']))

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display elapsed time
    print(f"Execution time: {elapsed_time:.4f} seconds")
