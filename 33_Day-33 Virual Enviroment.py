"""
Day 33: Virtual Environment Test
File: main.py
"""
import sys

def check_env():
    print("-" * 40)
    print("VIRTUAL ENVIRONMENT TEST")
    print("-" * 40)
    
    # Check if the code is running inside a virtual environment folder
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    print(f"Is virtual environment active?: {in_venv}")
    print(f"Python is running from: {sys.executable}")
    
    # Try to import the requests library
    try:
        import requests
        print("Library status: 'requests' is installed and working!")
    except ImportError:
        print("Library status: 'requests' is NOT installed.")
        print("👉 Run: pip install requests")
        
    print("-" * 40)

if __name__ == "__main__":
    check_env()
