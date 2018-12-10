#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    # k => Divisor
    # subsets = list(set(itertools.combinations(S, 2)))

    # reversed(range(len(S)) => len(S)-1부터 0까지 반복
    # 이렇게 하면 시간 제한에 걸릴 수 밖에 없음

    # for i in reversed(range(len(S)+1)):
    #     subsets = list(set(itertools.combinations(S, i)))

    #     for subset in subsets:
    #         flag = True

    #         subset_two = list(set(itertools.combinations(subset, 2)))

    #         for (a, b) in subset_two:
    #             if (a+b) % k == 0:
    #                 flag = False
    #                 break

    #         if flag is True:
    #             print(len(subset))
    #             return len(subset)

    # 다른 방식은 a%k + b%k = k가 안되는 조합을 찾으면 된다.
    # 특별하게 0 + 0은 k로 나뉘어진다.
    # e.g. k = 5면 (1, 4), (2, 3)만 아니면 된다.
    remain_count = [0 for i in range(k)]

    for num in S:
        remain_count[num % k] += 1

    print(remain_count)
    # 무조건 0이 하나 들어가던지, 안들어가던지
    count = min(remain_count[0], 1)

    # k = 6인 경우
    # (1, 5) (2, 4) (3)
    # (1, 5) 중에서 큰거 고르고
    # (2, 4) 중에서 큰거 고르고
    # 3은 하나만 넣어주고

    # 홀수인 경우에는
    # k = 7
    # (1, 6) (2, 5) (3, 4)
    # 이런 경우에는 하나만 있는 경우를 배제해도 됨
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(remain_count[i], remain_count[k - i])
    if k % 2 == 0:
        count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
