def is_even(number):
    if number%2:
       return False
    else:
        return True

you_number = 89559654
if is_even(you_number):
    print("%d is even" % you_number)
else:
    print("%d is not a even" % you_number)
