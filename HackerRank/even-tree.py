#!/bin/python3

import math
import os
import random
import re
import sys

def updateChild(table, t, f):
  for T in range(len(table[t])):
    if(table[T][t] == 1):
      table[T][f] = 1
      #updateChild(table, T, f)
  return table

def findMinOddChild(table):
  idx = 0
  m = len(table)
  for i in range(1, len(table)):
    v = sum(table[i])
    if m > v and v % 2:
      idx = i
      m = v
  print(idx, m)
  return idx

def removeChild(table, idx):
  for i in range(len(table)):
    table[i][idx] = 0
  return table

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
  table = []
  for i in range(t_nodes+1):
    table.append(list([0] * (t_nodes+1)))
  for f, t in zip(t_from, t_to):
    table[t][f] = 1
    table = updateChild(table, t, f)
  for t in table:
    print(*t, sep=' ')
  print('-'*20)
  ret = 0
  while(1):
    idx = findMinOddChild(table)

    if(idx == 0):
      break
    ret += 1
    table = removeChild(table, idx)
    for i in range(len(table[idx])):
      if(table[idx][i] == 1):
        table = removeChild(table, i)
  return ret-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
