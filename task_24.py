import random

random_number = random.randint(1,10)
while True:
    user_choice = int(input(" Ваш выбор {1.....10} ?"))
    if 1 <= user_choice <= 10:
        if user_choice == random_number:
            print()
            print("Поздравляю! Вы угадали !")
            break
        elif user_choice < random_number:
            print()
            print("Загаданное больше. Пробуйте еще...")
        else:
            print()
            print("Загаданное меньше. Пробуйте еще...")
    else :
        print()
        print("Неверный выбор. Повторите")




