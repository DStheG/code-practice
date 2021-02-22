#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
  arr.sort()
  
  ret = 0
  runner = 0
  for i in range(len(arr)):
    for r in range(runner, len(arr)):
      if ((arr[r] - arr[i]) == k):
        ret += 1
        runner = r + 1
        break
      elif ((arr[r] - arr[i]) > k):
        runner = r
        break
  return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
