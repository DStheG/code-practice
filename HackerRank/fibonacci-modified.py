#!/bin/python3

import math
import os
import random
import re
import sys

def fm(t, tt, n, N):
  a = t + tt*tt
  if(n == N):
    return a
  else:
    return fm(tt, a, n, N+1)

# Complete the fibonacciModified function below.
def fibonacciModified(t1, t2, n):
  return fm(t1, t2, n, 3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
