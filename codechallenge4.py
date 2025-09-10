print ("Greetings, This is the manga reccomendation")
x = input ("Are you interested ? yes/no ") 

if ( x == "yes" ) or ( x == "YES" ) or ( x == "Yes" ) :
	anime = input ("What genre do you seem to be interested with : romance/action/humandrama \n ") .lower()
	year = input ("What year range manga would you like to read : 1 (2020-2025) , 2 (2011-2019) \n ") .lower()
	L = input ("What manga length do you desire to read : 1 ( long ) , 2 (short) \n ") .lower()
else:
	print("Okay thank you, come back if you seem to be interested in reading some manga")

if (anime == "romance") and (year == '1') and (L == '1') :
	print ("I recommend you to read |  The Fragrant Flower Blooms with Diginity  | ")
elif (anime =="romance") and (year == '2') and (L == '2') :
	print ("I reccommend you to read |  My Little Monster  | ")
elif (anime == "action") and (year == '1') and (L == '1') :
	print ("I reccommend you to read | The Eminence of Shadow | ")
elif (anime == "action") and (year == '2') and (L == '2') : 
	print ("I reccommend you to read | Assasination Classroom |")
elif (anime == "humandrama") and (year == '1') and (L == '1') :
	print ("I reccommend you to read | Frieren | ")
elif (anime == "humandrama") and (year == '2') and (L == '2') :
	print ("I reccommend you to read | Mushishi | ")
else :
	print ("I don't seem to know anything on the particular genre")
