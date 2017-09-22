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
    elif guess == "quit":
        break
    else:
        print( "Ooops!! The answer is wrong. Try again. ")
        
    
    

