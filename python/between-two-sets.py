#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    maxA = max(a)
    minB = min(b)
    considered = []
    final = []
    for item in range(maxA, minB+1):
        appendItem = True
        for elemA in a:
            if item % elemA != 0:
                appendItem = False
                break
        if appendItem:
            considered.append(item)

    for item in considered:
        appendItem = True
        for elemB in b:
            if elemB % item != 0:
                appendItem = False
                break
        if appendItem:
            final.append(item)

    print("considered " + str(considered))
    print("final " + str(final))
    return len(final)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
