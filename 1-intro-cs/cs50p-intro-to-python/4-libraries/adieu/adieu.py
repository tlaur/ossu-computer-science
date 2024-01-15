def print_names(names: list):
    common = "Adieu, adieu, to"
    if len(names) == 1:
        print(common, names[0])
    elif len(names) == 2:
        print(common, f"{names[0]} and {names[1]}")
    elif len(names) > 2:
        print(common, end=" ")
        for name in names[:-1]:
            print(name, end=", ")
        print(f"and {names[-1]}")

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print()
        break

if len(names) > 0:
    print_names(names)