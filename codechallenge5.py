x = eval(input("Enter a factorial number : "))
print ("The factorial number is " , x )
 
breakdown = 1

for sol in range (x,0,-1):
    breakdown *= sol 


print("This is the total of the factorial : ", x ," , you've inputted : " , breakdown)
