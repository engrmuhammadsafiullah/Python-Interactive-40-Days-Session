"""
Day 39: Spreadsheet & DataFrame Analytics
File: day39_pandas_core.py
"""
def analyze_sales_dataframe():
    # Simulated CSV Data Store (Rows of transactional items)
    sales_dataframe = [
        {"item": "Laptop", "price": 1200, "quantity": 2, "status": "shipped"},
        {"item": "Mouse", "price": 25, "quantity": 10, "status": "shipped"},
        {"item": "Monitor", "price": 300, "quantity": 0, "status": "cancelled"},
        {"item": "Keyboard", "price": 80, "quantity": 5, "status": "shipped"}
    ]
    
    print("-" * 50)
    print("DATAFRAME REPORT: SHIPPED ORDERS")
    print("-" * 50)
    
    grand_total_revenue = 0
    
    # Filtering data tables using logical conditions
    for record in sales_dataframe:
        if record["status"] == "shipped" and record["quantity"] > 0:
            item_revenue = record["price"] * record["quantity"]
            grand_total_revenue += item_revenue
            print(f"Product: {record['item']:<10} | Revenue generated: ${item_revenue:,}")
            
    print("-" * 50)
    print(f"Total Combined Shipped Revenue: ${grand_total_revenue:,}")
    print("-" * 50)

if __name__ == "__main__":
    analyze_sales_dataframe()
    
    print("\nExecution finished.")
    input("Press the ENTER key to close this window...")
