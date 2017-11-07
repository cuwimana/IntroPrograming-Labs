# Lab activity 08
# CMPT 120 - Id personality 
# Author: Charlotte Uwimana
# Date: November 3, 2017

# Demonstrates the use of a matrix for looking up values.


# emotionals
emotion = [ " angry ", "disgusted", " fearful ", "happy", "sad", "suprised"]
angry     = 0
disgusted = 1
fearful   = 2
happy     = 3
sad       = 4
surprised = 5

# kinds of interaction from which the user may choose
action = [ "reward", "punish", "joke", "threaten"]
reward   = 0
punish   = 1
joke     = 2
threaten = 3

# responses that this AI may have when feeling each emotion
responses = [
        " Really! Do be like that please. You are making me feel angry "
    ,   "Stay away from me?"
    ,   "I am really scared righ now."
    ,   "Thank you for making my heart jump with joy."
    ,   "Why can you do that to me? You are really making me sad."
    ,   " Wow! I did not expect that!"
    ]

# personality matrix
personality = [
        # reward  punish  joke   threaten
        [ happy,     sad,   disgusted, angry ] # angry
    ,   [ angry,     angry, disgusted, fearful ] # disgusted
    ,   [ surprised, sad,   surprised, fearful ] # fearful
    ,   [ happy,     sad,   happy,     surprised ] # happy
    ,   [ surprised, sad,   happy,     angry ] # sad
    ,   [ happy,     sad,   happy,     fearful ] # surprised
    ]


def intro():
    global user
    print("Hello! Welcome to the personality game!!!")
    print(" My name is Toto. I am programmed to respond to four different actions:"
          " reward, punish, joke, or threaten.")
    print("To interact with me, enter one of these actions at the prompt.\n")

def ending():
    print("Thank you for stimulating my emotional. Byeee!.")

def primaryLoop():
    currentEmotion = fearful
    while True:
        showEmotion(currentEmotion)
        userAction = getNextInteraction()
        currentEmotion = lookupNewEmotion(currentEmotion, userAction) 

def getNextInteraction():
    userAction = input("Interact> ").strip().lower()
    if userAction == "reward":
        return 0
    elif userAction == "punish":
        return 1
    elif userAction == "joke":
        return 2
    elif userAction == "threaten":
        return 3
def lookupNewEmotion(emotion, action):
    return personality[emotion][action]

def showEmotion(emotion):
    print(responses[emotion])
    
def main():
    intro()
    primaryLoop()
    ending()
main()



    
        
 
