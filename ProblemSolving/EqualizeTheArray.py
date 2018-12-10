#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the equalizeArray function below.
def equalizeArray(arr):
    counter = Counter(arr)
    # Get Max Digit Count
    max_digit_count = arr.count(max(arr, key=counter.get))

    return len(arr) - max_digit_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
