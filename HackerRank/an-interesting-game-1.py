#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    # Write your code here
    L = len(arr)
    hint = []
    Max = -1
    Idx = -1
    for i in range(L):
        if (arr[i] > Max):
            Max = arr[i]
            Idx = i
            hint.append((Max,Idx))

    return "ANDY" if not len(hint) % 2 else "BOB"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
