import math

def square_and_perimetr_triangle(catheter_1,catheter_2):
    square = catheter_1 * catheter_2 / 2
    gypotenuse = math.sqrt(catheter_1**2 + catheter_2**2)
    perimetr = gypotenuse + catheter_1 + catheter_2
    return (square,perimetr)

a = 53
b = 16
(s,p) = square_and_perimetr_triangle(a,b)
print ("Прямоугольный треугольник с катетами %.2f и %.2f имеет "
       "\nПлощадь %.2f и периметр %.2f" % (a,b,s,p))
