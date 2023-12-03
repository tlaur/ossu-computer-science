# Replace :) and :( in user input with emoticons
def main():
    print(convert(input()))

def convert(x: str) -> str:
    return x.replace(":)","🙂").replace(":(","🙁")

main()