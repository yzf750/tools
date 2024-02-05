#!/usr/bin/env python3

# sudo apt-get install python3-prettytable

import csv
import sys
from prettytable import PrettyTable

def parse_csv(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Assuming the first row contains headers
        for row in csv_reader:
            data.append(dict(zip(headers, row)))
    return headers, data

def search_csv(headers, data, partial_value):
    results = []
    for row in data:
        for column in headers:
            cell_value = row.get(column)
            if cell_value and partial_value.lower() in cell_value.lower():
                results.append(row)
                break  # Stop searching other columns for the same row once a match is found
    return results

def display_results(results):
    if results:
        table = PrettyTable()
        table.field_names = results[0].keys()
        for result in results:
            table.add_row(result.values())
        print(table)
    else:
        print("No results found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: default-passwords.py <password_file_path> <search_value>")
        sys.exit(1)

    file_path = sys.argv[1]
    partial_value = sys.argv[2]

    headers, data = parse_csv(file_path)

    results = search_csv(headers, data, partial_value)

    print(f"Search Results for '{partial_value}'")
    display_results(results)
