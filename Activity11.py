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
