#!/bin/python3

import math
import os
import random
import re
import sys
from difflib import SequenceMatcher

CHARS = 26

# Complete the makeAnagram function below.
def makeAnagram(str1, str2):
    # make hash array for both string  
    # and calculate 
    # frequency of each character 
    count1 = [0]*CHARS 
    count2 = [0]*CHARS 
  
    # count frequency of each character  
    # in first string 
    i = 0
    while i < len(str1): 
        count1[ord(str1[i])-ord('a')] += 1
        i += 1
  
    # count frequency of each character  
    # in second string 
    i =0
    while i < len(str2): 
        count2[ord(str2[i])-ord('a')] += 1
        i += 1
  
    # traverse count arrays to find  
    # number of characters 
    # to be removed 
    result = 0
    for i in range(26): 
        result += abs(count1[i] - count2[i]) 
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
