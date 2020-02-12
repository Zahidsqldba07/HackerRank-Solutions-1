#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    calc = {}

    minId = -1
    maxId = -1
    maxCounter = -1

    for item in arr:
        if calc.__contains__(item):
            calc[item] = calc[item]+1
        else:
            calc[item] = 1

    for key in calc.keys():
        if minId==-1 or key<minId:
            minId = key
        if calc[key] > maxCounter:
            maxCounter = calc[key]
            maxId = key
        elif calc[key] == maxCounter and key < maxId:
            maxId = key

    return maxId

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
