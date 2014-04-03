#  File: ISBN.py

#  Description: This program takes an input file and checks each ISBN number in the input and returns the output to an output file with "valid" or "invalid"
#               next to the ISBN number depending on whether it is a valid or invalid ISBN number.

#  Student Name: Alexis Emperador

#  Student UT EID: ase369

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 10/27/10

#  Date Last Modified: 10/29/10
#########################################
import string

def sum_partial(liststr):
#Function to get the partial sum
    s1 = []
    sum = 0
    for item in liststr:
        if (item == "X" or item == "x"):
            item = 10
        sum += int(item)
        s1.append(sum)

#Get the partial sum of s1
    s2 = []
    sum2 = 0

    for item in s1:
        sum2 += item
        s2.append(sum2)

#Check to make sure the partial sum of s1 is evenly divisible by 11
    if s2[-1]%11==0:
        return True
    else:
        return False

def valid(line):
#Function to check the validity of the ISBN    
    blank = ""
#Remove all hyphens
    for ch in line:
        if ch.isalnum():
            blank += ch
#Check all conditions laid out in problem statement            
    if (len(blank) != 10):
        return False
    if not (blank[:9].isdigit()):
        return False
    if not(blank[-1]=="x" or blank[-1] == "X" or blank[-1].isdigit()):
        return False
    else:
        return True

    
    
    

def main():

#Open the file to be read line by line  
    infile = open("isbn.txt","r")
    outfile = open("isbnOut.txt","w")
    
    for line in infile:
        line = line.rstrip("\n") #Remove the new line character
        newlist = []
        for ch in line:
             if ch.isalnum(): #alnum to make sure that there are no hyphens included
                 newlist.append(ch)
#Run validity function to finally return a value in the outfile             
        if valid(line):
            if sum_partial(newlist):
                outfile.write(line + " valid \n")
            else:
                outfile.write(line + " invalid \n")
        else:
            outfile.write(line + " invalid \n")
    

      
main()
