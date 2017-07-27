import random

def average():
    summa = 0
    for _ in range(101):
        summa += random.randint(-10000, 10000)
    return summa / 100

print("Average 100 random numbers = %.2f" % average())