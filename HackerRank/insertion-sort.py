#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
L = [0] * 100001
def update_sum(arr, a, v):
  Len = len(arr)
  while(a < Len):
    l = L[a]
    arr[a] += v
    a += l
    
def get_sum(arr, a):
  ret = 0
  while(a > 0):
    l = L[a]
    ret += arr[a]
    a -= l
  return ret
    
def insertionSort(arr):
  ARR = sorted(set(arr))
  look_up = [-1] * 10000001
  for i in range(len(ARR)):
    I = i +1
    L[I] = I & -I
    a = ARR[i]
    look_up[a] = I
  tree = [0] * (len(ARR)+1)
  ret = 0
  for i in range(len(arr)):
    v = look_up[arr[i]]
    ret += (i - get_sum(tree, v))
    update_sum(tree, v, 1)
  return ret

def insertionSort0(arr):
  table = [0] * 10000001
  ret = 0
  for i, a in zip(range(0, len(arr)), arr):
    ret += (i - get_sum(table, a))
    update_sum(table, a, 1)
  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
