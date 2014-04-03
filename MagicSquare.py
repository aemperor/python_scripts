#  File: MagicSquare.py

#  Description: This program checks to see if a square amount of numbers is a Magic Square. It
#               takes a user specified file as input and returns an output to another user specified file.

#  Developer Name: Alexis Emperador

#  Date Created: 11/4/10

#  Date Last Modified: 11/7/10
#################################

#Takes an input 2D list and returns whether or not it is magic
def isMagic(c):
  sum = 0
  sumtot = []
  #Horizontal Summing
  for i in range(len(c)):
    for k in range(len(c[0])):
      sum = sum + c[i][k]
    sumtot.append(sum)
    sum = 0
  #Vertical Summing
  for m in range(len(c)):
    for n in range(len(c)):
      sum = sum + c[n][m]
    sumtot.append(sum)
    sum = 0
  #L to R Diagonal Summing
  for o in range(len(c)):
    sum = sum + c[o][o]
  sumtot.append(sum)
  sum = 0
  #R to L Diagonal Summing
  for p in range(len(c)):
    sum = sum + c[p][len(c) - 1 - p]
  sumtot.append(sum)
  sum = 0
  result = "valid"
  for x in range(len(sumtot) - 1):
    if sumtot[x] != sumtot[x + 1]:
      result = "invalid"
  return result

def main():
  a = []
  b = []
  c = []

  #Read in the input and open the output
  infile = raw_input("Enter name of input file: ")
  outfile = raw_input("Enter name of output file: ")
  f = open(infile, "r")
  o = open(outfile, "w")
  for line in f.read().split():
    a.append(int(line))
  f.close()

  #Get number of squares in input
  squares = a[0]
  del a[0]

  #Writes number of squares back out
  o.write( str(squares) + "\n" + "\n")

  #Make a 2D list for each square to input into isMagic()
  while squares > 0:
    dimen = a[0]
    del a[0]
    b = a[:dimen ** 2]
    del a[:dimen ** 2]
    while b != []:
      c.append(b[:dimen])
      del b[:dimen]
    #Write out the dimension of the square along with its magic result
    o.write( str(dimen) + " " + isMagic(c) + "\n")
    for i in range(len(c)):
      for x in range(len(c)):
        o.write ( str(c[i][x]))
      o.write( "\n" )
    o.write( "\n" )
    c = []
    squares = squares - 1
  o.close()
  print ""
  print "The output has been written to", outfile
  
main()
