amerikan_date = "11.01.2017"
day =  amerikan_date[3:6]
mouns = amerikan_date[:3]
europion_date = day + mouns + amerikan_date[-4:]

print("Американский формат даты \f%s " %(amerikan_date))
print("Европейский формат даты \f%s " %(europion_date))
