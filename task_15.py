import math

def is_cross(x1,y1,r1,x2,y2,r2):
    distans = math.hypot(abs(x2 - x1), abs(y2 - y1))
    if (r1+r2) >= distans and abs(r2 - r1) <= distans :
        return True
    else :
        return False

x1 = 1
y1 = 1
r1 = 1

x2 = -1
y2 = -1
r2 = 2

if is_cross(x1,y1,r1,x2,y2,r2):
    print ("Circle inersect")
else :
    print("Circles don't intersect")
