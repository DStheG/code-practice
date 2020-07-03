#!/bin/python3

import math
import os
import random
import re
import sys

def sol(L, mi, ma, pos, direction):
  MIN = min(mi,ma) - 1
  MAX = max(mi,ma) + 1
  left = list(filter(lambda o: o[direction] < pos[direction], L))
  right = list(filter(lambda o: o[direction] > pos[direction], L))

  for l in left:
    MIN = max(MIN, l[direction])
  for r in right:
    MAX = min(MAX, r[direction])
  print(MIN, MAX)
  return abs(MAX - MIN - 2)

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
  ret = 0
  row = list(filter(lambda o: o[0] == r_q, obstacles))
  ret += sol(row, 1, n, (r_q, c_q), 1)
  col = list(filter(lambda o: o[1] == c_q, obstacles))
  ret += sol(col, 1, n, (r_q, c_q), 0)
  a = r_q - c_q
  dia1 = list(filter(lambda o: o[0] - o[1] == a, obstacles))
  ret += sol(dia1, max(1+a, 1), min(n, n+a), (r_q, c_q), 0)
  b = r_q + c_q
  dia2 = list(filter(lambda o: o[0] + o[1] == b, obstacles))
  ret += sol(dia2, min(n, -1+b), max(1, -n+b), (r_q, c_q), 0)
  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
