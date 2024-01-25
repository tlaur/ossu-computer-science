import sys
import csv

# Check exactly one argument has been passed
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Check input file is a csv
if len(sys.argv[1].split(".")) != 2 or sys.argv[1].split(".")[1] != "csv":
    sys.exit(f"Could not read {sys.argv[1]}")

# Read CSV file and split name into first and last
try:
    students = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"].replace(" ","").split(",")
            students.append({"first": name[1], "last": name[0], "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

# Write split name and house into new file
try:
    with open(sys.argv[2], "w") as file:
        fields = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in students:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
except Exception as e:
    print(e)