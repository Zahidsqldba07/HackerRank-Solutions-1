# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from itertools import product

data = sys.stdin.readlines()
if (len(data) == 2):
    A = list(map(int, data[0].split()))
    B = list(map(int, data[1].split()))

    # print("A: " + str(A))
    # print("B: " + str(B))

    # print(str(list(product(A, B)))[1:-1])
    for item in product(A, B):
        print(str(item), end=' ')
