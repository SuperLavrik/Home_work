import random

number_elem = 20

lower_bound  = -100
upper_bound = 100

lst = [random.randint(lower_bound, upper_bound) for i in range(number_elem)]

print ("Basic list :")
print (lst)
print ()

sort_lst = lst.copy()
sort_lst.sort()

for i in range(len(lst)):
    if lst[i] == sort_lst[0]:
        lst[i] = sort_lst[len(lst)-1]
    elif sort_lst[len(lst)-1] == lst[i]:
         lst[i] = sort_lst[0]

print ("Transformed list :")
print(lst)






# min=list[0]
# numb_min = 0
# max=list[0]
# numb_max = 0
#
# for i in range(1,number_elem):
#     if min > list[i]:
#         min = list[i]
#         numb_min = i
#     elif max < list[i]:
#         max = list[i]
#         numb_max = i
# print (min,numb_min)
# print (max,numb_max)