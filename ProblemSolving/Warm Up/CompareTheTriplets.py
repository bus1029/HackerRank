#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_score, bob_score = 0, 0

    for a_n, b_n in zip(a, b):
        if a_n > b_n: alice_score += 1
        elif a_n < b_n: bob_score += 1
        else: continue

    return alice_score, bob_score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
