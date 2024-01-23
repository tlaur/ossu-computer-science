import csv
names = []

# for _ in range(3):
#     names.append(input("What's your name? "))
    
# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(name+"\n")
# file.close()

# Better (and more pythonic) way to do the same as above
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda x: x["name"]):
    print(f"hello, {student['name']} of {student['home']}")
