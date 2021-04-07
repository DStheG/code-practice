#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pylons function below.
def pylons(k, arr):
    i = 0
    L = len(arr)
    ret = 0
    while(i < L):
        r = i + k - 1
        c = -1
        print(i)
        while(r > i):
            if(r < L and arr[r] == 1):
                c = r
                break
            r -= 1
        if(c == -1):
            l = i
            while(l > i - k):
                if(l >= 0 and arr[l] == 1):
                    c = l
                    break
                l -= 1
        if (c != -1):
            i = c + k
            ret += 1
        else:
            return -1
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
