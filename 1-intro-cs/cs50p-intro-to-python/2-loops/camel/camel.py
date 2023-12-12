def main():
    variable = input("camelCase: ")
    print("snake_case:", camel_to_snake(variable))

def camel_to_snake(str):
    output = ""
    for character in str:
        if character.isupper():
            output += "_" + character
        else:
            output += character
    return output.lower()

main()
