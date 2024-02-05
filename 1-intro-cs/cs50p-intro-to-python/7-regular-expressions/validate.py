import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")