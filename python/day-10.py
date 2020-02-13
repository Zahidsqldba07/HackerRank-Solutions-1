#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    
    nb = "{0:b}".format(n)
    
    p = 0
    max = 0
    ones = 0
    
    for i in nb:
        if i == '1':
            ones += 1
        else:
            ones = 0
        if ones > max:
            max = ones
        p = i
       # print(str(ones))
        
    print(str(max))
    
    