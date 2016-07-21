#!/usr/bin/env python
import sys
import os
from random import randint

# variables
m = 1

# save argv
txt1 = sys.argv[1];
txt2 = sys.argv[2];

# method diff
def diff():
    with open(txt1) as text_one, open(txt2) as text_two:
     return set(text_one) ^ set(text_two)

# check if a file exists
while os.path.exists('test-bootstrap['+str(m)+'].dat'):
      m = m + 1

# save the changes between files
if __name__ == '__main__':
    with open('test-bootstrap['+str(m)+'].dat', 'w') as result:
        for i in diff():
            result.write(i)