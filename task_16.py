def is_crash(v1,v2):
    if v1 / v2 > 2 / 3 :
        return True
    else :
        return False

v1 = 4
v2 = 6

if is_crash(v1,v2):
    print ("Trains break off")
else :
    print("We have a crash")
