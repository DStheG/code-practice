#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = list(filter(lambda c : c != ' ', s))
    l = len(s)
    rootl = math.sqrt(l)
    row = math.floor(rootl)
    col = math.ceil(rootl)

    result = []
    for i in range(0, l, col):
        result.append(s[i:i+col])

    if(row*col < len(s)):
        row+=1
    r = []
    for i in range(col):
        for j in range(row):
            if(len(result[j]) > i):
                c = result[j][i]
                r.append(c)
        r.append(' ')

    return r

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = encryption('chillout')
    #result = encryption(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
