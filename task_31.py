import string
import random

def random_selection(numb):
    return code_table[numb][random.randint(0,len(code_table[numb]) - 1)]

code_table = {1: [x for x in string.ascii_lowercase], \
             2 : [x for x in string.digits], \
             3 : [x for x in string.ascii_uppercase]}


number_digit_pass = 8    # in this decisions  must be more 3
password = []

for i in range(1,len(code_table.keys())):                   # for obligatory symbols
    password.append(random_selection(i))

code_table[2].append("_")

for _ in range(number_digit_pass - len(code_table.keys()) + 1 ):
    password.append(random_selection(random.choice\
                        (list(code_table.keys()))))

random.shuffle(password)
key_password = "".join(password)

print ("You %d symbol password : %s" %(number_digit_pass,key_password))
