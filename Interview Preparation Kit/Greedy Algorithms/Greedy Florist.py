#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # k: number of friends
    # c: cost of flowers
    cost = 0
    persons = [0] * k
    # 오름차순으로 꽃 값을 정렬
    c.sort(reverse=True)

    # 최소한의 비용으로 모든 꽃을 사려면
    # 가장 높은 가격을 가진 꽃을 가장 적은 배수로 구입해야 한다.
    # Time Complexity는 k가 1인 경우 O(n) (최악)
    while len(c) > 0:
        for i in range(k):
            try:
                cost += c[i] * (persons[i] + 1)
                persons[i] += 1
            except IndexError:
                # Cost List에 대해서 Index Error가 뜰 수 있음
                # 떴다는 의미는 더 이상 살 꽃이 남지 않았다는 뜻이므로
                break

        # 구매된 꽃은 제외
        c = c[k:]

    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
