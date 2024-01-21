# Error handling won't quite work as the original in 
# Problem Set 3, but for the purposes of testing 
# convert() and gauge() this will suffice

def main():
    try:
        fraction = input("Fraction: ")
        print(gauge(convert(fraction)))
    except Exception as e:
        print(e)

def convert(fraction):
    try:
        fraction = [int(x) for x in fraction.split("/")]
        result = round(float(fraction[0]/fraction[1])*100)
        if 0 <= result <= 100:
            return result
        else:
            raise Exception("Invalid entry: Denominator larger than numerator")
    except ValueError:
        raise ValueError("Invalid entry: Enter fraction as n/n, for example 1/2")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")
    except:
        raise Exception("Unknown error: Did you enter fraction as n/n, for example 1/2?")

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}"

if __name__ == "__main__":
    main()