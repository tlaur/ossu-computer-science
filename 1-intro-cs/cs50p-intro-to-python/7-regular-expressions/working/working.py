import re

def main():
    print(convert(input("Hours: ")))

def clock_convert(time):
    time = time.strip().replace(" ", ":").split(":")
    hour = int(time[0])
    minute = int(time[1]) if len(time) == 3 else 0
    meridiem = time[2].upper() if len(time) == 3 else time[1].upper()
    
    if meridiem == "PM" and 1 <= hour <= 11:
        hour += 12
    elif meridiem == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

def convert(s):
    regex_rule = (r"^(([1-9]|1[0-2])|([1-9]|1[0-2]):[0-5][0-9]) (AM|PM) "
                  r"to (([1-9]|1[0-2])|([1-9]|1[0-2]):[0-5][0-9]) (AM|PM)$")
    if matches := re.search(regex_rule, s, re.IGNORECASE):
        return (f"{clock_convert(matches.group(1)+' '+matches.group(4))} " 
                f"to {clock_convert(matches.group(5)+' '+matches.group(8))}")
    else: 
        raise ValueError("Invalid time format")

if __name__ == "__main__":
    main()