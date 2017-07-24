def is_even(number):
    if number%2:
       return False
    else:
        return True

def differens_in_amounts(list):
    differens = 0
    for count in list:
        if is_even(count):
            differens += count      # add even number
        else :
            differens -= count      # subtraction odd number

    return differens

list = [1,34,45,63,32,-38,35,-77,21]
print(list)
print ("Differens = %d" % differens_in_amounts(list))