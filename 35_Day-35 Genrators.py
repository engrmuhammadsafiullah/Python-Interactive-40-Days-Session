"""
Day 35: Memory-Efficient Generators
File: day35_generators.py
"""
import sys

# 1. Normal Function (Saves everything in RAM at once)
def normal_list(limit_number):
    result = []
    for i in range(limit_number):
        result.append(i)
    return result

# 2. Generator Function (Generates values on-the-fly)
def dynamic_generator(limit_number):
    for i in range(limit_number):
        yield i  # 💡 Pauses here and returns just ONE number at a time

if __name__ == "__main__":
    # We will test this with 100,000 numbers
    limit = 100_000
    
    list_data = normal_list(limit)
    gen_data = dynamic_generator(limit)
    
    print("-" * 50)
    print("MEMORY USAGE COMPARISON (RAM)")
    print("-" * 50)
    
    # sys.getsizeof() shows exactly how many bytes of RAM a variable consumes
    print(f"Standard List takes up: {sys.getsizeof(list_data):,} bytes")
    print(f"Generator takes up:     {sys.getsizeof(gen_data):,} bytes")
    print("-" * 50)
    
    # 💡 Notice: Looping through a generator looks EXACTLY like a list loop!
    print("Printing the first 3 items generated on-demand:")
    count = 0
    for value in gen_data:
        print(f"Fetched Value: {value}")
        count += 1
        if count == 3:
            break
            
    print("\nExecution finished.")
    input("Press the ENTER key to close this window...")
