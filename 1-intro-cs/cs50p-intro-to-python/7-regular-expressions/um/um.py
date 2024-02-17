import re

def main():
    print(count(input("Text: ")))

def count(s):
    regex_rule = r"(^|\s)um(?=[^\w\]-]|$)"
    return len(re.findall(regex_rule, s, re.IGNORECASE))
    
if __name__ == "__main__":
    main()