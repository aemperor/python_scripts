#  File: Goldbach.py

#  Description: This program verifies Goldbach's conjecture in the range 4 through 100 inclusively. It prints out all even numbers in that range.

#  Developer Name: Alexis Emperador

#  Date Created: 10/7/10

#  Date Last Modified: 10/8/10

#################################

def main():
  for i in range (4, 102, 2):
    sum = str(i) #converts sum to a string
    for j in range (2, i/2 + 1):
      two = i - j
      if isPrime(j):
        if isPrime(two):
          j = str(j)
          two = str(two)
          sum = sum + " = " + j + " + " + two
    print sum

#Checks if input is prime
def isPrime(a):
    n = abs(int(a))
    if n < 2:
        return False
    if n == 2:
        return True 
    if not n & 1:
        return False
#Define the range of the algorithm
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

main()
