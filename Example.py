def main():
  # Prompt the user to enter year
  y = input ("Enter year: ")
  print "y = ", y

  # Compute Easter Sunday for that year
  a = y % 19
  print "a = ", a
  b = y / 100
  print "b = ", b
  c = y % 100
  print "c = ", c

  n = 4
  p = 15

  # Write out the date for Easter Sunday
  print "In", y, "Easter Sunday is on", p,
  if (n == 3):
    print "March"
  if (n == 4):
    print "April"


main()
