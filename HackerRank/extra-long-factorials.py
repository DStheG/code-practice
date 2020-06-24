#!/bin/python3

import math
import os
import random
import re
import sys

def fact(n):
  if(n == 1):
    return 1
  return fact(n-1)*n

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
  print(fact(n))

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
