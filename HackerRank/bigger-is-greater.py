#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
  W = list(w[::-1])
  
  for i in range(len(W)):
    for j in range(i):
      if W[i] < W[j]:
        ret = W[:i]
        ret[j] = W[i]
        ret.sort(reverse=True)
        ret = ret + list(W[j]) + W[i+1:]
        ret = ret[::-1]
        return ''.join(ret)
  return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
