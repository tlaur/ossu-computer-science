def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_min_max_characters(s) and start_with_two_letters(s) and no_nums_in_middle(s) and first_num_not_zero(s) and only_alphanumeric(s):
        return True

def start_with_two_letters(x):
    for i in range(2):
        if x[i].isalpha() is False:
            return False
    return True

def check_min_max_characters(x):
    if 2 <= len(x) <= 6:
        return True

def no_nums_in_middle(x):
    numbers = []
    for i in range(len(x)):
        numbers.append(x[i]) if x[i].isnumeric() else None
    if len(numbers) > 0 and not x[-1].isnumeric():
        return False
    return True
    
def first_num_not_zero(x):
    numbers = []
    for i in range(len(x)):
        numbers.append(x[i]) if x[i].isnumeric() else None
    if len(numbers) > 0 and numbers[0] == "0":
        return False
    return True

def only_alphanumeric(x):
    for i in range(len(x)):
        if x[i].isalnum() is False:
            return False
    return True

if __name__ == "__main__":
    main()