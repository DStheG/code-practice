#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.
def isSubStr(S, sS):
  if (not len(S)):
    return True
  idx = 0

  for s in sS:
    if (S[idx] == s):
      idx += 1
    if (idx >= len(S)):
      return True
  return False

def getGroups(A):
  group = []
  i = 1
  while(len(A)):
    if (i == len(A)):
      group.append(A)
      break
    if (A[i].islower() != A[i-1].islower()):
      group.append(A[:i])
      A = A[i:]
      i = 0
    i += 1
  return group

def getUppers(gr):
  ret = []
  for g in gr:
    if(g.isupper()):
      ret.append(g)
  return ret

def getCountStr(uppers, b):
  ret = []
  for u in uppers:
    c = b.count(u)
    ret.append((u, c))
  return ret

def find_indices(s, S):
  ret = []
  start = 0
  
  while True:
    r = S.find(s, start)
    if r == -1:
      break
    ret.append(r)
    start = r + len(s)
  return ret

def numOfUpper(S):
  cnt = 0
  for c in S:
    C = ord(c)
    if (C >= ord('A') and C <= ord('Z')):
      cnt += 1
  return cnt

def solve(a, b, d):
  if(a == b):
    return True
  if(len(b) == 0 and getUppers(a) == 0):
    return True
  if(getUppers(a) == 0 and len(a)):
    return True if isSubStr(b, a.upper()) else False

  group = getGroups(a)
  uppers = list(set(getUppers(group)))

  uppers.sort(key=len, reverse=True)
  cnt = getCountStr(uppers, b)

  if(len(cnt) == 0):
    return False
  for c in cnt:
    if(c[1] == 0):
      return False

  cnt.sort(key=lambda x : x[1], reverse = True)
  key = cnt[0][0]
  idx = find_indices(key, b)

  la = a[:a.find(key)]
  ra = a[a.find(key)+len(key):]

  for i in idx:
    lb = b[:i]
    rb = b[i+len(key):]
    
    if( len(lb) > len(la) ):
      print(i, d, 'Key: ', key, 'b:', b, 'la: ', la, 'ra: ', ra, 'lb: ', lb, 'rb: ', rb)
      print('False 1')
      return False
    if (len(rb) > len(ra) ):
      print(i, d, 'Key: ', key, 'b:', b, 'la: ', la, 'ra: ', ra, 'lb: ', lb, 'rb: ', rb)
      print('False 2')
      return False
    if (len(lb) < numOfUpper(la)):
      print(i, d, 'Key: ', key, 'b:', b, 'la: ', la, 'ra: ', ra, 'lb: ', lb, 'rb: ', rb)
      print('False 3', len(lb), numOfUpper(la))
      return False
    if (len(rb) < numOfUpper(ra)):
      print(i, d, 'Key: ', key, 'b:', b, 'la: ', la, 'ra: ', ra, 'lb: ', lb, 'rb: ', rb)
      print('False 4')
      return False
    
    if(solve(la, lb, d+1) and solve(ra, rb, d+1)):
      return True
  
  return False

def abbreviation(a, b):
  return 'YES' if solve(a, b, 0) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
