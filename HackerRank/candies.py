#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    ret = 0
    i = 0
    cnt = [0] * n
    while(i < n):
        idx = i
        while(idx < n-1 and arr[idx] > arr[idx+1]):
            idx+=1
        print(idx)
        for j in range(idx, i, -1):
            print(j, idx - j + 1)
            cnt[j] = idx - j + 1
        a = 0
        if i > 0 and arr[i-1] < arr[i]:
            a = cnt[i-1]
        b = cnt[i+1] if i < n - 1 else 0
        cnt[i] = max(a+1, b+1)
        i = idx + 1
    return sum(cnt)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
