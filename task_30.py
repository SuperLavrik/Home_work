import string
encryption_table = string.ascii_lowercase + string.digits + \
                   " " + string.ascii_uppercase + string.punctuation

# print (encryption_table, len(encryption_table))

user_str = input("Input you snring :  ")
coded_str = ""
for i in range(len(user_str)):
    if user_str[i] in encryption_table:
        for j in range(len(encryption_table)):
            #print(user_str[i], encryption_table[j])
            if user_str[i] == encryption_table[j]:
                if j + 5 > len(encryption_table):
                    j -= len(encryption_table)
                #print(encryption_table[j + 5])
                coded_str += encryption_table[j + 5]
    else :
        print ("Simbol %s not detected" % user_str[i])
        print ("Try again")
        coded_str = ""
        break

print("You coded string : ", coded_str)



