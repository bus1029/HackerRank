#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    # sorted()는 값을 Return (모든 Iterable한 자료구조에 사용 가능)
    # list.sort()는 값을 Return 하지 않고 List내에서 정렬

    # 함수 f와 반복가능 자료구조
    # map(f, iterable)

    # Toy를 가격순으로 정렬한 후 이용
    prices = sorted(prices)
    toy = 0

    for price in prices:
        if k-price > 0:
            k -= price
            toy += 1
        # -가 나온다면 더 이상 돌 필요가 없음
        else:
            break

    return toy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
