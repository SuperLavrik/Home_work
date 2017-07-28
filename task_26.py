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
print ("Simple numbers less 100 :")
for i in range(1,100):
    if is_simple(i):
        print (i)
