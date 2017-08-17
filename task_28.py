import random

lower_bound = 0
upper_bound = 5
numb_elem = 5

list1 = [random.randint(lower_bound,upper_bound) for x in range(numb_elem)]
list2 = [random.randint(lower_bound,upper_bound) for x in range(numb_elem)]

average_sum1=round(sum(list1)/numb_elem,2)
average_sum2=round(sum(list2)/numb_elem,2)

print("List 1 :", end="  ")
print (list1)
print()
print("List 2 :", end="  ")
print (list2)
print()

#print(average_sum1, average_sum2)
if average_sum1 > average_sum2:
    print ("Arithmetic mean list1 more")
elif average_sum1 < average_sum2:
    print ("Arithmetic mean list2 more")
else:
    print("The arithmetic mean is the same")
