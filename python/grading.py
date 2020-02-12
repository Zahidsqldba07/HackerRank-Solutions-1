#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def calculateFinalGrade(grade):
    finalGrade = grade
    if grade % 5 >= 3 and grade >=38:
        finalGrade = 5 * ((grade // 5) + 1)
    return finalGrade

def gradingStudents(grades):
    finals = []
    for item in grades:
        finals.append(calculateFinalGrade(item))
    return finals

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
