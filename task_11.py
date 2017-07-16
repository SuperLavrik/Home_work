import math

def deg_to_rad(deg):
    rad = deg * math.pi / 180
    print("Косинус %d градусов равен %.4f " % (deg, math.cos(rad)))
    return

deg_to_rad(40)
deg_to_rad(45)
deg_to_rad(60)

