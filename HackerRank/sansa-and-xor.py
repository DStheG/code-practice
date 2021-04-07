#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sansaXor function below.
# freq. by window size
# w=1 => 1 1 1 1 1
# w=2 => 1 2 2 2 1
# w=3 => 1 2 3 2 1
# w=4 => 1 2 2 2 1
# w=5 => 1 1 1 1 1 
# w = i xor n-i+1 => 0, we care about w = n+(n-1) / 2 
def sansaXor(arr):
    # in even case result would be 0 
    # because every elements show multiple of 2.
    # so that xor will be zero
    if(not len(arr) % 2):
        return 0
    ret = 0
    for i in range(0, len(arr), 2):
        ret = ret ^ arr[i]
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
