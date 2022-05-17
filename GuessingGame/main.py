import random

def is_status(x, key):
    if x == key:
        return True
    if x < key:
        print("Число слишком мало, возьмите больше.")
    if x > key:
        print("Число большое, берите меньше.")


print("Добро пожаловать в игру 'Угадай число', начнем играть!")

while True:
    print("\ncase 1: Start game\ncase 2: Restart game\ncase 0: Exit game\n")
    case = input("case: ")

    if case == '1':
        key = random.randint(1, 100)
        x = int(input("Введите свое число: "))
        while is_status(x, key) != True:
            x = int(input("Введите свое число: "))
        print("You win!")


    if case == '2':
        pass

    if case == '0':
        print("Спасибо за проведенную игру, Bye!")
        break