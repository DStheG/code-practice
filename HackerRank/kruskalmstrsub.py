#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    # Write your code here
    l = [[f,t,w] for f, t, w in zip(g_from, g_to, g_weight)]
    L = sorted(l, key = lambda x: x[2])
    v = [0 for _ in range(g_nodes+1)]
    
    ret = 0
    for l in L:
      f, t, w = l
      if v[f] == 0 and v[t] == 0:
        v[f] = v[t] = min(f, t)
        ret += w
      elif v[f] == 0 or v[t] == 0:
        v[f] = v[t] = max(v[f], v[t])
        ret += w
      elif v[f] != v[t] and v[f] != 0 and v[t] != 0:
        a = min(v[f], v[t])
        b = max(v[f], v[t])
        v = [a if x == b else x for x in v]
        ret += w
    return ret
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    # Write your code here.
    fptr.write(str(res) + '\n')

    fptr.close()
