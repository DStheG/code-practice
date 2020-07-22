#!/bin/python3

import math
import os
import random
import re
import sys

def counting(n, grid, bomb):
  if(n == 0):
    return grid

  row = len(grid)
  col = len(grid[0])

  for i in range(row):
    for j in range(col):
      if(grid[i][j] == 1):
        if(i-1 >= 0 and grid[i-1][j] != 1):
          grid[i-1][j] = -1
        if(i+1 < row and grid[i+1][j] != 1):
          grid[i+1][j] = -1
        if(j-1 >= 0 and grid[i][j-1] != 1):
          grid[i][j-1] = -1
        if(j+1 < col and grid[i][j+1] != 1):
          grid[i][j+1] = -1
        grid[i][j] = -1

  for i in range(row):
    for j in range(col):
      if(grid[i][j] > 0):
        grid[i][j] -= 1
      elif(grid[i][j] == -1):
        grid[i][j] = 0
      elif(grid[i][j] == 0 and bomb != 0 and bomb % 2):
        grid[i][j] = 3
  print(grid)

  if(n > 4):
    n = 4 + (n % 4)
  return counting(n-1, grid, bomb+1)

# Complete the bomberMan function below.
def bomberMan(n, grid):
  ret = []
  if not n % 2 :
    for i in range(len(grid)):
      l = len(grid[0])
      ret.append('O' * l)
  else:
    G = []
    for i in range(len(grid)):
      l = list(grid[i])
      for j in range(len(l)):
        if(l[j] == '.'):
          l[j] = 0
        else:
          l[j] = 3
      G.append(l)
    v = counting(n, G, 0)
    for i in range(len(v)):
      l = []
      for j in range(len(v[i])):
        if(v[i][j] == 0):
          l.append('.')
        else:
          l.append('O')
      ret.append(''.join(l))

  return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
