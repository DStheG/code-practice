#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if(int(n / 2) < k):
        return [-1]
    if k == 0:
        return [i for i in range(1, n+1)]
    v = 0
    ret = [0 for _ in range(0, n+1)]
    for i in range(1, k+1):
        idx = i
        while(idx <= n):
            v += 1
            ret[idx] = idx + k
            idx = idx + 2 * k
    for i in range(n, n-k, -1):
        idx = i
        while(idx > 0):
            v +=1
            ret[idx] = idx - k
            idx = idx - 2 * k
    if(v != n):
        return [-1]
    return ret[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
