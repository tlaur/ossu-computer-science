from random import randint

level = 0

while level < 1:
    try:
        level = int(input("Level: "))
    except:
        pass

target = randint(1,level)
guess = 0

while guess != target:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            raise
        elif guess > target:
            print("Too large!")
        elif guess < target:
            print("Too small!")
        else:
            print("Just Right!")
            break
    except:
        pass
