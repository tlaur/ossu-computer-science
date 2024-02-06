import re

name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"Hello, {name}")

# matches = re.search(r"^(.+), (.+)$", name)

# if matches:
#     name = f"{matches.group(2)} {matches.group(1)}"

if matches := re.search(r"^(.+), (.+)$", name): 
    name = f"{matches.group(2)} {matches.group(1)}"


print(f"Hello, {name}")