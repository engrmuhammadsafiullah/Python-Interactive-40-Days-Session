from datetime import datetime

# Stream storage writing logs locally
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Context manager ensures system resources close securely
with open("user_log.txt", "a") as file:
    file.write(f"User logged in at: {timestamp}\n")

with open("user_log.txt", "r") as file:
    print("Log Contents:\n", file.read())
