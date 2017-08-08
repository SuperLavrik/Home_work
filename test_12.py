import random

create_value = []
for l in range(2,10):
    for k in range (l,10):
        create_value.append(str(l) + " * " + str(k) + " = ")

task_table = {num: create_value[num - 1] for num in range(1,37)}

number_task = 15        # must be less 37
count = 1
while count <= number_task:
    i = random.randint(1,len(create_value))
    if i in task_table:
        print ("Задание %d\t\t%s" %(count,task_table[i]))
        del task_table[i]
        count +=1
