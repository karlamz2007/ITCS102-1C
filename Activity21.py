import random 
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print ("ARCADE GUESSING GAME! ")
print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

random_num = random.randint(1,5)
attempt = 0

Game = True

contestant = input("Kindly Enter your name  | ")

while Game == True :
    number = eval(input("Guess a number from 1 - 5 | "))
    attempt =+ 1 

    if number == random_num :
        print ("Congratulations!!")
        break
    else:
        print("You have Guess Incorrectly")
        continue

print(f"Hi {contestant}, Your guess is CORRECT, The number of tries you did is {attempt}")
