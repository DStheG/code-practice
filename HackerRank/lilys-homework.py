#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def travel(li, i):
  idx = i
  ret = 0
  while(li[idx][1] != -1) :
    ret += 1
    i = li[idx][1]
    li[idx][1] = -1
    idx = i
  return ret

def getCost(li):
  ret = 0
  for i in range(len(li)):
  
    if (li[i][1] == -1):
      continue
    ret += (travel(li, i) - 1)
  return ret

def lilysHomework(arr):
  ali = [[arr[idx], idx] for idx in range(len(arr))]
  dli = [[arr[idx], idx] for idx in range(len(arr))]

  ali.sort(key = lambda l:l[0])
  dli.sort(key = lambda l:l[0], reverse=True)
  
  print(ali)
  cost1 = getCost(ali)
  print(dli)
  cost2 = getCost(dli)
  return min(cost1, cost2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
