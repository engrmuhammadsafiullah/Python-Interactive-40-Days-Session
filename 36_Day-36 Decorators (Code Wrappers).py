"""
Day 36: Mastering Decorators
File: day36_decorators.py
"""
import time

# This is the decorator function
def performance_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()       # 1. Capture start time
        
        result = func(*args, **kwargs) # 2. Execute the original function
        
        end_time = time.time()         # 3. Capture end time
        duration = end_time - start_time
        print(f"⏱️ Function '{func.__name__}' took {duration:.4f} seconds to run.")
        return result
    return wrapper

# Using the '@' symbol to attach our decorator
@performance_timer
def heavy_calculation():
    print("Running a heavy loop simulation...")
    total = sum(i for i in range(5_000_000))
    return total

if __name__ == "__main__":
    calc_result = heavy_calculation()
    print(f"Calculation Result: {calc_result}")
    
    print("\nExecution finished.")
    input("Press the ENTER key to close this window...")
