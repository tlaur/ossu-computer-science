import random

def main():
    question_count = 0
    level = get_level()
    while question_count < 9:
        try:
            ints = [generate_integer(level),generate_integer(level)]
            answer = str(ints[0] + ints[1])
            question = f"{ints[0]} + {ints[1]} = "
            answer_count = 0
            response = ""
            while response != answer and answer_count < 3:
                response = input(question)
                if response == answer:
                    question_count += 1
                    break
                else:
                    print("EEE")
                    answer_count += 1
                if answer_count == 3:
                    print(answer)
                    question_count += 1
        except Exception as e:
            print(e)

def get_level():
    level = None
    while level not in [1,2,3]:
        try:
            level = int(input("Level: "))
        except:
            pass
    return level

def generate_integer(level: int):
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)
        case _:
            raise ValueError
        
main()