#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    # n = days of advertising
    cumulatives = 0
    shared = 5

    for day in range(1, n+1):
        cumulatives += math.floor(shared / 2)
        shared = math.floor(shared / 2) * 3

    return cumulatives

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
