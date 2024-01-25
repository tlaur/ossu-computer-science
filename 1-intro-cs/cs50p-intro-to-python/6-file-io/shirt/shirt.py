import sys
from PIL import Image, ImageOps

def extension_valid(x):
    if x.split(".")[1].lower() in ["jpg", "jpeg", "png"]:
        return True

# Check exactly two arguments have been passed
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Check input and output file validity
for arg in sys.argv[1:]:
    if len(arg.split(".")) != 2 or arg.split(".")[1].lower() not in ["jpg", "jpeg", "png"]:
        sys.exit(f"Invalid input" if arg == sys.argv[1] else "Invalid output")

# Check input and output file extensions match
if sys.argv[1].split(".")[1].lower() != sys.argv[2].split(".")[1].lower():
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    size = shirt.size
    before = ImageOps.fit(Image.open(sys.argv[1]), size=size)
    before.paste(shirt, shirt)
    before.save(sys.argv[2])
except FileNotFoundError:
    sys.exit(f"Input does not exist")