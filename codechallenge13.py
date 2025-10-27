user = input ("Kindly Enter your name : \t")
print("PRESS |  0  | TO STOP THE PROGRAM!")
oddnum = 0
oddlist = ""
numscan = True


while numscan == True:
    num = eval(input("Enter a number :\t"))

    if (num % 2) == 1:
        oddnum += num
        print ("ODD NUMBER DETECTED")
        oddlist += (f"{num}  |   ")
        continue
    elif num == 0:
        print("The program has stopped!") 
        break
    else :
        print("EVEN NUMBER DETECTED")
        continue



print("Hi", user, "This is the final sum of all the ODD numner : ", oddnum)
print ("The following Odd numbers you've input is : ", oddlist)


