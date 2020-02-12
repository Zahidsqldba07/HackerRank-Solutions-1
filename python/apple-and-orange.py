#!/bin/python3

import math
import os
import random
import re
import sys

def numberOfFruitsInHouse(treePoint, housePointStart, housePointEnd, fruits):
    numberOfFruitsInHouse = 0
    for fruitDistance in fruits:
        if treePoint+fruitDistance >= housePointStart and treePoint+fruitDistance <= housePointEnd:
            numberOfFruitsInHouse+=1
    return numberOfFruitsInHouse

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    houseApples = numberOfFruitsInHouse(a, s, t, apples)
    houseOranges = numberOfFruitsInHouse(b, s, t, oranges)
    print(str(houseApples))
    print(str(houseOranges))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
