#!/bin/python3

import math
import os
import random
import re
import sys

def digit(n):
    ret = 0
    while (n):
        ret += n % 10
        n = n // 10
    return ret
# Complete the superDigit function below.
def superDigit(n, k):
    acc = 0
    for a in n:
        acc += int(a)
    N = acc * k
    while(N > 10):
        N = digit(N)
    return N

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
