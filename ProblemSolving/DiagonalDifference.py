#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    left_total = 0
    right_total = 0

    diagonal_count = 0
    reverse_d_count = len(arr) - 1

    # left & right diagonal
    for arr_line in arr:
        left_total += arr_line[diagonal_count]
        right_total += arr_line[reverse_d_count]
        diagonal_count += 1
        reverse_d_count -= 1

    return abs(left_total - right_total)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
