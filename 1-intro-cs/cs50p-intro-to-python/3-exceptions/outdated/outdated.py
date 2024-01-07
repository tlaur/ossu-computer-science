def parse_us_numdate(date: str):
    date = date.strip().split("/")
    day = int(date[1])
    month = int(date[0])
    year = int(date[2])
    date = {"day": day, "month": month, "year": year}
    if is_date_valid(date) is True:
        return date

def parse_us_textdate(date: str):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    date = date.replace(",","").split(" ")
    day = int(date[1])
    month = int(months.index(date[0])+1)
    year = int(date[2])
    date = {"day": day, "month": month, "year": year}
    if is_date_valid(date) is True:
        return date

def is_date_valid(date: dict):
    if not 1 <= date['day'] <= 31:
        raise Exception(f"Invalid day input ({date['day']}). Must be between 1-31.")
    if not 1 <= date['month'] <= 12:
        raise Exception(f"Invalid month input ({date['month']}). Must be between 1-12.")
    return True

def printdate(date: dict):
    print(f"{date['year']:04}-{date['month']:02}-{date['day']:02}")

def main():
    date = input("Date: ").strip()
    if len(date.split(" ")) == 3:
        date = parse_us_textdate(date)
    elif len(date.split("/")) == 3:
        date = parse_us_numdate(date)
    printdate(date)

while True:
    try:
        main()
        break
    except EOFError:
        break
    except Exception as e:
        print(f"Error: {e}")