#!/bin/python3

import math
import os
import random
import re
import sys

def validPos(cur, n, m):
  y, x = cur
  if(y < 0 or x < 0 or y >= n or x >= m):
    return False
  return True

def hasAlternative(y, x, Mat):
  block = ['X', 'O', '*']
  if(Mat[y][x] in block):
    return False
  return True

def findPath(matrx):
  lMat = []
  for m in matrix:
    lMat.append(list(m))

  n = len(lMat)
  m = len(lMat[0])

  for i in range(n):
    for j in range(m):
      if lMat[i][j] == '*':
        goal = (i, j)
      elif lMat[i][j] == 'M':
        pos = (i, j)
        lMat[i][j] = '.'
  
  q = [[pos, 0]]

  while(True):
    cur = q.pop(0)
    y, x = cur[0]
    step = cur[1]
  
    if(not validPos(cur[0], n, m)):
      continue
    if(lMat[y][x] == '*'):
      lMat[y][x] = step
      break
    if(lMat[y][x] != '.'):
      continue

    lMat[y][x] = step

    q.append([(y+1, x), step+1])
    q.append([(y-1, x), step+1])
    q.append([(y, x+1), step+1])
    q.append([(y, x-1), step+1])
  
  cur = goal
  ret = 0
  first = True
  fin = False
  while(True):
    y, x = cur
    step = lMat[y][x]
    if(step == 0):
      fin = True
    lMat[y][x] = 'O'

    if(fin):
      break
    prevStep = step-1
    if(validPos((y-1, x), n, m) and lMat[y-1][x] == prevStep):
      cur = (y-1, x)
    elif(validPos((y+1, x), n, m) and lMat[y+1][x] == prevStep):
      cur = (y+1, x)
    elif(validPos((y, x-1), n, m) and lMat[y][x-1] == prevStep):
      cur = (y, x-1)
    elif(validPos((y, x+1), n, m) and lMat[y][x+1] == prevStep):
      cur = (y, x+1)
  
  lMat[goal[0]][goal[1]] = '*'
  for y in range(n):
    for x in range(m):
      cnt = 0
      if(lMat[y][x] == 'O'):
        if(validPos((y-1, x), n, m) and hasAlternative(y-1, x, lMat)):
          cnt += 1
        if(validPos((y+1, x), n, m) and hasAlternative(y+1, x, lMat)):
          cnt += 1
        if(validPos((y, x-1), n, m) and hasAlternative(y, x-1, lMat)):
          cnt += 1
        if(validPos((y, x+1), n, m) and hasAlternative(y, x+1, lMat)):
          cnt += 1
        if(cnt > 0):
          ret += 1

  return ret

# Complete the countLuck function below.
def countLuck(matrix, k):
  ret = findPath(matrix)
  print(ret)
  if(ret == k):
    return 'Impressed'
  return 'Oops!'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
