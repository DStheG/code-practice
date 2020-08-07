#!/bin/python3

import math
import os
import random
import re
import sys

def split(matrix):
  n = len(matrix)
  mat1 = [m[:n] for m in matrix]
  mat2 = [m[n:][::-1] for m in matrix]
  return mat1, mat2

# Complete the flippingMatrix function below.
def flippingMatrix(matrix):
  n = len(matrix)//2
  Upper = matrix[:n]
  upper1, upper2 = split(Upper)
  Lower = matrix[n:]
  lower1, lower2 = split(Lower)

  L = [m[::-1] for m in zip(*lower1)]
  lower1 = [list(m) for m in zip(*L)]
  L = [m[::-1] for m in zip(*lower2)]
  lower2 = [list(m) for m in zip(*L)]

  a = sum(upper1, [])
  b = sum(upper2, [])
  c = sum(lower1, [])
  d = sum(lower2, [])

  ret = 0
  for m in zip(a, b, c, d):
    ret += max(m)

  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        matrix = []

        for _ in range(2*n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
