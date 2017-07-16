def sum_of_digits(numerik):
    string = str(numerik)
    summa = int(string[0])+int(string[1])+int(string[2])
    return summa

number = 739
print("Сумма цифр числа %d равна %d" % (number, sum_of_digits(number)))