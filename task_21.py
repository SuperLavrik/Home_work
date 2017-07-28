def is_included(number, base):

    while number >= 1:
        digit = number % 10
        if digit == base :
            return True
        number //= 10
        # print (number)
    return False

number = 1000
digit_1 = 1
digit_2 = 7

print ("Numbers containing digits %d and %d less %d :" % (digit_1,digit_2, number))
for i in range(1,number+1):
    if is_included(i,digit_1) or is_included(i,digit_2):
        print (i)
