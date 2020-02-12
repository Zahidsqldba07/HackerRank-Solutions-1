 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    completed = 0
    pairs = set()
    for socket in ar:
        if socket in pairs:
            completed += 1
            pairs.remove(socket)
        else:
            pairs.add(socket)
    return completed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
