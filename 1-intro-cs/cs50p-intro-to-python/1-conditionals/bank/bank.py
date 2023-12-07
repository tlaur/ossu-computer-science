greeting = input("Greeting: ").strip()

if greeting.lower()[:5] == "hello":
    print("$0")
elif greeting.lower()[0] == "h":
    print("$20")
else:
    print("$100")