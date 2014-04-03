#  File: Cipher.py

#  Description: This program encrypts or decrypts the user specified file to the parameter (also user specified) and prints the output in the user specified output file. It uses the Cesar Cipher algorithm.

#  Developer Name: Alexis Emperador

#  Date Created: 10/21/10

#  Date Last Modified: 10/22/10
##############################
import string

#Ask the program to read the file
def read_file (infile):
  readFile = open (infile, "r")
  fileContent = readFile.read()
  readFile.close()
  return fileContent
  
#Encrypt the file
def encrypt(newfile, parameter, outfile):
  enc_file = open (outfile, "w")
  for ch in newfile:
    if (ch.isupper() == True):
      enc_file.write(chr((((ord(ch) - 65) + parameter)%26 +65)))
    if (ch.islower() == True):
      enc_file.write (chr(((ord(ch) - 97) + parameter)%26 +65))
    elif (ch.isdigit() == True):
      enc_file.write(str((((int(ch) + parameter))%10)))
    else:
      enc_file.write(ch)
  enc_file.close()
  
  
#Decrypt the file
def decrypt(oldfile, parameter, outfile):
  dec_file = open (outfile, "w")
  for ch in oldfile:
    if (ch.isupper() == True):
      dec_file.write(chr(((ord(ch) - 65) - parameter)%26 + 65))
    if (ch.islower() == True):
      dec_file.write(chr(((ord(ch) - 97) - parameter)%26 + 97))
    elif (ch.isdigit() == True):
      dec_file.write((chr(((int(ch) - parameter)%10))))
    else:
      dec_file.write(ch)
  dec_file.close()
 
    
def main():
#Prompt the user to input appropriate values  
  enc_dec = raw_input ("Do you want to encrypt or decrypt? (E / D): ")
  infile = raw_input ("Enter the name of input file: " )
  parameter = raw_input ("Enter shift parameter: ")
  outfile = raw_input ("Enter name of output file: ")

#Check for values and initiate correct function
  if (enc_dec == "E"):
    s = read_file(infile)
    encrypt(s, int(parameter), outfile)
  elif (enc_dec == "D"):
    s = read_file(infile)
    decrypt(s, int(parameter), outfile)
#If appropriate values are not inputed print "Invalid Input"
  else:
    print "Invalid input."
    
#Check to see if the parameter is a positive integer
  if (not int(parameter)) or (parameter < 0):
     print "Invalid Input"

#Tell user where it was ciphered
  print "Output written to", outfile
main()
