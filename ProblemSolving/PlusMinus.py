#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    plus_count = 0
    zero_count = 0
    minus_count = 0
    total_count = 0

    # Check count of each number
    for number in arr:
        if number > 0:
            plus_count += 1
        elif number < 0:
            minus_count += 1
        else:
            zero_count += 1

    total_count = plus_count + zero_count + minus_count

    print(round(plus_count / total_count, 6))
    print(round(minus_count / total_count, 6))
    print(round(zero_count / total_count, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
