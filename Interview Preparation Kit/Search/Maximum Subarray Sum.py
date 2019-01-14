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

    prefix = []
    current = 0
    for i in range(len(a)):
        current = (a[i] % m + current) % m
        prefix.append(current)

    """
    max_modulo = 0

    for i in range(0, len(a)):
        max_modulo = max(prefix[i]%m, max_modulo)

        for j in range(i-1, -1, -1):
            max_modulo = max(max_modulo, (prefix[i]-prefix[j])%m)

    return max_modulo
    """

    # SubarraySum(i, j) = (prefix[j] - prefix[i-1] + m) % m
    # 여기서 +m을 해주는 이유는 prefix[j] - prefix[i-1]이 -가 나왔을 때
    # 계산을 쉽게 해주기 위해서 +를 하는 것이다.
    # 예를 들어, (2-4) mod 5 = -2 mod 5인데 이는 (-1 * 5) + r = -2이라서
    # r은 3이 된다. 하지만 이 계산을 쉽게 하려면
    # r =  -2 + (5 * 1)로 계산 할 수 있기 때문에 +m을 하는 것이다.
    # 예제에서는 *1 이상이 나올 수 있지만, 위 Code에서는 Prefix가 m보다 작은 수들로만 이루어져 있어서
    # 1이상은 나올 수가 없다. 그렇기 때문에 m만 더하는 것이다.

    # e.g. 3, 3, 9, 9, 5
    # prefix[3] = (3 + 3 + 9 + 9) % 7 = 3
    # prefix[0] = 3 % 7 = 3
    # prefix[3]-prefix[0] = (3 - 3 + 7) % 7

    # 여기서 SubarraySum이 큰 값을 가지려면
    # prefix[i-1]이 prefix[j]보다 크면서 큰 값 중 prefix[i-1]과 가장 가까운 수여야 한다.
    # 예를 들어 prefix[j]가 5라고 한다면 prefix[i-1]은 6이 되어야 SubarraySum(i, j)가 가장 큰 값이 된다.
    # 그래서 Binary Search Tree를 이용해서 해당 수와 가장 가까우면서도 큰 수를 찾는다.

    # 처음에 prefix[0]을 집어넣어주고
    bt = [prefix[0]]
    max_modular = max(prefix)

    for i in range(1, len(a)):
        # prefix[i]를 차례대로 Binary Search Tree에 집어넣으면서
        # 해당 값과 가장 가까우면서 큰 값을 고른다.
        # bt에 prefix[i] 를 넣었을 때의 Index를 리턴한다.
        # 이 때 실제 bt에는 prefix[i]가 없는 상태로 있기 때문에
        # 해당 Index에는 prefix[i]보다 가장 가까우면서 큰 값이 들어가있다.
        # e.g. bt = [3, 6], prefix[2] = 1
        # left = 0
        # left가 0이라는 의미는 bt에 1이 들어갔을 때의 Index인데,
        # 실제 bt[0]은 3이기 때문에 1과 가장 가까우면서 큰 값을 의미한다.
        left = bisect(bt, prefix[i])

        # 이 뜻은 left가 가장 큰 경우 pq의 Length와 같은 값이 나오기 때문에,
        # 이런 경우에는 pq에 해당 Index가 존재하지 않아서 Pass
        if left != len(bt):
            mod_sum = (prefix[i] - bt[left] + m) % m
            max_modular = max(mod_sum, max_modular)

        # 실제 Binary Search Tree에 prefix[i]를 집어넣고 다시 for문을 순회한다.
        insort(bt, prefix[i])

    return max_modular


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
