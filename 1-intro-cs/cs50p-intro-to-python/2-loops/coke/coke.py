amount_due = 50

while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coint: "))
    if coin in [25, 10, 5]:
        amount_due -= coin

print("Change Owed:", -amount_due)