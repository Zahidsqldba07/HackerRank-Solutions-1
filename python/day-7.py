#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    rev = list(reversed(arr))
    
    for a in rev:
        print(str(a) + " ", end='')
