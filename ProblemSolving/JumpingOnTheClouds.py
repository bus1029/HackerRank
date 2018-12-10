#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # c => array of clouds
    i = 0
    path_count = 0

    # 마지막에 도달하면 멈춤
    while i != len(c)-1:
        if i+2 <= len(c)-1 and c[i+2] == 0:
            i += 2
            path_count += 1
        else:
            i += 1
            path_count += 1

    return path_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
