#!/bin/python3
     
import math
import os
import random
import re
import sys
import itertools

# Complete the birthday function below.
def birthday(s, d, m):
    result = 0
    sums = []
    sums.append(0)
    for i in range(0, len(s)):
        sums.append(sums[i] + s[i])
    for i in range(0, len(s)-m+1):
        if sums[i+m]-sums[i] == d:
            result+=1
    return result

    # solutions = []

    # squares = s.copy()
    # squares.sort()

    # combinations = itertools.product(squares, repeat=m)
    # selected = []
    
    # print("start elements " + str(len(squares)) + ": " + str(squares))
    # calculateCombinations(combinations, selected, squares)                
    # print("selected final " + str(selected) + " left elements " + str(len(squares)) + ": " + str(squares))

    # return len(selected)

def calculateCombinations(combinations, selected, squares):
    # print("combinations " + str(combinations))
    # for i in range(len(combinations)-1, -1, -1):
        # print("index of combination " + str(i) + " from " + str(len(combinations)))
        # combination = combinations[i]
    for combination in combinations:
        # print("elements of combination " + str(combination))
        # print("sum of combination " + str(sum(combination)))
        if sum(combination) == d and len(squares) >= m:
            selected.append(combination)       
            for item in combination:
                # print("remove item " + str(item) + " from " + str(combination))
                if squares.count(item) > 0:
                    squares.remove(item)     
            combinations = itertools.product(squares, repeat=m)
            print("selected " + str(selected) + " left elements " + str(len(squares)) + ": " + str(squares))
            calculateCombinations(combinations, selected, squares)
            break

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
