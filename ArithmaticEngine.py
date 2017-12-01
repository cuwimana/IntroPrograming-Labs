
#NumberEngine
#Author:Charlotte Uwimana
# Lab #10
# 12/1/2017
#=============================================================
#allow the user to enter two number and to choose the operation
# show intro _____ loop _________end
# Ask for a command---ask for two numbers ---perform opr or quit: use if-elif-else---show the result
# commands: " add, mult, diff, quot, quit
#Using try and except to avoid errors that can collapse the program
#================================================================

from graphics import *
#def intro():
    #print("Welcome to Arithematic Engine!\n"
          #"===============================\n")
    #print("This program is allow you to enter two numbers and choose the operation that you want to use.")
    #print()
def end():
    print("\n Thank you for using Arithematic Engine...")
    print("\n please come back again soon!")
    
def loop():
    print("Valid command are: add, mult, diff, quot, and quit")
    while True:
        cmd = input("what the operation you want to perform?: ")
        if cmd == "quit":
            break
        try:
            a = int(input("Enter the first number: "))
            b = int(input ( "Enter the second number: "))
        except:
            print(" ERROR: you must enter valid integers!\n")
              
        if cmd == "add":
            result = a + b
        elif cmd == "mult":
            result = a * b
        
        elif cmd == "diff":
            result = a - b
        elif cmd == "quot":
            result = a // b
        else:
            raise Exception( " ERROR: Invalid comand '" + cmd + " '! Exitings...") 
 
        print( "The result is: " + str(result)+ ".\n")
def main():
    app = GraphWin("Arthimatic Angine", 600, 200)
    app.setCoords(0,0,10,10)
    Text(Point(5,7), "Welcome to Arithematic Engine!\n"
                   "===============================\n")
    Text(Point(4,3), "This program is allow you to enter two numbers and choose the operation that you want to use.")
   
    loop()
    end()
main()

    
        
    
    
    
