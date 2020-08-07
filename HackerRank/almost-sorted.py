#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
  sorted_arr = sorted(arr)
  l = 100001
  r = 0
  if(sorted_arr == arr):
    print('yes')
    return

  for i in range(len(arr)):
    if(sorted_arr[i] != arr[i]):
      l = min(l, i)
      r = max(r, i)
  s_arr = arr[:]
  s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
  r_arr = arr[:l] + arr[l:r+1][::-1] + arr[r+1:]

  if(s_arr == sorted_arr):
    print('yes')
    print('swap %d %d' % (l+1, r+1))
  elif(r_arr == sorted_arr):
    print('yes')
    print('reverse %d %d' % (l+1, r+1))
  else:
    print('no')
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
