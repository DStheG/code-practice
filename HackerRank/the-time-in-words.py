#!/bin/python3

import math
import os
import random
import re
import sys


def getMin(m):
  M = (
        "zero", 
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine")
  mm = (None, "quarter", "half")
  if(m % 15):
    return M[m] + ' minute' + ('s' if m > 1 else '')
  else:
    return mm[int(m/15)]

# Complete the timeInWords function below.
def timeInWords(h, m):
  H = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve')

  ret = ''
  if m == 0:
    ret = "%s o' clock" % (H[h])
  elif m > 30:
    ret = "%s to %s" % (getMin(60-m), H[h+1])
  else:
    ret = "%s past %s" % (getMin(m), H[h])

  return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
