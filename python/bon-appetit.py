#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    result = "Bon Appetit"

    eaten = bill.copy()
    eaten.remove(eaten[k])

    annaSum = sum(eaten) / 2
    billSum = sum(bill) / 2

    if (annaSum != b):
        print(int(b-annaSum))
    else:
        print(result)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
