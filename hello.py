import time

def shortPause():
    time.sleep(2)
    
def longPause():
    time.sleep(2.25)
    
if __name__ == "__main__":
    #Variables
    end = False
    test = False
    
    #user name and welcome message
    name = input("Enter your name: ")
    print("\nHello "+name + "...\n")
    shortPause()
    print("Welcome to my game.\n")
    shortPause()
    
    #rules
    print("The rules are simple:\n")
    shortPause()
    print("I am going to take you through a story\n")
    longPause()
    print("and you get to make a decision by entering the letter of the option of your choosing.\n")
    longPause()
    shortPause()
    
    #Test run
    print("Let's do a test run")
    shortPause()
    while test != True:
        testQuestion = input("Select an answer provided: \n[A] Yes \n[B] No\n\n")
        print(testQuestion.lower())
        shortPause()
        if testQuestion.lower() != 'a' or testQuestion.lower() != 'b':
            print("\nThat's not quite how you do it.\n")
            shortPause()
            print("Let's try again\n")
            shortPause()
            print("Type in the letter in block for the option you choose")
            shortPause()
        elif testQuestion.lower() == 'a' or testQuestion.lower() == 'b':
            test = True
    print("\nGood job.,\n")
    shortPause()
    print("That was just the test run, so\n")
    shortPause()
    print("you've already started...")
    
    # while end != false:
    #     print("")
    
    
    
    
    