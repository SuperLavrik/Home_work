import random

def is_number_simple_in_lst(number,lst_simple):
    for i in lst_simple[1:]:
        if number == 1 or number % i == 0 or number == i:
            return False
    return True

lower_bound  = 1
upper_bound = 100
lst_simple = []

for  j in range(1, upper_bound +1):
    if is_number_simple_in_lst(j,lst_simple):
        lst_simple.append(j)

numb_elem = 10

list = [lst_simple[random.randint(0,len(lst_simple))] for x in range(numb_elem)]

print ("List random simple :")
print (list)