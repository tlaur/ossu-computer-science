import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
except Exception as e:
    sys.exit(e)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = r.json()

    unit_price = float(o["bpi"]["USD"]["rate_float"])
    print(f"{(unit_price * amount):,.4f}")
except Exception as e:
    print(e)