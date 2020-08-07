#!/bin/python3

import math
import os
import random
import re
import sys

def setVisit(M, pos):
  x,y = pos
  M[y][x] = 2

def fillRegion(M, pos, size):
  x,y = pos
  n,m = size

  if(x < 0 or y < 0 or x >= m or y >= n):
    return 0
  if(M[y][x] != 1):
    return 0
  
  ret = 1
  setVisit(M, pos)

  for i in range(-1, 2):
    for j in range(-1, 2):
      ret += fillRegion(M, (x+j, y+i), size)
  return ret

# Complete the connectedCell function below.
def connectedCell(matrix):
  l = []
  n = len(matrix)
  m = len(matrix[0])
  for mat in matrix:
    l.append(list(mat))
  
  ret = 0
  for i in range(n):
    for j in range(m):
      ret = max(ret, fillRegion(l, (j, i), (n, m)))

  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
