import string
import random

def random_selection(numb):
    return code_table[numb][random.randint(0,len(code_table[numb]) - 1)]

code_table = {1: [x for x in string.ascii_lowercase], \
             2 : [x for x in string.digits], \
             3 : [x for x in string.ascii_uppercase]}
code_table[2].append("_")

number_digit_pass = 8     # in this decisions  must be more 3
password = []

for i in [1,2,3]:                   # for obligatory symbols
    password.append(random_selection(i))

for _ in range(1,number_digit_pass - 2):
    password.append(random_selection(random.randint(1,3)))

random.shuffle(password)
key_password = ""

for i in password:
    key_password += i

print ("You %d symbol pasword : %s" %(number_digit_pass,key_password))
