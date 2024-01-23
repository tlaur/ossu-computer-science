import sys

# Check exactly one argument has been passed
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check file is a python file and exists
if len(sys.argv[1].split(".")) != 2 or sys.argv[1].split(".")[1] != "py":
    sys.exit("Not a Python file")

# Read file and count number of lines with code
try:
    line_count = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if len(line.strip()) > 0 and line.lstrip()[0] != "#":
                line_count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

# Print out line count
print(line_count)