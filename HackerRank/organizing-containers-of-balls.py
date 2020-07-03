#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
  sum_rows = [sum(x) for x in container]
  sum_cols = [sum(x) for x in zip(*container)]
  
  vote = []
  for i in range(len(container)):
    for j in range(len(container[0])):
      a = sum_rows[i] - container[i][j]
      b = sum_cols[j] - container[i][j]
      if(a == b):
        vote.append(j)
  
  vote = list(set(vote))
  if(len(vote) == len(container)):
    return 'Possible'
  else:
    return 'Impossible'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
