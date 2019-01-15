#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    # i <= days <= j
    # k = divisor
    b_days = 0

    # for number in range(i, j+1):
    #     rvsed_number = int(str(number)[::-1])
    #     if abs(number - rvsed_number) % k == 0:
    #         b_days += 1


    # or
    b_days = [1 for number in range(i, j+1) if abs(number - int(str(number)[::-1])) % k == 0]

    return sum(b_days)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
