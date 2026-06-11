user_profile = {
    "username": "coder99",
    "level": 5,
    "is_active": True
}

# Accessing values via keys
print(user_profile["username"])

# Adding or updating key-value pairs
user_profile["level"] = 6
user_profile["joined_year"] = 2026

print(user_profile.get("email", "Not Provided"))
