inventory = ["sword", "shield"]

inventory.append("potion")       # Adds to the very end
inventory.insert(1, "bow")       # Inserts at index position 1
print(inventory)                 # ['sword', 'bow', 'shield', 'potion']

inventory.remove("shield")       # Removes element by exact match
popped_item = inventory.pop()    # Removes and returns the last element

print(inventory)                 # ['sword', 'bow']
print(f"Removed item: {popped_item}")
