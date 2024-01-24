import sys
import csv
import tabulate

# Check exactly one argument has been passed
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Check file is a csv
if len(sys.argv[1].split(".")) != 2 or sys.argv[1].split(".")[1] != "csv":
    sys.exit("Not a CSV file")

# Read CSV file and print table to console
try:
    with open(sys.argv[1]) as file:
        content = csv.DictReader(file)
        print(tabulate.tabulate(content, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
