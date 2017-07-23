import math
def decision_sq_equation(a,b,c):
    D = b**2 - 4 * a * c
    if D >= 0 :
        xf1 = (- b - math.sqrt(D)) / (2 * a)
        xf2 = (- b + math.sqrt(D)) / (2 * a)
    else :
        xf1 = None
        xf2 = None
    return xf1, xf2

a = 41
b = 34
c = -4

x1, x2 = decision_sq_equation(a, b, c)
if x1 :
    print("X1 = %.2f \nX2 = %.2f" %(x1,x2))
else :
    print("No valid solutions")