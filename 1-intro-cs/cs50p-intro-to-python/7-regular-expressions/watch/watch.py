import re

html = ('<iframe width="560" height="315" \
        src="https://www.youtube.com/embed/xvFZjo5PgG0" \
        title="YouTube video player" frameborder="0" allow="accelerometer; \
        autoplay; clipboard-write; encrypted-media; gyroscope; \
        picture-in-picture" allowfullscreen></iframe>')

def main():
    print(parse(input("HTML: ")))

def parse(s):
    regex_rule = r"^<iframe.+src=\"https?://www.youtube.com/embed/([a-zA-Z0-9]*)\".*>$"
    if matches := re.search(regex_rule, s):
        return f"https://youtu.be/{matches.group(1)}"

if __name__ == "__main__":
    main()