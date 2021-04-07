#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
def getNextLowerPowerOf2(n):
    mask = 1 << 63
    while(not (n & mask)):
        print(n, mask)
        mask = mask >> 1
    return mask

def counterGame(n):
    # Write your code here
    flag = True
    while (n != 1):
        P = getNextLowerPowerOf2(n)
        if (P == n):
            n = n // 2
        else :
            n = n - P
        flag = not flag

    return 'Richard' if flag else 'Louise'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
