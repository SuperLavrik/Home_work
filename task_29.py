import random

lower_bound = -1
upper_bound = 1
numb_elem = 11

list = [random.randint(lower_bound,upper_bound) for x in range(numb_elem)]
#list = [0,1,0,0,0,1,0,0,0,1,-1]
list_count = [list.count(-1),list.count(0),list.count(1)]
list_elem = [-1,0,1]

print("Basic list:")
print (list)
print()

if list_count[0] == list_count[1] or list_count[0] == list_count[2] \
        or list_count[1] == list_count[2]:
    pass
else :
    print ("Element %d repeats %d times " % \
           (list_elem[list_count.index(max(list_count))], max(list_count)))

