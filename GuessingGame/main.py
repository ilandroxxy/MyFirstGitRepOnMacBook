import random

def is_status(x, key):
    if x == key:
        return True
    if x < key:
        print("Число слишком мало, возьмите больше.")
    if x > key:
        print("Число большое, берите меньше.")


print("Добро пожаловать в игру 'Угадай число', начнем играть!")
print("\ncase 1: Start game\ncase 0: Exit game\n")
case = input("case: ")

while True:

    if case == '2':
        case = '1'

    if case == '1':
        print("Игра началась, угадывайте число!")
        key = random.randint(1, 100)
        x = int(input("Введите свое число: "))
        while is_status(x, key) != True:
            x = int(input("Введите свое число: "))
        print("You win!")


    if case == '0':
        print("Спасибо за проведенную игру, Bye!")
        break

    print("\ncase 2: Restart game\ncase 0: Exit game\n")
    case = input("case: ")