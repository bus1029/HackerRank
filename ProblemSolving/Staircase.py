#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    stair_str = ""

    for line in range(1, n + 1):
        for stair in range(0, n):
            stair_minus = n - stair

            if stair_minus > line:
                stair_str += " "
            else:
                stair_str += "#"

        stair_str += "\n"

    print(stair_str)


if __name__ == '__main__':
    n = int(input())

    staircase(n)
