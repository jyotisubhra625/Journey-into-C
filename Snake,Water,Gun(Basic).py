import random

def check(comp, user):
    if comp == user:
        return 0
    if (comp == 1 and user == 2):
        return -1
    if (comp == 2 and user == 3):
        return -1
    if (comp == 3 and user == 1):
        return -1
    return 1

while True:
    comp = random.choice([1, 2, 3])
    user = int(input("Enter 1 for SNAKE, 2 for WATER or 3 for GUN: "))
    print("Enter 4 to QUIT")
    if user == 4:
        break
    elif user not in [1, 2, 3, 4]:
        print("Invalid Number!")
        continue

    score = check(comp, user)

    print("You : ", user)
    print("Computer : ", comp)

    if score == 0:
        print("It's a tie!")
    elif score == -1:
        print("You Lose!")
    else:
        print("You Win!")