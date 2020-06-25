#!/bin/python3

import math
import os
import random
import re
import sys

def buildMS(a, b, c, d):
  ms = [a, 15-a-c, c, 15-a-d, 5, 15-c-b, d, 15-d-b, b]
  return ms

def buildAllMS():
  e = [2, 8, 4, 6]
  
  MSs = []
  for i in range(2):
    MSs.append(buildMS(e[0],e[1],e[2],e[3]))
    MSs.append(buildMS(e[0],e[1],e[3],e[2]))
    MSs.append(buildMS(e[1],e[0],e[2],e[3]))
    MSs.append(buildMS(e[1],e[0],e[3],e[2]))

    e = e[2:] + e[:2]
  return MSs

def listAsb(s, mss):
  ret = 99999999
  for ms in mss:
    cost = 0
    for a, b in zip(s, ms):
      cost += abs(a - b)
    ret = min(ret, cost)
  return ret

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
  l = sum(s, [])
  print(l)
  MSs = buildAllMS()
  return listAsb(l, MSs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
