# Basic while-loop
i = 0

while i < 3:
    print("meow")
    i += 1

# Basic "pythonic" for-loop
for _ in range(3):
    print("meow")

# Alternative approach with print function
print("meow\n" * 3, end="")

# Validate user input with a while loop
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# Same as above but with functions
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()