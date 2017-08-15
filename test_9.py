import random

number_elem = 10

lower_bound  = -100
upper_bound = 100

lst = [random.randint(lower_bound, upper_bound) for i in range(number_elem)]

print ("Basic list :")
print (lst)
print ()

sort_lst = lst.copy()
sort_lst.sort()

if abs(sort_lst[0]) > abs(sort_lst[len(lst)-1]):
    norm = abs(sort_lst[0])
else:
    norm  = abs(sort_lst[len(lst)-1])

norm_lst = [round(lst[m] / norm,2) for m in range(len(lst))]

print ("Norm list :")
print (norm_lst)
