#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
  ret = 0 
  E = expenditure
  l = len(E)
  e = E[:d-1]
  se = sorted(e)
  midx = d // 2
  
  f = (lambda _ : 2*se[midx]) if d % 2 else (lambda _ : (se[midx-1] + se[midx]))

  for i in range(d-1, l-1):
    e.append(E[i])
    bisect.insort(se, E[i])
    if(f(None) <= E[i+1]):
      ret += 1
    c = e.pop(0)
    idx = bisect.bisect_left(se, c)
    del se[idx]
    
  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
