#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def getIdx(c):
    return ord(c) - ord('a')

def isValid(s):
    li = [0] * (ord('z') - ord('a') + 1)
    for c in s:
        li[getIdx(c)] += 1
    
    li = list(filter(lambda x : x > 0, li))
    
    MostFreqV = 0
    MaxV = 0
    for n in list(set(li)):
        if(li.count(n) > MostFreqV):
            MaxV = n
            MostFreqV = li.count(n)
        elif(li.count(n) == MostFreqV and MaxV > n):
            MaxV = n
            MostFreqV = li.count(n)
    print(li)
    print(MostFreqV, MaxV)
    v = MaxV
    li = list(filter(lambda x: x - v != 0, li))
    if (len(li) == 1 and (abs(li[0] - v) == 1 or li[0] == 1)):
        return 'YES'
    elif (len(li) == 0):
        return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
