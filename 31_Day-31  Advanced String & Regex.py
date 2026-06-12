import re

text = "Contact support at support@example.com or sales@company.org. Call us at 555-123-4567."

# Pattern for emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

# Pattern for phone numbers (###-###-####)
phone_pattern = r"\d{3}-\d{3}-\d{4}"
phones = re.findall(phone_pattern, text)

print("Found Emails:", emails)
print("Found Phones:", phones)
