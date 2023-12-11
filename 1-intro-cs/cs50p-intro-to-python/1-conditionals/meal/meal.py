def main():
    time = convert(input("What time is it? "))

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    time = time.strip().replace(" ", ":").split(":")
    hour = int(time[0])
    minute = float(time[1])
    meridiem = time[2].lower() if len(time) == 3 else None
    
    if meridiem is not None:
        if meridiem == "p.m" and 1 <= hour <= 11:
            hour += 12
        elif meridiem == "a.m" and hour == 12:
            hour = 0
        else:
            pass

    return hour + (minute / 60)

if __name__ == "__main__":
    main()