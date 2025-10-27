print ("\t\t *", end = " ")
for o in range (1,11,1):
    for z in range (1,o,-1):
        print(" ", end=" ")
    for zz in range (1,o,1):
        print("*", end=" ") 
    for zzz in range (1,o,1):
        print("*",end=" ")
    print()
    
