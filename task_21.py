def is_included(number, base):

    number_thous = number // 1000
    number_cent  = number // 100
    number_dec = number // 10 - number_cent * 10
    number_one =  number - number_thous * 1000 - number_cent * 100\
                  - number_dec * 10
    if number_thous == base or number_cent == base or \
       number_dec == base or number_one == base:
        return True
    else :
        return False

number = 1000
print ("Numbers containing digits 1 and 7 less 1000:")
for i in range(1,number+1):
    if is_included(i,1) or is_included(i,7):
        print (i)
