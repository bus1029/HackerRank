#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict, defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    # 키 값이 없더라도 에러를 출력하지 않고 기본값(int)을 출력한다.
    count_maps = defaultdict(int)

    # 왼쪽 Element들을 카운트해서 저장하고 있는 hashmap
    left_maps = defaultdict(int)

    triplets = 0

    # Making Count Hashmap
    for num in arr:
        try:
            count_maps[num] += 1
        except KeyError:
            count_maps[num] = 1

    # Remove Duplicates keep order
    removed_arr = list(OrderedDict.fromkeys(arr))

    # Array is made by only one number (1, 1, 1, 1, 1, 1, 1, ...)
    # nC2
    if len(removed_arr) == 1:
        triplets += (len(arr) * (len(arr) - 1) * (len(arr) - 2)) // 6

    # 단순히 숫자를 곱한다고 되는 문제가 아님
    # 아닌 경우 (e.g., 1 2 1 2 4)
    # 아닌 경우 (e.g., 1 4 2 1 2 4)
    else:
        # for num in arr:
        #     try:
        #         # 데이터 전체를 순차적으로 순회하면서
        #         # 사용된 숫자의 Count는 -1
        #         count_maps[num] -= 1
        #
        #         # Center, Right Number's Count in Hashmaps
        #         c_count = count_maps[num * r]
        #         r_count = count_maps[num * r * r]
        #
        #         triplets += c_count * r_count
        #
        #     # There is no Key in Hashmap
        #     except KeyError:
        #         # Triplet이 만들어지지 않았더라도
        #         # 사용되었다면 해당 숫자의 Count를 1 줄여준다.
        #         continue

        """
        Triplet의 첫 번째 Element부터 계산하는 것이 아니라,
        두 번째 Element를 기준으로 
        /r과 *r을 Count해서 계산하면
        """
        for num in arr:
            count_maps[num] -= 1
            triplets += left_maps[num/r] * count_maps[num*r]
            # 지나간 Element는 왼쪽 Count를 담당하는 Dictionary에 저장
            left_maps[num] += 1

    return triplets


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)

    # fptr.write(str(ans) + '\n')
    #
    # fptr.close()
