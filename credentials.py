# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Your Name Here
# Created: YYYY-MM-DD
def firstlast():
    # get user's first and last names
    first = input("Enter your first name: ").lower()
    last = input("Enter your last name: ").lower()
    # TODO modify this to generate a Marist-style username
    return first,last

def username():
    first,last = firstlast()
    uname = first +"." + last + "1"
    # ask user to create a new password
    return uname
def password():
    passwd = input("Create a new password: ")
    return passwd
    # TODO modify this to ensure the password has at least 8 characters
def checkpassword():
    passwd = password()
    while len(passwd)< 8 and passwd == passwd.upper(): 
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
def main():
    uname = username()
    checkpassword()
    print("The force is strong in this one…")
    print("Account configured. Your new email address is",uname + "@marist.edu")
main()
