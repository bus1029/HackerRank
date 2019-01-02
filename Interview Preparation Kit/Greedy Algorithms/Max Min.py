#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxMin function below.
def maxMin(k, arr):
    # Minimize Unfairness
    # Unfairness: Max(subarr) - Min(subarr)
    # Subarr: k length of array in arr

    # 하지만 이렇게 하니까 Time Out이 발생함
    # Sorting에 nlogn이 걸리고
    # max, min 찾는데 n**2이 걸림 (17.12)
    """
    # 오름차순 정렬
    arr.sort()

    unfairness_list = []

    # 최대와 최소의 차가 가장 작은 Sub List를 구하기 위해
    # Window를 옮겨가면서 찾음
    for i in range(len(arr)-k+1):
        sub_arr = arr[i:i+k]
        unfairness_list.append(max(sub_arr) - min(sub_arr))

    return min(unfairness_list)
    """

    # max, min 쓰지말고
    # 이미 정렬되어 있기 때문에 가장 처음과 끝이 min과 max다.
    # 위 코드보다는 발전했지만, 3개의 Time out이 여전히 발생함 (27.34)
    # 왜냐하면, subarray를 만드는 과정에서도
    # 전체 List들 중에서 Subarray를 뽑을 떄 k만큼의 연산 비용이 들기 때문이다.
    """
    # 오름차순 정렬
    arr.sort()
    unfairness_list = []

    # 최대와 최소의 차가 가장 작은 Sub List를 구하기 위해
    # Window를 옮겨가면서 찾음
    for i in range(len(arr)-k+1):
        sub_arr = arr[i:i+k]
        unfairness_list.append(sub_arr[-1] - sub_arr[0])

    return min(unfairness_list)
    """

    # 오름차순 정렬
    # Subarray를 만들지 않고 한다면?
    arr.sort()
    # unfairness_list = []
    # 굳이 List를 사용하지 않고 정수 하나랑 비교해도 되겠다
    unfairness = float('inf')

    # 최대와 최소의 차가 가장 작은 Sub List를 구하기 위해
    # Window를 옮겨가면서 찾음
    for i in range(len(arr) - k + 1):
        # unfairness_list.append(arr[i+k-1] - arr[i])
        if unfairness > (arr[i + k - 1] - arr[i]):
            unfairness = arr[i + k - 1] - arr[i]

    return unfairness


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
