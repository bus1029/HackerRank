#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level = 0
    valley_count = 0
    mountain, valley = False, False

    for step in s:
        if step == "U":
            sea_level += 1

        elif step == "D":
            sea_level -= 1

        if sea_level < 0:
            valley = True
            mountain = False
        elif sea_level > 0:
            mountain = True
            valley = False
        elif sea_level == 0:
            if valley:
                valley_count += 1
                valley = False
            elif mountain:
                mountain = False

    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
