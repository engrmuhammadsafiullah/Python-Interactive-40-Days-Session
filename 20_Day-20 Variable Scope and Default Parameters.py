# Default parameter allows greeting without an explicit argument
def greet_user(name="Guest"):
    # Local scope variable
    message = f"Welcome back, {name}!"
    return message

print(greet_user("Sarah")) # Uses argument
print(greet_user())        # Falls back to default 'Guest'
