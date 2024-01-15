import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")

o = response.json()
for song in o["results"]:
    print(song["trackName"])
