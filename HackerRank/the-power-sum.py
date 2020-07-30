#!/bin/python3

import math
import os
import random
import re
import sys

def solve(toGo, l):
  if(toGo == 0):
    return 1
  if(toGo < 0):
    return 0
  ret = 0
  for i in range(len(l)):
    ret += solve(toGo - l[i], l[i+1:])
  return ret
# Complete the powerSum function below.
def powerSum(X, N):
  newX = [(x+1)**N for x in range(X)]
  newX = list(filter(lambda x : x <= X, newX))
  newX.sort(reverse=True)

  return solve(X, newX)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
