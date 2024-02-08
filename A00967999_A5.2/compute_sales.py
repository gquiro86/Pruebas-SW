"""Programa para obtener el costo total de dos archivos dados."""
import json
import sys
import time


# Function to load JSON data from a file
def load_json_file(filename):
    """ Función para cargar datos de JSON a un archivo """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
        return None


# Function to create a price dictionary from the price catalogue
def create_price_dictionary(price_catalogue_input):
    """ Función para crear un diccionario de artículos y su costo """
    price_dictionary_calc = {}
    for item_dict in price_catalogue_input:
        title = item_dict['title']
        price = item_dict['price']
        price_dictionary_calc[title] = price
    return price_dictionary_calc


# Function to compute total cost for all sales
def compute_total_cost(price_catalogue_input_cost, sales_record_input_cost):
    """ Función para calcular el costo total """
    total_cost_compute = 0
    sale_details_input_cost = []
    for sale in sales_record_input_cost:
        sale_info_compute = {}
        sale_info_compute['SALE_ID'] = sale['SALE_ID']
        sale_info_compute['SALE_Date'] = sale['SALE_Date']
        sale_info_compute['Total_Cost'] = 0
        items_cost = []
        product_name = sale['Product']
        quantity = sale['Quantity']
        if product_name in price_catalogue_input_cost:
            item_cost = price_catalogue_input_cost[product_name] * quantity
            items_cost.append({'Product': product_name,
                               'Quantity': quantity,
                               'Item_Cost': price_catalogue_input_cost[product_name],
                               'Total_Sale': item_cost})
            sale_info_compute['Total_Cost'] += item_cost
        else:
            print(f"Warning: Product '{product_name}'"
                  f"not found in price catalogue.")
        sale_info_compute['Items'] = items_cost
        total_cost_compute += sale_info_compute['Total_Cost']
        sale_details_input_cost.append(sale_info_compute)
    return total_cost_compute, sale_details_input_cost


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py "
              "price_catalogue.json sales_record.json")
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
    print(f"{'Product':<20} {'Quantity':<10}"
          f" {'Price Item':<15} {'Total Sale':<15}")


    for sale_info in sale_details:
        print(f"Sale ID: {sale_info['SALE_ID']}, "
              f"Sale Date: {sale_info['SALE_Date']}, "
              f"Total Cost: ${sale_info['Total_Cost']:.2f}")
        for item_sale in sale_info['Items']:
            print(f"{item_sale['Product']:<20} {item_sale['Quantity']:<10}"
                  f"${item_sale['Item_Cost']:<15.2f} ${item_sale['Total_Sale']:<15.2f}")


    # Output results to file
    with open('sales_results.txt', 'w', encoding='utf-8') as results_file:
        results_file.write(f"Total cost of all sales: ${total_cost:.2f}\n")
        results_file.write("Sales Details:\n")
        for sale_info in sale_details:
            results_file.write(f"Sale ID: {sale_info['SALE_ID']}, "
                               f"Sale Date: {sale_info['SALE_Date']}, "
                               f"Total Cost: ${sale_info['Total_Cost']:.2f}\n")
            for item in sale_info['Items']:
                results_file.write(f"{item['Product']:<20} {item['Quantity']:<10} "
                    f"${item['Item_Cost']:<15.2f} ${item['Total_Sale']:<15.2f}\n")


    end_time = time.time()
    elapsed_time = end_time - start_time

    # Display elapsed time
    print(f"Execution time: {elapsed_time:.4f} seconds")
