#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
  ret = [[] for i in range(100)]
  
  l = len(arr)
  cnt = 1
  th = l // 2
  for x, s in arr:
    x = int(x)
    S = s if cnt > th else '-'
    ret[x].append(S)
    cnt += 1
  s = ''
  for r in ret:
    s += ' ' + ' '.join(r)
  print(s[1:].strip())

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
