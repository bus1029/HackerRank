#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    cut_counts = []

    while len(arr) > 0:
        shortest = min(arr)
        cut_counts.append(len(arr))
        # 뺀 후, 0보다 큰 stick들을 모아서 arr에 다시 배정
        arr = [stick-shortest for stick in arr if stick-shortest > 0]

    return cut_counts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
