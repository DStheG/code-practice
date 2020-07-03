#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

# x = nk + a
# y = mk + b
# s' = all {x + y}, which a + b mod k != 0
def nonDivisibleSubset(k, s):
    # Write your code here
    bucket = [0 for _ in range(k)]
    for n in s:
      m = n % k
      bucket[m] += 1
    ret = 1 if bucket[0] else 0
    print(bucket)
    for i in range(1, int(k/2)+1):
      if(i == k-i):
        ret += 1
      else:
        ret += max(bucket[i], bucket[k-i])

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
