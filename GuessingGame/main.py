import random
import time

def is_status(x, key, dep):
    if x == key:
        return True
    if x < key:
        dep[0] = x
        print("Число слишком мало, возьмите больше",
              dep)
    if x > key:
        dep[1] = x
        print("Число большое, берите меньше", dep)

Result = []


print("Добро пожаловать в игру 'Угадай число', начнем играть!")
print("\ncase 1: Start game\ncase 0: Exit game\n")
case = input("case: ")

while True:
    if case == '2':
        case = '1'

    if case == '1':
        print("Игра началась, угадывайте число!")
        score = 0
        Deaposon = [1, 100]
        key = random.randint(1, 100)
        x = int(input("Введите свое число: "))
        score += 1
        while is_status(x, key, Deaposon) != True:
            x = int(input("Введите свое число: "))
            score += 1
        print("You win!\nYour Score:", score)
        s = 'score: ' + str(score) + '   ' + time.ctime()
        Result.append(s)

    if case == '3':
        for i in range(0, len(Result)):
            print(str(i + 1) + ') ', Result[i])


    if case == '0':
        print("Спасибо за проведенную игру, Bye!")
        break

    print("\ncase 2: Restart game\ncase 3: Show the results table\ncase 0: Exit game\n")
    case = input("case: ")