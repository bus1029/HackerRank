#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    # Making Hash Table of arr
    count_dict = {}
    pairs = 0

    for num in arr:
        try:
            count_dict[num] += 1
        except KeyError:
            count_dict[num] = 1

    # 만들어놓은 HashTable을 순회하면서
    # k를 만들 수 있는 값이 있는지 확인
    for num, count in count_dict.items():
        if num < k:
            continue
        else:
            try:
                # k를 만들 수 있는 숫자가 존재하는 경우
                # count * 숫자 갯수 만큼 pair를 만들 수 있음
                if count_dict[num-k] > 0:
                    pairs += count * count_dict[num-k]
                else:
                    continue
            except KeyError:
                continue

    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
