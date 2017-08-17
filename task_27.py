import random
upper_bound = 100
numb_elem = upper_bound//2

list = [x for x in range(upper_bound) if x%2]

print("Basic list:")
print (list)
print()

random.shuffle(list)
print("Random list:")
print (list)


# for i in range(numb_elem):
#     elem = random.randint(numb_elem)
#     random_list.append(random())
