#!/bin/python3

import math
import os
import random
import re
import sys

def flatten(matrix, offset, size):
  Y, X = offset
  m, n = size
  ret = []
  for y in range(Y, Y+m):
    ret.append(matrix[y][X])
  for x in range(X+1, X+n):
    ret.append(matrix[Y+m-1][x])
  for y in range(Y+m-2, Y-1, -1):
    ret.append(matrix[y][X+n-1])
  for x in range(X+n-2, X, -1):
    ret.append(matrix[Y][x])
  return ret
  
def enroll(matrix, offset, size, f):
  Y, X = offset
  m, n = size

  for y in range(Y, Y+m):
    matrix[y][X] = f.pop(0)
  for x in range(X+1, X+n):
    matrix[Y+m-1][x] = f.pop(0)
  for y in range(Y+m-2, Y-1, -1):
    matrix[y][X+n-1] = f.pop(0)
  for x in range(X+n-2, X, -1):
    matrix[Y][x] = f.pop(0)
  return matrix

# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
  m, n = len(matrix), len(matrix[0])
  L = min(m, n)
  for l in range(L//2):
    f = flatten(matrix, (l, l), (m-2*l, n-2*l))
    rot = r % len(f)
    f = f[len(f)-rot:] + f[:-rot] if rot else f
    matrix = enroll(matrix, (l, l), (m-2*l, n-2*l), f)

  for m in matrix:
    print(*m)
  return matrix

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
