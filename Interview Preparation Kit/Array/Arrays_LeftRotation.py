#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    # Input Format::
    # The first line contains two space-seperated integers n and d,
    # the size of a and the number of left rotations you must perform.
    # The second line contains n space-seperated integers a[i].

    # Output Format::
    # Print a single line of n space-separated integers denoting the final state of the array
    # after performing d left rotations.

    for i in range(d):
        val = a.pop(0)
        a.append(val)

    return a

    # Because 1 <= d <= n
    # Time Complexity == 1
    # 만약 d가 n보다 클 수 있었다면,
    # Modulo 연산을 통해서 계산했을 것 같다.
    # return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
