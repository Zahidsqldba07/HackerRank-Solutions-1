#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    leftTurns = 0
    rightTurns = 0

    if n % 2 == 0:
        n += 1

    for i in range(0, n, 2):
        if p > i+1:
            leftTurns+=1
        else:
            break

    for i in range(n, 0, -2):
        if p < i-1:
            rightTurns+=1
        else:
            break

    return min(leftTurns, rightTurns)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
