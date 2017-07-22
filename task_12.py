def sum_of_digits(numerik):
    #string = str(numerik)
    number_dec = (numerik-numerik//100 * 100 - numerik%10) / 10
    summa = numerik//100 + number_dec + numerik%10
    #+numerik//100int(string[2])
    return summa

number = 138
print("Сумма цифр числа %d равна %d" % (number, sum_of_digits(number)))