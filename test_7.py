def fibonacci_number(n):
    if n == 0:
        return 1
    elif n == 1 :
        return 1
    else :
        return fibonacci_number(n -1) + fibonacci_number(n-2)


numb_fibonacci = 10
sum_numb_fibonacci = 0

for i in range(numb_fibonacci):
    sum_numb_fibonacci += fibonacci_number(i)

print()
print ("Sum of first %d number Fibonacci = %d" % (numb_fibonacci, sum_numb_fibonacci))