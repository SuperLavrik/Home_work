import string
encryption_table = string.ascii_lowercase + string.digits + \
                   " " + string.ascii_uppercase + string.punctuation

user_str = input("Input you snring :  ")
coded_str = ""

for i in user_str:
    if i in encryption_table:
        j = int(encryption_table.index(i))
        coded_str += encryption_table[(j + 5) % \
                     len(encryption_table)]
    else :
        print ("Simbol %s not detected" % user_str[i])
        print ("Try again")
        coded_str = ""
        break

print("You coded string : ", coded_str)



