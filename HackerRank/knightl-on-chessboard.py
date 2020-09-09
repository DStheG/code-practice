#!/bin/python3

import math
import os
import random
import re
import sys

m_value = 25*25

def travel(n, pos, step, visit, cnt):
  x, y = pos
  step_x, step_y = step

  if(x < 0 or y < 0 or x >= n or y >= n):
    return

  if(visit[y][x] == -1 or visit[y][x] > cnt):
    visit[y][x] = cnt
    travel(n, (x+step_x, y+step_y), step, visit, cnt+1)
    travel(n, (x-step_x, y+step_y), step, visit, cnt+1)
    travel(n, (x+step_x, y-step_y), step, visit, cnt+1)
    travel(n, (x-step_x, y-step_y), step, visit, cnt+1)
    travel(n, (x+step_y, y+step_x), step, visit, cnt+1)
    travel(n, (x-step_y, y+step_x), step, visit, cnt+1)
    travel(n, (x+step_y, y-step_x), step, visit, cnt+1)
    travel(n, (x-step_y, y-step_x), step, visit, cnt+1)

  return visit

def travel2(n, pos, step, visit, cnt):
  l = [(pos, cnt)]
  step_x, step_y = step

  while(len(l)):
    p, cnt_t = l.pop(0)
    x, y = p

    if(x < 0 or y < 0 or x >= n or y >= n):
      continue

    if(visit[y][x] == -1 or visit[y][x] > cnt_t):
      visit[y][x] = cnt_t
      l.append(((x+step_x, y+step_y), cnt_t+1))
      l.append(((x-step_x, y+step_y), cnt_t+1))
      l.append(((x+step_x, y-step_y), cnt_t+1))
      l.append(((x-step_x, y-step_y), cnt_t+1))
      l.append(((x+step_y, y+step_x), cnt_t+1))
      l.append(((x-step_y, y+step_x), cnt_t+1))
      l.append(((x+step_y, y-step_x), cnt_t+1))
      l.append(((x-step_y, y-step_x), cnt_t+1))

  return visit

# Complete the knightlOnAChessboard function below.
def knightlOnAChessboard(n):
  ret = []
  visit = []
  for _ in range(n-1):
    ret.append([m_value] * (n-1))

  for y in range(n-1):
    for x in range(n-1):
        visit = []
        for _ in range(n):
          visit.append([-1] * n)
        ret[y][x] = travel2(n, (0, 0), (x+1, y+1), visit, 0)[n-1][n-1]
  
  return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
