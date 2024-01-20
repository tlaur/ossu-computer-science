def main():
    user_input = input("Input: ").strip()
    print("Output:", shorten(user_input))

def shorten(word):
    vowels = ["A", "E", "I", "O", "U"]
    output = ""
    for char in word:
        if char.upper() not in vowels:
            output += char
    return output

if __name__ == "__main__":
    main()