def factorial(n):
   if  not n:
       return 1
   f = factorial(n -1) * n
   return f

n = 10
print("Factorial number %d = %d" % (n, factorial(n)))
