#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

num_swaps = 0
has_swapped = True
while has_swapped:
    has_swapped = False
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            has_swapped = True
            num_swaps += 1

print("Array is sorted in " + str(num_swaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))