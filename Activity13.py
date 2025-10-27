import time
y = 0
for x in range (1,11,1):
    nums = eval(input("Input a number : "))
    print ("Input count <",x,">")
    time.sleep(0.5)
    y += nums 
print ("\t \t The total of the numbers you've input is : ", y)
