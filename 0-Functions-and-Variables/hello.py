# Classic hello world
print("Hello world")

# Ask user for their name and greet them
# Remove whitespace from str and capitalise name
# Split the name of the user into first and last names
name = input("What is your name? ").strip().title()

first_name, last_name = name.split(" ")

print(f"Hello, {name}")
print(f"Hello, {first_name} {last_name}")

# Alternative uglier str split
# Both will fail if user input is not two values
first_name = name.split(sep=" ")[0]
last_name = name.split(sep=" ")[1]

# Declaring functions to do the same as above
def main():
    name = input("What is your name? ")
    hello(name)

def hello(to="world"):
    print(f"Hello {to}")

main()