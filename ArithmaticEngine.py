
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
def intro():
    app = GraphWin("Arthimatic Angine", 600, 200)
    app.setCoords(0,0,10,10)
    Text(Point(4,7), "Welcome to Arithmatic Engine!\n"
                   "===============================\n").draw(app)
    Text(Point(4,3), "This program is allow you to enter two numbers\n"
                     "and choose the operation that you want to use\n.").draw(app)
    Text(Point(4,1), " The valid command are: add, mult, diff, quot, and quit").draw(app)

    inputBox = Entry(Point(8,1), 6).draw(app)
    while app.getKey() != "Return": pass
    cmd = inputBox.getText()
    app.close()
    return cmd

def getData(cmd):
    app = GraphWin("Arthmatic Engine", 600, 200)
    app.setCoords (0,0,10,10)

    Text(Point(5,6), " Enter two numbers. ").draw(app)

    num1 = Entry(Point(8,3), 6).draw(app)
    num2 = Entry(Point(8,1), 6).draw(app)

    while app.getKey()!= "Return": pass
    num1 = float(num1.getText())
    num2= float(num2.getText())
  
    if cmd == "add":
        result = num1 + num2
    elif cmd == "mult":
        result = num1 * num2
    elif cmd == "diff":
        result = num1 - num2
    elif cmd == "quot":
        result = num1 // num2
    else:
        pass
    Text(Point(5,4), ("The result is: " + str(result)+ ".\n")).draw(app)
    if app.getKey() == "Return":
        app.close()
    
def loop():
    cmd = intro()
    while cmd != "quit":
        if cmd in ["add", "diff", "mult", "quot"]:
            try:
                getData(cmd)
            except ValueError:
                print("ERROR: You must enter valid integers!\n")
                continue
            except ZeroDivisionError:
                print("You can not divide by zero.")
        else:
            print(" you have entered an invalid command.")
            return    
   
def end():
    print("\n Thank you for using Arithematic Engine...")
    print("\n please come back again soon!")
    
def main():  
    loop()
    end()
main()

    
        
    
    
    
