import numpy as np

a = 0
b = 0
c = 0
d = 0
other = []
crater = []
dark_dune = []
streak = []
bright_dune = []
impact = []
edge = []

file = open('labels-map-proj.txt',  'r')

for line in file:
    b = b + 1  
    words = line.split()
    for word in words:
      c = c + 1
      #print(len(word))
      if (len(word) == 1):
        d = d + 1
        if (word[0] == 0):
          other.append(float(word))
          a = a + 1
        if (word[0] == 1):
          crater.append(float(word))
          a = a + 1
        if (word[0] == 2):
          dark_dune.append(float(word))
          a = a + 1
        if (word[0] == 3):
          streak.append(float(word))
          a = a + 1
        if (word[0] == 4):
          bright_dune.append(float(word))
          a = a + 1
        if (word[0] == 5):
          impact.append(float(word))
          a = a + 1
        if (word[0] == 6):
          edge.append(float(word))
          a = a + 1

print (b, c, d, a)