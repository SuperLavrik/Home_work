import math

def distans(xf1,yf1,xf2,yf2):
    dist_of_centr = math.hypot(abs(xf2 - xf1),abs(yf2 - yf1))
    return dist_of_centr

x1 = 1
y1 = 1
r1 = 1

x2 = -1
y2 = -1
r2 = 2

print (distans(x1,y1,x2,y2))