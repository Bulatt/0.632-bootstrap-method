#!/usr/bin/env python
import random
import sys
import os

# variables
i = 1
j = 1
length = 1

# check if a file exists
while os.path.exists('train-random-bootstrap['+ str(i) +'].dat'):
  i = i + 1

# create a file
f = open('train-random-bootstrap['+ str(i) +'].dat', 'w')

# save argv
txt1 = sys.argv[1];

# length of a file 
file_len = open(txt1, 'r')
line = file_len.readline()
while line:
    line = file_len.readline()
    length = length + 1
file_len.close()

# a random selection 
while j < length:
  f.write(random.choice([line for line in open(txt1, 'r')]))
  j=j+1
f.close()