#!/bin/python3

import math
import os
import random
import re
import sys

def print_n(n, i):
    print(str(n) + " x " + str(i) + " = " + str(n*i))

if __name__ == '__main__':
    n = int(input())
    for i in range(10):
        print_n(n, i+1)
