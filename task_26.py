def is_simple(number):
    if not number%2 and number//2 != 1 :
        return False
    elif not number%3 and number//3 != 1 :
        return False
    elif not number%5 and number//5 != 1 :
        return False
    elif not  number%7 and number//7 != 1:
       return False
    else:
        return True

lower_bound  = 1
upper_bound = 100
print ("Simple numbers more %d and less %d :" %(lower_bound, upper_bound))

for i in range(lower_bound, upper_bound):
    if is_simple(i):
        print (i)
