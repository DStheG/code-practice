
#!/bin/python3

import math
import os
import random
import re
import sys

def digest(s):
  n = ord('z') - ord('a') + 1
  d = [0 for _ in range(n)]
  for c in s:
    idx = ord(c) - ord('a')
    d[idx] += 1
  D = ''
  for v in d:
    D += '%02x' % v
  return D

def comb(n,r):
  f = math.factorial
  return f(n) // f(r) // f(n-r)
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
  dic = {}
  for i in range(len(s)):
    l = i + 1
    for j in range(len(s)-i):
      a = s[j:j+l]
      d = digest(a)
      if(not d in dic):
        dic[d] = 0
      dic[d] += 1
  ret = dict(filter(lambda e : e[1] > 1, dic.items()))
  print(ret)
  result = 0
  for r in ret.items():
    result += comb(r[1], 2)

  return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
