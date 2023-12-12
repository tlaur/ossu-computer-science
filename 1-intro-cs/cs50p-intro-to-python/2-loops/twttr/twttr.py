vowels = ["A", "E", "I", "O", "U"]
user_input = input("Input: ").strip()
output = ""

for char in user_input:
    if char.upper() not in vowels:
        output += char

print("Output:", output)