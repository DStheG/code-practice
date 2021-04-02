#!/bin/python3

import math
import os
import random
import re
import sys
import copy
    
# Complete the steadyGene function below.
def search(gene, avg, tot, L, freq, wsz, R1):
    cur = copy.deepcopy(freq[wsz])
    cur['A'] = tot['A'] - cur['A']
    cur['C'] = tot['C'] - cur['C']
    cur['G'] = tot['G'] - cur['G']
    cur['T'] = tot['T'] - cur['T']
    for n in R1:
        m = n + wsz
        if(cur['A'] > avg or cur['C'] > avg or cur['G'] > avg or cur['T'] > avg):
            cur[gene[n]] += 1
            if (m < L):
                cur[gene[m]] -= 1
            else:
                return -1
        else :
            return wsz
    return -1
        
    
def steadyGene(gene):
    freq = [{'A': 0, 'C': 0, 'G': 0, 'T': 0}]
    
    L = len(gene)
    for i in range(L):
        l = copy.deepcopy(freq[i])
        l[gene[i]] += 1
        freq.append(l)
    tot = freq[L]
    avg = L // 4
    minWsz = max(avg - tot['A'], 0) + max(avg - tot['C'], 0) + max(avg - tot['G'], 0) + max(avg - tot['T'], 0)
    R1 = range(L)
    R2 = range(minWsz, L+1)
    I = minWsz
    J = L
    ret = L
    while(True):
        wsz = (I+J) // 2
        print(I, J, wsz)
        if (I == J):
            break
        if (search(gene, avg, tot, L, freq, wsz, R1) != -1):
            ret = min(ret, wsz)
            J = wsz
        else:
            if(I == wsz):
                break
            I = wsz
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
