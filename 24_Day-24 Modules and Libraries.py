import math
import time

# Referencing local system utilities and formulas
print("Starting countdown...")
time.sleep(1)  # Delay application thread for 1 second

radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Calculated circle surface area: {area:.4f}")
