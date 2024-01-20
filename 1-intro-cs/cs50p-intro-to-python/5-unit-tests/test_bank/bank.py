def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")

def value(greeting):
    try:
        if greeting.lower()[:5] == "hello":
            return 0
        elif greeting.lower()[0] == "h":
            return 20
        else:
            return 100
    except IndexError:
        return 100

if __name__ == "__main__":
    main()