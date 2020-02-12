#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    p = 0
    if year>1918:
        p = 0
    elif year<1918:
        if year % 4 == 0 and year % 100 == 0:
            p = -1
    else:
        p = 13

    x = datetime.datetime(year, 1, 1) + datetime.timedelta(256-1 + p)
    return x.strftime("%d.%m.%Y")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
