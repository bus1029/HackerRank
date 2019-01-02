#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    # 일단 Brute Force로 해보자

    # 정답이 아닌 경우가 발생
    """
    combs = list(set(combinations(arr, 2)))
    result_list = [abs(a-b) for (a, b) in combs]

    return min(result_list)
    """

    # 정렬한 후, Window Size를 2로 지정해서 모든 값들을 구한 다음에 최소 값을 구한다면?
    # 왜냐하면, 가장 작은 차이를 보이려면 값이 인접한 두 수를 이용하면 되기 때문이다.
    arr_sorted = sorted(arr)
    result_list = []

    for i in range(len(arr) - 1):
        result_list.append(abs(arr_sorted[i] - arr_sorted[i + 1]))

    return min(result_list)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
