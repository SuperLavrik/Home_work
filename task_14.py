def even_or_not(number):
    if number%1:
        print("Не целое число")
        return
    if number%2:
        print ("Число нечетное")
        return
    else:
        print("Число четное")
    return

you_number = 890
print(you_number)
even_or_not(you_number)
