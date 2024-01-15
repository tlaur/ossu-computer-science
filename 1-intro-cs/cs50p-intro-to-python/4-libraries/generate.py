from random import choice, randint, shuffle

coin = choice(["heads", "tails"])

number = randint(1,10)

cards = ["jack", "queen", "king"]
shuffle(cards)

print(coin)
print(number)

for card in cards:
    print(card)