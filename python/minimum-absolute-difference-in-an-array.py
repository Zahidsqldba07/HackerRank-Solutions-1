 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    mad = -1
    arr = sorted(arr)
    # for i in range(len(arr)):
    #     for j in range(i, len(arr)):
    #         print(str(i) + " " + str(j) + " " + str(abs(arr[i] - arr[j])) + " " + str(mad))
    #         if i != j and (mad == -1 or abs(arr[i] - arr[j]) < mad):
    #             mad = abs(arr[i] - arr[j])
    print(str(arr))
    for i in range(len(arr) - 1):
        if mad == -1 or arr[i+1] - arr[i] < mad:
                mad = arr[i+1] - arr[i]
    return mad

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
