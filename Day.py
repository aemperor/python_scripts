#  File: Day.py

#  Description: This program calculates the day of the week.

#  Student Name: Alexis Emperador

#  Student UT EID: ase369

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 9/23/10

#  Date Last Modified: 9/23/10

#####################################
def main():
  cond = False
  while (not cond):
    day = input ("Enter a day between 1 and 31: ")
    month = input ("Enter a month between 1 and 12: ")
    year = input ("Enter a year between 1900 and 2100: ")
    cond = (1 <= month <= 12) and (1 <= day <= 31) and (1900 <= year <= 2100)

  a = (int(month) + 10) % 12
  b = int(day)
  c = (int(year)) % 100
  d = int(year) / 100

  # Adjust for February 
  if (int(month) == 2):
    a = 12
  # Adjust the year of the century for January and February
  if (int(month) == 1) or (int(month) == 2):
    c = c - 1

  w = (13 * a - 1) / 5
  x = c / 4
  y = d / 4
  z = w + x + y + b + c - 2 * d
  r = z % 7
  r = (r + 7) % 7

  if (r == 0):
    print "The day is Sunday."
  elif (r == 1):
    print "The day is Monday."
  elif (r == 2):
    print "The day is Tuesday."
  elif (r == 3):
    print "The day is Wednesday."
  elif (r == 4):
    print "The day is Thursday."
  elif (r == 5):
    print "The day is Friday."
  else:
    print "The day is Saturday."
    

main ()