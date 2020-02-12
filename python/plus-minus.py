#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    n = 0
    z = 0

    for item in arr:
        if item>0:
            p+=1
        elif item<0:
            n+=1
        else:
            z+=1

    print("{0:.6f}".format(p/len(arr)))
    print("{0:.6f}".format(n/len(arr)))
    print("{0:.6f}".format(z/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
