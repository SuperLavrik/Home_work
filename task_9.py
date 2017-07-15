base_string = "Task number nine. While it's simple"
words = base_string.split(" ",2)
new_string = words[0] + " " + words[1].upper() + " " + words[2]

print ("Исходное предложение \t\t\t%s" % base_string)
print ("Преобразованное предложение \t%s" % new_string)