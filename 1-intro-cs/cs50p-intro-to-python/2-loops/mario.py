def main():
    print_square(3)

def print_column(height):
    for _ in range(height):
        print("#")

def print_row(width):
    print("?" * width)

def print_square(size):
    for _ in range(size):
        print_row(size)

main()