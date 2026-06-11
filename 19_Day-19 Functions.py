# Defining a reusable function
def calculate_area(width, height):
    area = width * height
    return area

# Calling the function and saving its output
room1_area = calculate_area(12.5, 10.0)
room2_area = calculate_area(9.0, 9.0)

print(f"Room 1: {room1_area} sqft, Room 2: {room2_area} sqft")
