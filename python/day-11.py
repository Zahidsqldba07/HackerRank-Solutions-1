#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -100;
    for x in range(len(arr)-2):
        for y in range(len(arr[x])-2):
            print(str(arr[x][y]) + " " + str(arr[x][y+1]) + " " + str(arr[x][y+2]))
            print(" " + " " + str(arr[x+1][y+1]) + " " + " ")
            print(str(arr[x+2][y]) + " " + str(arr[x+2][y+1]) + " " + str(arr[x+2][y+2]))
            
            sum = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            print("!!!" + str(sum))

            if (sum > max_sum):
                max_sum = sum
        print("-----------------------")
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
