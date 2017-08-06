import random

create_value = []
j = 2
for l in range(2,10):
    for k in range (j,10):
        create_value.append(str(l) + " * " + str(k) + " = ")
    j += 1

task_table = {num: create_value[num - 1] for num in range(1,37)}

number_task = 20        # must be less 37
count = 1
while count <= number_task:
    i = random.randint(1,36)
    if i in task_table:
        print ("Задание %d\t\t%s" %(count,task_table[i]))
        del task_table[i]
        count +=1
