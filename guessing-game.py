# Guessing game
# Author: Charlotte Uwimana
# Lab Activity 4
# September 22, 2017


animal_Name = "dog"
while True: 
    print(" This program is thinking of an animal")
    guess = input(" guess the name of the animal: ").lower()
    if animal_Name == guess: 
        print("congratulation, you got the name!!!!")
        c = input (" do you like the animal? Y/N ")
    elif guess[0] == "q":
        if c == "Y":
            print(" me too!! ")
        else:
            print ( " Ooops, that is not good.")
        break 
    else:
        print( "Ooops!! The answer is wrong. Try again. ")
        
    
    

