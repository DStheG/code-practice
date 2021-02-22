#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
def getPoint(Off):
  x1, y1, sz1 = Off
  
  pt1 = [(x1, y) for y in range(y1 - sz1, y1 + sz1 + 1)]
  pt1 += [(x, y1) for x in range(x1 - sz1, x1 + sz1 + 1)]
  return list(set(pt1))

def isOverlap(Off1, Off2):
  pt1 = getPoint(Off1)
  pt2 = getPoint(Off2)
  s = set(pt1+pt2)
  print(pt1, pt2, s)
  return len(s) != (len(pt1)+len(pt2))
  
def getMaxCross(grid, offset, largestSize):
  X, Y = offset
  for sz in range(largestSize - 1, 0, -1):
    flag = True
    for x in range(X - sz, X + sz + 1):
      if (grid[Y][x] == 'B'):
        flag = False
    for y in range(Y - sz, Y + sz + 1):
      if (grid[y][X] == 'B'):
        flag = False
    if (flag):
      return sz
  return 0
    
def twoPluses(grid):
  X, Y = len(grid[0]), len(grid)
  sz = min(X, Y) // 2
  L = []
  for y in range(Y):
    for x in range(X):
      if (grid[y][x] == 'G') :
        l = [x + 1, y + 1, X - x, Y - y]
        off = getMaxCross(grid, (x, y), min(l))
        for i in range(off+1):
          L.append((x, y, i))
  print(L)
  ret = 0
  for i in range(len(L)):
    for j in range(i+1, len(L)):
      if not isOverlap(L[i], L[j]):
        sz = (L[i][2]*4 + 1) * (L[j][2]*4 + 1)
        ret = max(ret, sz)
  return ret
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
