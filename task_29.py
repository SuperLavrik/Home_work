import random

lower_bound = -1
upper_bound = 1
numb_elem = 11

list = [random.randint(lower_bound,upper_bound) for x in range(numb_elem)]
list_count = [list.count(-1),list.count(0),list.count(1)]

print("Basic list:")
print (list)
print()

if list_count.count(4) == 2 or list_count.count(5) == 2:
    pass
else :
    print ("Element %d repeats %d times " % \
           (list[list_count.index(max(list_count))], max(list_count)))
