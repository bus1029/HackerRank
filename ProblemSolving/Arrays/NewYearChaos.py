#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    brided = False
    count = 0

    # Check Too Chaotic
    # 본인 위치에서 2칸 이상 움직일 수 없는데, 움직인 경우에는 Too Chaotic
    for n, v in enumerate(q):
        if (v - 1) - n > 2:
            return print("Too chaotic")

    # Check the swap count
    # Bubble Sort...
    for i in range(0, len(q) - 1):
        for j in range(0, len(q) - 1):
            # Check Last Index
            if q[j] > q[j + 1]:
                count += 1
                q[j + 1], q[j] = q[j], q[j + 1]
                brided = True

        if brided:
            brided = False
        else:
            break

    print(count)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
