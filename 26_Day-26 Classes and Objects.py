# Defining real world schemas
class VirtualPet:
    def __init__(self, name):
        self.name = name  # Object instantiation properties
        self.hunger = 60

my_pet = VirtualPet("Pixel")
print(f"Pet named {my_pet.name} spawned. Initial Hunger level: {my_pet.hunger}")
