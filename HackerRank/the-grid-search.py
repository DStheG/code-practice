#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gridSearch function below.
def gridSearch(G, P):
  R = len(G)
  C = len(G[0])
  r = len(P)
  c = len(P[0])

  for i in range(R-r+1):
    for j in range(C-c+1):
      flag = True
      for k in range(r):
        if(G[i+k][j:j+c] != P[k]):
          flag = False
          break
      if(flag):
        return 'YES'
  return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
