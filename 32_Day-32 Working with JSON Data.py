import json

# Python Dictionary
user_profile = {
    "username": "coder123",
    "completed_days": 32,
    "skills": ["Python", "Logic"]
}

# Convert dictionary to JSON string (Serialization)
json_string = json.dumps(user_profile, indent=4)
print("JSON String:\n", json_string)

# Write dictionary directly to a JSON file
with open("user.json", "w") as file:
    json.dump(user_profile, file, indent=4)
