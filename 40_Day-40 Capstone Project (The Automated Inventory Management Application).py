"""
Day 40: Capstone Project - Automated Warehouse Database Tracker
File: day40_capstone.py
"""
import sqlite3

def initialize_system():
    # Connect and build a structured database table
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            sku INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            stock_level INTEGER NOT NULL,
            unit_price REAL NOT NULL
        )
    """)
    
    # Inject initial test data rows safely if table is completely empty
    cursor.execute("SELECT COUNT(*) FROM inventory")
    if cursor.fetchone()[0] == 0:
        initial_stock = [
            ("Premium Laptop", 15, 1200.00),
            ("Wireless Mouse", 120, 25.00),
            ("HD Monitor", 40, 300.00)
        ]
        cursor.executemany("INSERT INTO inventory (product_name, stock_level, unit_price) VALUES (?, ?, ?)", initial_stock)
        conn.commit()
    conn.close()

def generate_warehouse_analytics_report():
    conn = sqlite3.connect("warehouse.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    
    print("\n" + "=" * 60)
    print("📈 AUTOMATED INVENTORY & ASSET REPORT")
    print("=" * 60)
    print(f"{'SKU':<5} | {'PRODUCT NAME':<18} | {'STOCK':<6} | {'PRICE':<8} | {'ASSET VALUE':<12}")
    print("-" * 60)
    
    total_warehouse_value = 0
    
    for item in rows:
        sku, name, stock, price = item
        asset_value = stock * price
        total_warehouse_value += asset_value
        print(f"{sku:<5} | {name:<18} | {stock:<6} | ${price:<7.2f} | ${asset_value:,.2f}")
        
    print("-" * 60)
    print(f"Total Valuation of Distributed Stock: ${total_warehouse_value:,.2f}")
    print("=" * 60)
    conn.close()

if __name__ == "__main__":
    print("Booting Warehouse Tracking Subsystem...")
    initialize_system()
    generate_warehouse_analytics_report()
    
    print("\nSystem capstone run completed.")
    input("Press the ENTER key to shut down interface...")
