#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
  H = len(A)
  W = len(A[0])
  
  ret = 0
  for i in range(H):
    for j in range(W):
      area = 2
      T = A[i-1][j] if i - 1 >= 0 else 0
      B = A[i+1][j] if i + 1 < H else 0
      L = A[i][j-1] if j - 1 >= 0 else 0
      R = A[i][j+1] if j + 1 < W else 0
      area += max(A[i][j] - T, 0)
      area += max(A[i][j] - B, 0)
      area += max(A[i][j] - L, 0)
      area += max(A[i][j] - R, 0)

      ret += area

  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
