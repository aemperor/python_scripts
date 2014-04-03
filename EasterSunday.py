#  File: EasterSunday.py

#  Description: This program is an Easter Sunday calculator.

#  Developer Name: Alexis Emperador

#  Date Created: 9/10/10

#  Date Last Modified: 9/11/10
######################################################################


def main():

  y = input ("Enter year: ")
  
  a = y % 19
  
  b = y / 100
  
  c = y % 100
  
  d = b / 4
  
  e = b % 4
  
  g = (8 * b + 13) / 25
  
  h = (19 * a + b - d - g + 15) % 30
  
  j = c / 4
  
  k = c % 4
  
  m = (a + 11 * h) / 319
  
  r = (2 * e + 2 * j - k - h + m + 32) % 7
  
  n = (h - m + r + 90) / 25
  
  p = (h - m + r + n + 19) % 32
  
  
  if (y <= 2010):
    x = "was on "
  else:
    x = "will be on "

  if (n == 3):
    t = "March "
  if (n == 4):
    t = "April "

  print "In " + str (y) +", " + "Easter Sunday " +str (x) +str (t) +str (p) +"."


main()
