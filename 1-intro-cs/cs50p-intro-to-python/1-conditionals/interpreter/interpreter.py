def add(x,y):
    return float(x + y)

def subtract(x,y):
    return float(x - y)

def multiply(x,y):
    return float(x * y)

def divide(x,y):
    return float(x / y)

def main():
    expression = input("Expression: ").strip().split(" ")

    x = int(expression[0])
    y = expression[1]
    z = int(expression[2])

    match y:
        case "+":
            result = add(x,z)
        case "-":
            result = subtract(x,z)
        case "*":
            result = multiply(x,z)
        case "/":
            result = divide(x,z) if z != 0 else "Can't divide by zero"

    if type(result) is float:
        print(f"{result:.1f}")
    else:
        print(result)

main()