import time
import random
import os

def repsystem():
      if menu == "yes":
      
            print("\t\t\t\t\t***************************************")
            print("\n\t\t\t\t\t\t   >Main Menu< ")
            print("\n\t\t\t\t\t1). Printing using PYTHON ")
            print("\t\t\t\t\t2). Arithmetic Operators & Assignment Operators in PYTHON")
            print("\t\t\t\t\t3). Conditional Statements in PYTHON")
            print("\t\t\t\t\t4). Shapes and Figures in PYTHON")
            print("\t\t\t\t\t5). While Loop in PYTHON")
            print("\t\t\t\t\t6). Extras using Basics in PYTHON")
            print("\t\t\t\t\t7). Exit \n")
            print("\t\t\t\t\t***************************************")
            ans1 = eval(input("Enter the topic or preferred option you're interested in | 1 - 7 | "))
       
            if ans1 == 1 :
                  print(printfunction())
                  rep1 = eval(input("Enter the specific function your're Interested In | 1 - 3 | "))
                  if rep1 == 1 :
                        print(basicprint())
                        time.sleep(5)
                        print(repsystem())
                  elif rep1 == 2:
                        print(inputfunction())
                        time.sleep(5) 
                        print(repsystem())  
                  elif rep1 == 3:
                        print(repsystem())
                  else:
                        print(printfunction())
            elif ans1 == 2:
                  print(operatorsfunction())
                  rep2 = eval(input("Enter the specific function your're Interested In | 1 - 3 | "))
                  if rep2 == 1 :
                        print(operatorssymbols())
                        time.sleep(5)
                        print(repsystem())
                  elif rep2 == 2 :
                        print(basiccal())
                        time.sleep(5)
                        print(repsystem())  
                  elif rep2 == 3:
                        print(repsystem())
                  else:
                        print(operatorsfunction())      
            elif ans1 == 3:
                  print(conditionalfunction())
                  rep3 = eval(input("Enter the specific function your're Interested In | 1 - 3 | "))
                  if rep3 == 1 :
                        print(conditionalbasic())
                        time.sleep(5)
                        print(repsystem())
                  elif rep3 == 2 :
                        print(Tempzer())
                        time.sleep(5)
                        print(repsystem())
                  elif rep3 == 3:
                        print(repsystem())
                  else:
                        print(conditionalfunction())           
            elif ans1 == 4:
                  print(forloopfunction())
                  rep4 = eval(input("Enter the specific function your're Interested In | 1 - 4 | "))
                  if rep4 == 1 :
                        print(rectangle())
                        time.sleep(5)
                        print(repsystem())
                  elif rep4 == 2 :
                        print(pyramid())
                        time.sleep(5)
                        print(repsystem())
                  elif rep4 == 3 :
                        print(kite())
                        time.sleep(5)
                        print(repsystem())
                  elif rep4 == 4 :
                        print(repsystem())
                  else:
                        print(forloopfunction())
            elif ans1 == 5:
                  print(whileloopfunction())
                  rep5 = eval(input("Enter the specific function your're Interested In | 1 - 4 | "))
                  if rep5 == 1 :
                        print(basicwhile())
                        time.sleep(5)
                        print(repsystem())
                  elif rep5 == 2 :
                        print(password())
                        time.sleep(5)
                        print(repsystem())
                  elif rep5 == 3 :
                        print(pokemongame())
                        time.sleep(5)
                        print(repsystem())
                  elif rep5 == 4:
                        print(repsystem())
                  else:
                        print(conditionalfunction())
            elif ans1 == 6:
                  print(extras())
                  rep6 = eval(input("Enter the specific function your're Interested In | 1 - 4 | "))
                  if rep6 == 1 :
                        print(OEdectector())
                        time.sleep(5)
                        print(repsystem())
                  elif rep6 == 2 :
                        print(guessgame())
                        time.sleep(5)
                        print(repsystem())   
                  elif rep6 == 3 : 
                        print(arcadescoring())
                        time.sleep(5)
                        print(repsystem())              
            elif ans1 == 7 :
                        print("______________________________________\n")
                        print("You have successfully exit the Program")
                        print("______________________________________")
      elif menu == "no":
            print("______________________________________\n")
            print("You have successfully exit the Program")
            print("______________________________________")
      else :
            print("______________________________________\n")
            print("Error")
            print("______________________________________")
            time.sleep(5)
            print(repsystem())
def basicprint():
      print("This is basic printing, using the | print('' | function")
      print("\t\t\n Input Sample : ")
      print("\t section = 'BSIT1C' ")
      print("\t age = 18 \n\n")
      print("\t print('Amsterdam')")
      print("\t print('Honda Civic')")
      print("\t print('Technology')")
      print("\t print(section)")
      print("\t print(age)")
      print("\t\t\n Output : ")
      print("\t Amsterdam")
      print("\t Honda Civic")
      print("\t Technology")
      print("\t BSIT1C")
      print("\t 18")
def printfunction():
      print("______________________________________\n")
      print ("   PYTHON PRINTING") 
      print("______________________________________")
      print("\n\t The printing function prints the specified message to the screen. It is the most basic and the first step in PYTHON \n\t\t Text in pyton or print must always be inside QUOTES")
      print("\t\t 1). Basic print | print("") or print(variables) ")
      print("\t\t 2). Input print | name = input("") ")
      print("\t\t 3) >| Navigate back to Main Menu |< ")
def inputfunction():
      print("This is function is used when the system is having an interaction with the user of the system \n using the syntax | name = 'blahblahblah' ")
      print("\n\t\t Input Sample : ")
      print("\t input1 = input('Enter something here ---> ')")
      print("\t input2 = input('Kindly input your name ---> ')")
      print("\n\t\t Output : ")
      inputsample = input("Enter something here ---> ")
      inputsample1 = input("Kindly input your name ---> ")
      print("\n\nYou can also make the user to only input a NUMBER using the | eval() | function ")
      print("\n\t\t Input Sample : ")
      print("\t evalsample = eval(input('Enter a number'))")
      print("\n\t\t Output : ")
      evalsample = eval(input('Enter a number : '))
def operatorsfunction():
      print("______________________________________\n")
      print ("   PYTHON OPERATORS") 
      print("______________________________________")
      
      print("\n\t Operators is often used to add together two values, it can also be used to add together a variable and a value, or two variables \n\t\t Operators are used to perform operations on variables")
      print("\t\t 1). Python Operators Symbols ")
      print("\t\t 2). Simple Calculator using Assignment and Arithmetic Operators ")
      print("\t\t 3) >| Navigate back to Main Menu |< ")
def operatorssymbols():
      print("\t\t\n Operators :")
      print("\t | + | Addition")
      print("\t | - | Subtraction")
      print("\t | * | Multiplication")
      print("\t | / | Division")
      print("\t | & | Modulos")
      print("\t | ** | Exponentiation")
      
      print("(+)")
      firstnum = eval (input("Input a number  : "))
      secondnum = eval (input("Input another number  : "))
      answer = firstnum + secondnum
      print ("The answer sum : \n ", answer)

      print("(-)")
      firstnum = eval (input("Input a number  : "))
      secondnum = eval (input("Input another number  : "))
      answer = firstnum - secondnum
      print ("The difference is : \n ", answer)

      print("(*)")
      firstnum = eval (input("Input a number  : "))
      secondnum = eval (input("Input another number  : "))
      answer = firstnum * secondnum
      print ("The product is : \n ", answer)

      print("(/)")
      firstnum = eval (input("Input a number  : "))
      secondnum = eval (input("Input another number  : "))
      answer = firstnum / secondnum
      print ("The quotient is : \n ", answer)

      print("(&)")
      firstnum = eval (input("Input a number  : "))
      secondnum = eval (input("Input another number  : "))
      answer = firstnum & secondnum
      print ("The answer is : \n ", answer)

      print("(**)")
      firstnum = eval (input("Input a number  : "))
      secondnum = eval (input("Input another number  : "))
      answer = firstnum ** secondnum
      print ("The answer is : \n ", answer)
def basiccal():
      num1 = eval(input('Enter a number : '))
      num2 = eval(input('Enter a number : '))

      add = num1 + num2
      dif = num1 - num2
      prod = num1 * num2
      div = num1 / num2
      mod = num1 % num2
      expo = num1 ** num2

      print('\n\nThe sum of the two numbers you’ve inputted is : ',add)
      print('The difference of the two numbers you’ve inputted is : ',dif)
      print('The product of the two numbers you’ve inputted is : ',prod)
      print('The division of the two numbers you’ve inputted is : ',div)
      print('The modulos of the two numbers you’ve inputted is : ',mod)
      print('The exponential of the two numbers you’ve inputted is : ',expo)
def conditionalfunction():
      print("______________________________________\n")
      print ("   PYTHON Conditional Statements") 
      print("______________________________________")
      print("\n\t The if statement evaluates a condition | an expression that results in TRUE or FALSE |. If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.")
      print("\t\t 1). Explanation and Basics ")
      print("\t\t 2). Simple Temperature Analyzer")
      print("\t\t 3) >| Navigate back to Main Menu |< ")
def Tempzer():
      print("This Temperature Analyzer is example of Conditional Statement using | if , elif , else | ")
      asktemp = eval(input("Input the temperature today : "))

      if ( asktemp <= 0 ):
            print("The temperature today is FREEZING COLD")
      elif (asktemp >= 1 ) and (asktemp <= 20) :
            print("The temperature today is EXTREMELY COLD")
      elif (asktemp >= 21)and (asktemp <= 30) :
            print ("The temperature today is COLD")
      elif (asktemp >= 31) and (asktemp <= 37) :
            print ("The temperature today is LUKEWARM")
      elif (asktemp >= 38) and (asktemp <= 45) :
            print ("The temperature today is HOT")
      elif (asktemp >= 45) and (asktemp <= 50) :
            print ("The temperature today is BOILING HOT")
      elif (asktemp >= 51) and (asktemp <= 1000):
            print ("The temperature today is DANGEROUS, Be Careful")
      else :
            print ("Cannot Analyze this temperature")
def conditionalbasic():
      print("\t x = 25")
      print("\t y = 150")
      print("\t if b > a : \n \t\t print('x is greater than y')")
def forloopfunction():
      print("______________________________________\n")
      print ("   Shapes and Figures in PYTHON") 
      print("______________________________________")
      print("\n\t You can use the For loop functions to create Shapes and Figures and use symbols to formulate the figures and shapes")
      print("\t\t 1). Rectangle")
      print("\t\t 2). Pyramid")
      print("\t\t 3). Kite")
      print("\t\t 4). >| Navigate back to Main Menu |< ")
def rectangle():
      for o in range (1,11,1):
            for z in range (10,o,-1):
                  print("*", end=" ")
            for zz in range (1,o,1):
                  print("*", end=" ") 
            print()
def kite():
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
      print ("\n\t\t *", end = " ")
      print ("\n\t\t *", end = " ")
      print ("\n\t\t *", end = " ")
      print ("\n\t\t *", end = " ")
      print ("\n\t\t *", end = " ")
      print ("\n\t\t *", end = " ")     
def pyramid():
      print ("\t\t *", end = " ")
      for o in range (1,11,1):
          for z in range (10,o,-1):
              print(" ", end=" ")
          for zz in range (1,o,1):
              print("*", end=" ") 
          for zzz in range (1,o,1):
              print("*",end=" ")
          print()     
def whileloopfunction():
      print("______________________________________\n")
      print("   PYTHON While-Loop Functions") 
      print("______________________________________")
      print("\n\t You can use the While-Loop functions to loop a statement or a functions, prints, variables depending on the condition you want. You must use | continue , break | to control the While Loop Function")
      print("\t\t 1). Basic While Loop ")
      print("\t\t 2). While loop")
      print("\t\t 3). Pokemon Game")
      print("\t\t 4). >| Navigate back to Main Menu |< ")
def password():
      print("Keeps asking for the password, Stops only when the correct password is entered")
      password = ""

      while password != "pass99word11":
            password = input("Enter the password: ")

      print("Access Granted!")
def basicwhile():
      print("\t\t\n Input :")
      print("\t i = 1")
      print("\t while i < 8 :")
      print("\t\t print(i)")
      print("\t\t i += 1 ")
      print("the i(1) will keep have an increment every print until it meets the specific condition") 
      print("\t\t\n Output :")
      i = 1
      while i < 8:
            print(i)
            i += 1    
def pokemongame():
      Hero = input("Enter your pokemon name:\t")
      print(Hero, "Greetings!")
      print("A wild Suicide Pokemon has Appeared!!")

      pokemonhealth = 100

      while True:
            pokemon_attack = input("Use Quick Attack (yes/no):\t").lower()

            if pokemon_attack == "yes":
                  pokemonhealth -= 25
                  print("Suicide Pokemon Health Decreased to", pokemonhealth, "%")

                  if pokemonhealth <= 0:
                        print("You have Achieved Victory!!,", Hero)
                        break

            else:
                  print("You have been defeated...")
                  break
def extras():
      print("______________________________________\n")
      print ("   COMBINATION OF BASICS IN PYTHON ") 
      print("______________________________________")   
      print("\n\t This option is also the Basics of PYTHON, but used in its own way and maximixing functions and basics.")
      print("\t\t 1). ODD & EVEN DETECTOR ")
      print("\t\t 2). Guessing Number Game ")
      print("\t\t 3). Arcade Scoring System ")
def OEdectector():
      user = input ("Kindly Enter your name : \t")
      print("PRESS |  0  | TO STOP THE PROGRAM!")
      oddnum = 0
      evennum = 0
      oddlist = ""
      evenlist = ""
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
                  evennum += num
                  evenlist += (f"{num}  |   ")
                  continue
      print("Hi", user, "This is the final sum of all the ODD numner : ", oddnum)
      print("Hi", user, "This is the final sum of all the ODD numner : ", evennum)
      print ("The following Odd numbers you've input is : ", oddlist)
      print ("The following Even numbers you've input is : ", evenlist)
def guessgame():
     
      print("This game used random.int() which is a built in function, and also used While-loop, aritmethic operations, and conditional statements ")
      print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
      print ("ARCADE GUESSING GAME! ")
      print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

      random_num = random.randint(1,5)
      attempt = 0

      Game = True

      contestant = input("Kindly Enter your name  | ")

      while Game == True :
            number = eval(input("Guess a number from 1 - 5 | "))
            attempt += 1 

            if number == random_num :
                  print ("Congratulations!!")
                  break
            else:
                  print("You have Guess Incorrectly")
                  continue
      print(f"Hi {contestant}, Your guess is CORRECT, The number of tries you did is {attempt}")
def arcadescoring():
      
      scores = []   
      running = True

      while running:
            os.system("cls" if os.name == "nt" else "clear")

      print("=================================")
      print("      PYTHON ARCADE SYSTEM")
      print("=================================")
      print("[1] Add Score")
      print("[2] View Scores")
      print("[3] Average Score")
      print("[4] Exit")
      print("=================================")

      choice = input("Choose an option: ")

      if choice == "1":
            score = int(input("Enter your score: "))
            scores.append(score)
            print("Score added!")
            os.system("pause")

      elif choice == "2":
            if len(scores) == 0:
                  print("No scores yet.")
            else:
                  print("Your Scores:")
                  for s in scores:
                        print("-", s)
            os.system("pause")

      elif choice == "3":
            if len(scores) == 0:
                  print("No scores to compute average.")
            else:
                  total = 0
                  for s in scores:
                        total += s
                  average = total / len(scores)
                  print("Average Score:", average)
            os.system("pause")

      elif choice == "4":
            print("Thank you for playing!")
            running = False

      else:
            print("Invalid choice!")
            os.system("pause")
      
      
      
             
print ("Greetings User")
comuser = input("Kindly Input your name --->  ")
print (f"Hii {comuser}, Welcomeee")

menu = input ("Would you like to start the Program? | Yes or no |").lower()

repsystem()

