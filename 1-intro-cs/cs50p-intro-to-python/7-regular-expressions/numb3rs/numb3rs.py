import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip: str) -> bool:
    regex_rule = (r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}"
                  r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")
    if matches := re.search(regex_rule, ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()