#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
  m = n // 2
  s1 = list(s[:m])
  s2 = list(s[::-1][:m])
  
  cnt = 0
  for a, b in zip(s1, s2):
    if (a != b):
      cnt += 1
  if (cnt > k):
    return '-1'
  
  for i in range(m):
    if(s1[i] != s2[i]):
      s1[i] = s2[i] = max(s1[i], s2[i])
      s1[i] += '*'
      k -= 1
  print(k, s1, s2)
  for i in range(m):
    if (k and s1[i][0] != '9'):
      temp = 2 if len(s1[i]) == 1 else 1
      if (k >= temp):
        s1[i] = s2[i] = '9*'
        k -= temp
  
  li = []
  if n % 2 :
    c = list(s[m] if k == 0 else '9')
    li = c
  print(s1, li, s2)
  li = s1 + li + s2[::-1]
  ret = [c[0] for c in li]

  return ''.join(ret)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
