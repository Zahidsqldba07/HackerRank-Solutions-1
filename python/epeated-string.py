#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    acounter = 0
    for c in range(len(s)):
            if s[c] == 'a':
                acounter += 1

    acounter = math.floor(n/len(s))*acounter

    g = math.floor(n/len(s)) * len(s)
    for c in range(len(s)):
        if g < n and s[c] == 'a':
            acounter += 1
        g += 1

    # g = 0
    # while g <= n:
    #     for c in range(len(s)):
    #         if g+c <= n and s[c] == 'a':
    #             acounter += 1
    #         g += 1

    return acounter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
