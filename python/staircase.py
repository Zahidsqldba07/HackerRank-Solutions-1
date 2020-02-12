#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for l in range(n-i-1):
            print(" ", end="")
        for c in range(i+1):
            print("#", end="")
        print("")

if __name__ == '__main__':
    n = int(input())

    staircase(n)
