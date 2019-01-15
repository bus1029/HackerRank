#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    # k = threshold
    # a = arrive times
    arrived_num = 0

    for a_time in a:
        if a_time <= 0:
            arrived_num += 1

    return "YES" if arrived_num < k else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
