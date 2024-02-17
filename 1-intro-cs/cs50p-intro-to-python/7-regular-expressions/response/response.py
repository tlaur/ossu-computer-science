from validators import email

if email(input("What's your email? ").strip()):
    print("Valid")
else:
    print("Invalid")