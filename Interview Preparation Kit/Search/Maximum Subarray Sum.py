#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect, insort

# Complete the maximumSum function below.
def maximumSum(a, m):
    # Brute Force
    """
    max_modulo = 0

    # 원소가 하나일 경우에는 바로 찾을 수 있음

    for i in range(len(a)):
        if a[i] >= m:
            break
        else:
            max_modulo = max(max_modulo, a[i] % m)

    # 2개 이상일 경우
    for window in range(2, len(a)+1):
        prev_sum = sum(a[0:window])
        max_modulo = max(prev_sum % m, max_modulo)

        for i in range(1, len(a)+1-window):
            cur_sum = prev_sum - a[i-1] + a[i+1]
            max_modulo = max(max_modulo, cur_sum%m)
            prev_sum = cur_sum

    return max_modulo
    """

    # 또다른 Brute Force
    # Prefix Table을 이용하는 방법
    """
    prefix = []
    current = 0
    for i in range(len(a)):
        current = (a[i] % m + current) % m
        prefix.append(current)

    # SubarraySum(i, j) = (prefix[j] - prefix[i-1] + m) % m
    # e.g. 3, 3, 9, 9, 5
    # prefix[3] = (3 + 3 + 9 + 9) % 7 = 3
    # prefix[0] = 3 % 7 = 3
    # prefix[3]-prefix[0] = (3 - 3 + 7) % 7

    max_modulo = 0

    for i in range(0, len(a)):
        max_modulo = max(prefix[i], max_modulo)

        for j in range(i - 1, -1, -1):
            max_modulo = max(max_modulo, (prefix[i] - prefix[j] + m) % m)

    return max_modulo
    """


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        # fptr.write(str(result) + '\n')
    #
    # fptr.close()
