# Take two integers as an input and print their sum
# No error handling
x = int(input("What's x? "))
y = int(input("What's y? "))
z = x + y
print(f"{x} + {y} equals {z}")

# Now let's do division and round
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)
print(f"{x} / {y} equals {z}")
# Alternative way to specify float precision
print(f"{x} / {y} equals {z:.5f}")