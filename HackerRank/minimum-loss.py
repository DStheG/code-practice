#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    PRICE = []
    for i in range(len(price)):
      PRICE.append((price[i], i))
    sorted_price = sorted(PRICE)
    ret = 10**16
    for i in range(1, len(sorted_price)):
      p0, idx0 = sorted_price[i-1]
      p1, idx1 = sorted_price[i]
      diff = p1 - p0
      if(diff < ret and idx0 > idx1):
        ret = diff
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
