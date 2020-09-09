#!/bin/python3

import math
import os
import random
import re
import sys

def m_to_0(A, m):

  i = A.index(m)
  if i % 2 :
    if i == 1:
      a = [A[2]] + [A[0]] + A[3:]
    else:
      a = [A[1]] + [A[0]]
      print(m, i, A[2:i], A[i+1:])
      a = a + A[2:i] + A[i+1:]
    A = a
  else :
    A = A[:i] + A[i+1:]
  return A

# Complete the larrysArray function below.
def larrysArray(A):
  m = min(A)
  while(len(A) > 2):
    A = m_to_0(A, m)
    m = m+1
  sol = sorted(A)
  if(A == sol):
    return 'YES'
  return 'NO'
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
