#  File: CalcSqrt.py

#  Description: This program calculates the square root of a number n and returns the square root and the difference.

#  Student Name: Alexis Emperador

#  Student UT EID: ase369

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 9/29/10

#  Date Last Modified: 9/30/10
##################################
def main():
  #Prompts user for a + number
  n = input ("Enter a positive number: ")

  #Checks if the number is positive and if not reprompts the user
  while ( n < 0 ):
    print ("That's not a positive number, please try again.")
    n = input ("Enter a positive number: ")

  #Calculates the initial guesses
  oldGuess = n / 2.0
  newGuess = ((n / oldGuess) + oldGuess) / 2.0

  #Loops the algorithm until the guess is below the threshold
  while ( abs( oldGuess - newGuess ) > 1.0E-6 ):
    oldGuess = newGuess
    newGuess = ((n / oldGuess) + oldGuess) / 2.0

  #Calculates the difference between the actual square and guessed
  diff = newGuess - (n ** .5)

  #Prints the results
  print 'Square root is: ', newGuess
  print 'Difference is: ', diff

main()
