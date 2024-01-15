import sys
from random import choice
from pyfiglet import Figlet, print_figlet

def get_input():
    x = input("Input: ")
    return x

if len(sys.argv) == 1:
    font = choice(Figlet().getFonts())
    print_figlet(get_input(), font=font)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in Figlet().getFonts():
    print_figlet(get_input(), font=sys.argv[2])
else:
    sys.exit("Invalid usage")

