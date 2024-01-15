import emoji

emoji_code = input("Input: ")

print(f"Output: {emoji.emojize(emoji_code, language='alias')}")