Hero = input("Enter your pokemon name :\t ")
print (Hero,"Greetings!")
print ("A wild Suicide Pokemon has Appeared!!")

pokemonhealth = 100
isHero = True


while isHero == True:
    pokemon_attack = input("Use Quick Attack  (yes/no) :\t").lower()

    if pokemon_attack == "yes":
        pokemonhealth -= 25
        print ("Suicide Pokemon Health Decreased to ", pokemonhealth, "%")
        continue
    elif pokemonhealth <= 0:
        print ("You have Achieved Victory!!, ", Hero )
        break
    else:
        print("You have been defeated...")
        break    
