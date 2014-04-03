#  File: Books.py

#  Description: This program takes in two books as text and compares their word frequency to output the differences in words between authors of the books.

#  Student Name: Alexis Emperador

#  Student UT EID: ase369

#  Course Name: CS 303E

#  Unique Number: 52220

#  Date Created: 11/21/10

#  Date Last Modified: 11/29/10


########################################

# Removes punctuation marks from a string
def parseString (st):
  out = ''
  for ch in st:
    if ch.isalpha():
      out = out + ch
    elif ch.isspace():
      out = out + ch
    else:
      out = out + ' '
  return out

#Checks to see if a capitalized word is normal or Proper and increments counts appropriately
def proper(dict):
  f2 = open("words.txt", 'r')
  words = f2.read()
  caps = []
  leng = len(dict)
  for (j, k) in dict.items():
    if j[0].isupper():
      jlo = j.lower()
      if jlo in dict:
        k = k + 1
      else:
        if jlo in words:
          dict[jlo] = 1
      del dict[j]
  return dict

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  dict = {}
  f = open(file, 'r')
  for line in f:
    read = parseString(line)
    read = read.split()
    for i in range(len(read)):
      if read[i] in dict:
        dict[read[i]] = dict[read[i]] + 1
      else:
        dict[read[i]] = 1
  f.close()
  dict = proper(dict)
  return dict
  
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
  set1 = set(freq1)
  set2 = set(freq2)
  total1 = 0
  for (j, k) in freq1.items():
    total1 = total1 + k
  print author1
  print 'Total distinct words = ', len(freq1)
  print 'Total words (including duplicates) =', total1
  print 'Ratio (% of total distinct words to total words) = ', len(freq1)/float(total1) * 100
  print
  total2 = 0
  for (j, k) in freq2.items():
    total2 = total2 + k
  print author2
  print 'Total distinct words = ', len(freq2)
  print 'Total words (including duplicates) =', total2
  print 'Ratio (% of total distinct words to total words) = ', len(freq2)/float(total2) * 100
  print
  print author1 + ' used ' + str(len(set1 - set2)) + ' words that ' + author2 + ' did not use.'
  print 'Relative frequency of words used by' + author1 + ' not common with ' + author2 + ' = ' + str(len(set1 - set2) / float(total1) * 100)
  print
  print author2 + ' used ' + str(len(set2 - set1)) + ' words that ' + author1 + ' did not use.'
  print 'Relative frequency of words used by' + author2 + ' not common with ' + author1 + ' = ' + str(len(set2 - set1) / float(total2) * 100)
  
def main():
  # Enter names of the two books in electronic form
  book1 = raw_input ("Enter name of first book: ")
  book2 = raw_input ("Enter name of second book: ")
  print

  # Enter names of the two authors
  author1 = raw_input ("Enter last name of first author: ")
  author2 = raw_input ("Enter last name of second author: ")
  print 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
