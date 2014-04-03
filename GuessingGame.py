##  File: GuessingGame.py

#  Description: This is a game that guesses a number between 1 and 100 that the user is thinking within in 7 tries or less.

#  Student Name: Alexis Emperador

#  Student UT EID: ase369

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 11/10/10

#  Date Last Modified: 11/11/10

###################################
    

def main():

#A series of print statements to let the user know the instructions of the game.
    print "Guessing Game"
    print ""
    print "Directions:"
    print "Think of a number between 1 and 100 inclusive."
    print "And I will guess what it is in 7 tries or less."
    print ""
    answer = raw_input ("Are you ready? (y/n): ")

#If the user inputs that "n", no, he is not ready, prompt him over and over    
    while (answer != "y"):
        answer = raw_input ("Are you ready? (y/n): ")
#If the user inputs yes, start the program
    if (answer == "y"):    
        count = 1
        hi = 100
        lo = 1
        mid = (hi+lo)/2
        print "Guess",count,": The number you thought was:",mid
        correct = raw_input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
        
       
        while (correct != "0"):
#Iterate a loop that resets when correct isn't equal to zero            
            while (count < 7):
#Iterate a loop that stops the program when count gets to 7
                if (correct == "0"):
                    print "I win! Thank you for playing the Guessing Game."
                    break
#If correct == 0 then the program wins 
                if (correct == "1"):
#If correct == 1 then reset the values of hi and lo to take a new average
                    hi = mid
                    lo = lo + 1
                    mid = (hi+lo)/2
                    count = count + 1
                    print "Guess",count, ": The number you thought was:",mid
                    correct = raw_input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
                    
                if (correct == "-1"):
#If correct == -1 then reset the values of hi and lo to take a new average
                    hi = hi + 1
                    lo = mid - 1
                    mid = (hi+lo)/2
                    count = count + 1
                    print "Guess",count, ": The number you thought was:",mid
                    correct = raw_input ("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
            if (count >= 7):
#If count exceeds 7 then the user is not thinking of a number between 1 and 100.
                print "The number you are thinking of is not between 1 and 100."
                break

                

        
    
            
main()        
