#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):
    # 난 처음에 문제를 잘못 파악해서
    # 왼쪽에 있는 아이와만 비교를 진행한 후, dp를 채워나가기 시작했다.
    # 하지만, 문제를 자세히 읽어보니 adjacent라는 의미는 양쪽을 다 비교해서
    # 알맞은 캔디를 지급해야 한다는 것을 알았다.
    #    [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]에서
    # -> [1, 2, 1, 2, 1, 2, 3, 4, 2, 1]
    # 9는 8과 2중 가장 크기 때문에 8보다 1개 많은 4개의 캔디를 받았고
    # 9 다음의 2는 9, 2, 1 중에서 2번째로 크지만
    # 1이 가장 작은 수이기 때문에 1보다 한개 많은 캔디인 2개를 받았다.

    """
    # 본인의 성적이 왼쪽에 있는 아이보다 크다면
    # 왼쪽이 받은 캔디의 +1개를 받는다
    # 아니라면, 1개의 캔디를 받는다.

    dp = [0] * len(arr)
    dp[0] = 1 # 처음 애는 무조건 1개로 시작
    dp[1] = dp[0]+1 if arr[1] > arr[0] else 1 # 두 번째애는 첫 번째애와 비교해서

    # 끝까지 순회하는데
    for i in range(2, len(arr)):
        # 왼쪽애보다 성적이 좋다면
        if arr[i] > arr[i-1]:
            # 왼쪽애가 가지고 있는 캔디 + 1개
            dp[i] = dp[i-1] + 1
        else:
            # 작아졌다면 전 애와, 전전 애의 캔디 수 중에 최소값에 -1 한 캔디를 받는다.
            # 이 때, 캔디의 수는 1개 보다 작아지면 안되기 때문에 1과 max 비교를 한다
            dp[i] = max(min(dp[i-1], dp[i-2])-1, 1)

    return sum(dp)
    """

    # 왼쪽에서 오른쪽으로 가는 상향 패턴의 캔디를 기록하고
    # 오른쪽에서 왼쪽으로 가는 하향 패턴의 캔디를 기록해서
    # 두 리스트의 원소들 중 각각 큰 원소들을 선택하면
    # 양쪽을 다 비교해서 받을 수 있는 캔디를 결정할 수 있다.

    dp_l = [1] * len(arr)
    dp_r = [1] * len(arr)

    # Left to Right
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            dp_l[i] = dp_l[i - 1] + 1

    # Right to Left
    for j in range(len(arr) - 2, -1, -1):
        if arr[j] > arr[j + 1]:
            dp_r[j] = dp_r[j + 1] + 1

    dp_max = [max(l, r) for l, r in zip(dp_l, dp_r)]

    return sum(dp_max)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
