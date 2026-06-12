# Parent base template
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Derived child structure extending capabilities
class ElectricCar(Vehicle):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)  # Links properties to parent base init initialization
        self.battery_capacity = battery_capacity

tesla = ElectricCar("Tesla", "85 kWh")
print(f"Vehicle: {tesla.brand} | Battery Specs: {tesla.battery_capacity}")
