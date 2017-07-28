import random

def big_random_number():
    random_number = random.randint(100000000000,999999999999)
    for_print = random_number
    max_digit = random_number % 10
    random_number //= 10
    for _ in range (11):
        if max_digit < random_number % 10:
            max_digit = random_number % 10
        random_number //= 10
    return for_print, max_digit

print("Maximal digit of randon numbers %d = %d" % big_random_number())
