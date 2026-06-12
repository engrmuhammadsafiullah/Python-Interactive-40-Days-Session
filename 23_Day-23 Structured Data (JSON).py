import json

# Parsing object maps into structural records
expenses = {"food": 25.50, "transport": 14.00, "utilities": 120.00}

# Write structural JSON file
with open("expenses.json", "w") as out_file:
    json.dump(expenses, out_file, indent=4)

# Read structural JSON file back into application
with open("expenses.json", "r") as in_file:
    loaded_data = json.load(in_file)
    print("Loaded JSON Total Spending:", sum(loaded_data.values()))
