#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):
    if n > 1:
        prime = True
    else:
        prime = False

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            prime = False
            break

    if prime:
        return "Prime"
    else:
        return "Not prime"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
