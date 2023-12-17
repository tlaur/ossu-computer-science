shopping_list = {}

def print_dict(dict):
    try:
        for i in sorted(dict):
            print(dict[i], i)
    except:
        print("Something went wrong.")

while True:
    try:
        item = input().upper().strip()
        if len(item) == 0:
             pass
        elif item not in shopping_list:
            shopping_list[item] = 1
        else:
            shopping_list[item] += 1 
    except EOFError:
        print_dict(shopping_list)
        break
    except:
        pass