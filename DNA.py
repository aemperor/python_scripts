#  File: DNA.py

#  Description: This program will find the longest common base sequence in two strands of DNA. The user inputs two strands of DNA and the output are longest common subsequences.

#  Student Name: Alexis Emperador

#  Student UT EID: ase369

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/13/10

#  Date Last Modified: 10/13/10
##############################################

import string

def main():
    
  #Prompt the user to input DNA strands
  strand1 = raw_input ("Enter first strand: ")
  strand2 = raw_input ("Enter second strand: ")
  
  #Take the lengths of the two strands
  size1 = len(strand1)
  size2 = len(strand2)
  
  #Compare sizes and take smaller of the two
  if size1 > size2:
      size = size2
      short = strand2
      longer = strand1
  #Define which is the shorter/longer strand
  else:
      size = size1
      short = strand1
      longer = strand2
  #Iterate a for loop to find each index to return the longest common sequence
  found = False
  for sub_len in range (size,1,-1):
    for idx in range (0, size - sub_len + 1):
      sub_str = short[idx : idx + sub_len]
      if (longer.find(sub_str) != -1):
          print sub_str
          found = True
  #If statement to verify found
    if found:
      break
  #If no sequence found then the program prints "No common sequence found."
  if not found:
    print "No common sequence found."
     

      
main()
