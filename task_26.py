def is_number_simple_in_lst(number,lst_simple):
    for i in lst_simple[1:]:
        if number == 1 or number % i == 0 or number == i:
            return False
    return True

lower_bound  = 1
upper_bound = 100
lst_simple = []
print ("Simple numbers more %d and less %d :" %(lower_bound, upper_bound))

for  j in range(1, upper_bound +1):
    if is_number_simple_in_lst(j,lst_simple):
        lst_simple.append(j)

for  k in lst_simple:                   # print simple number in preset range
    if k >= lower_bound:
        print (k)
