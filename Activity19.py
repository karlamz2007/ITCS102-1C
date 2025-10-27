print ("\t\t *", end = " ")
for o in range (1,11,1):
    for z in range (10,o,-1):
        print(" ", end=" ")
    for zz in range (1,o,1):
        print("*", end=" ") 
    for zzz in range (1,o,1):
        print("*",end=" ")
    print()

for y in range (10,0,-1):
    for x in range (y,10,1):
        print(" ", end= " ")
    for xx in range (1,y,1):
        print("*", end = " ")
    for xx in range (1,y,1):
        print("*", end = " ")
    print()
print (end=" ")
print ("\t\t *", end = " ")


