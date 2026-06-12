"""
Day 34: API Interactions (Simulated No-Network Mode)
File: day34_api.py
"""
import json

def get_simulated_api_data():
    print("Connecting to API endpoint (Simulated Local Mode)...")
    
    # This string exactly mimics what a real web server returns to Python
    web_server_response = """
    {
        "status": "success",
        "crypto": {
            "name": "Bitcoin",
            "symbol": "BTC",
            "usd_price": 94250
        },
        "market_trend": "bullish"
    }
    """
    
    try:
        # json.loads converts raw text text into a functional Python Dictionary
        data = json.loads(web_server_response)
        
        # Extract values using standard dictionary keys
        coin_name = data["crypto"]["name"]
        price = data["crypto"]["usd_price"]
        trend = data["market_trend"]
        
        print("-" * 40)
        print(f"🚀 Success! Web Data Parsed (Offline Mode)")
        print(f"Asset: {coin_name}")
        print(f"Live Price: ${price:,} USD")
        print(f"Market Trend: {trend.upper()}")
        print("-" * 40)
        
    except Exception as e:
        print(f"Data Processing Failed: {e}")

if __name__ == "__main__":
    get_simulated_api_data()
    
    # Keeps your Windows terminal window open
    print("\nFetch execution finished.")
    input("Press the ENTER key to close this window...")

