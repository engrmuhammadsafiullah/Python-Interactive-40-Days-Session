"""
Day 38: Matrix Math & Array Concepts
File: day38_numpy_core.py
"""
def native_matrix_processing():
    # Simulated 2D NumPy Array (a 3x3 Matrix grid of pixels or math coordinates)
    matrix = [
 
        [7, 8, 9]
    ]
    
    print("Original 3x3 Data Grid:")
    for row in matrix:
        print(row)
        
    print("\nProcessing Array Row Operations:")
    # Calculate the average of each row across the grid
    for index, row in enumerate(matrix):
        row_total = sum(row)
        row_average = row_total / len(row)
        print(f"Row {index + 1} Total: {row_total} | Average: {row_average}")

if __name__ == "__main__":
    native_matrix_processing()
    
    print("\nExecution finished.")
    input("Press the ENTER key to close this window...")
