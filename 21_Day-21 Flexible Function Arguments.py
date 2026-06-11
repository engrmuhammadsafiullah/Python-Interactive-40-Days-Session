def sum_all_numbers(*args):
    total = sum(args)
    return total

print(sum_all_numbers(5, 10, 15, 20)) # Pass 4 items

def print_user_tags(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_tags(role="Admin", region="EU", status="Active")
