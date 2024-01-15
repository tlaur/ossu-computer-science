import sys

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# Print name
# print(f"Hello, my name is {sys.argv[1].capitalize()}")
for name in sys.argv[1:]:
    print (f"Hello, my name is {name.capitalize()}")