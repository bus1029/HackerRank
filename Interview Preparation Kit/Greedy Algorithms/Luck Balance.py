#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    i_contests = []
    luck = 0

    # 중요한 Contest의 Luck만 추출한 후
    for contest in contests:
        if contest[1] == 1:
            i_contests.append(contest[0])

    # 내림차순으로 정렬한 후
    i_contests.sort(reverse=True)

    # 가장 높은 Luck을 가진 Contest들만 k번 지고
    # 나머지 Contest들은 모두 이기면
    luck += sum(i_contests[:k])
    luck -= sum(i_contests[k:])

    # 나머지 중요하지 않은 Contest들은 지면 됨
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]

    return luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
