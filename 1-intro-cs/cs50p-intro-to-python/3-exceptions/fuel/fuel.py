def get_fraction(prompt):
    while True:
        try:
            fraction = [int(x) for x in input(prompt).split("/")]
            result = float(fraction[0]/fraction[1])*100
            if 0 <= result <= 100:
                return result
        except ValueError:
            print("Invalid entry: Enter fraction as n/n, for example 1/2")
        except ZeroDivisionError:
            print("Cannot divide by zero")
        except:
            print("Unknown error: Did you enter fraction as n/n, for example 1/2?")

def print_gauge(fraction):
    if fraction >= 99:
        print("F")
    elif fraction <= 1:
        print("E")
    else:
        print(f"{fraction:.0f}")

def main():
    x = get_fraction("Fraction: ")
    print_gauge(x)

main()