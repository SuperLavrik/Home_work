def sum_of_power(number, base):
     sum = 1
     power = 1
     while base**power <= number :
         sum += base**power
         power += 1
     return sum

number = 1000000
base = 3
print  ("The sum of all degrees nuber of %d less then %d = %d" % \
        (base, number, sum_of_power(number, base)))


