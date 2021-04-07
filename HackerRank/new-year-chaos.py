#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes1(q):
    ret = 0
    for i in range(len(q)):
        idx = i + 1
        if(True):
            bribe = 0
            for j in range(i+1, len(q)):
                if(q[i] > q[j]):
                    bribe += 1
            if(bribe > 2):
                print('Too chaotic')
                return
            ret += bribe
    print(ret)
    
def merge(q):
    L = len(q) // 2
    
    if (L == 0):
        return q, 0
    
    l, acc_l = merge(q[:L])
    r, acc_r = merge(q[L:])
    ret = []
    acc = acc_l + acc_r
    for i in range(len(q)):
        if(len(l) == 0):
            n = r.pop(0)
        elif(len(r) == 0):
            n = l.pop(0)
        elif(l[0] < r[0]):
            n = l.pop(0)
        else:
            acc += len(l)
            n = r.pop(0)
        ret.append(n)
    return ret, acc
    
# Complete the minimumBribes function below.
def minimumBribes(q):
    for i in range(len(q)):
        I = i + 1
        if (q[i] > I):
            if (q[i] - I > 2):
                print('Too chaotic')
                return
                
    bribe = [0] * (len(q) + 1)
    _, ret = merge(q)
    print(ret)
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
