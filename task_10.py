name = "Leo Tolstoy*1828-08-28*1910-11-20"

first_split = name.split("*")

date_of_birth = first_split[1].split("-")
date_of_death = first_split[2].split("-")

lifetime = int(date_of_death[0]) - int(date_of_birth[0])

print ("%s, %d" % (first_split[0], lifetime))
