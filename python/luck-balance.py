 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    balance = 0
    importantList = []

    for contest in contests:
        if contest[1] == 1:
            importantList.append(contest[0])
        else:
            balance += contest[0]

    importantList.sort(reverse=True)
    for importantLost in range(k):
        if importantLost < len(importantList):
            balance += importantList[importantLost]
    for importantWin in range(k, len(importantList)):
        if importantWin < len(importantList):
            balance -= importantList[importantWin]

    return balance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
