#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # Input Format::
    # The first line contains an integer n, the size of arr.
    # The second line contains n space-separated integers arr[i].

    # Constraints
    # 1 <= n <= pow(10, 5)
    # 1 <= arr[i] <= n
    swap = 0

    # length = len(arr)

    # 주의! .index를 쓰는 과정에서 Timeout이 발생

    # for i in range(length//2):
    #     index = arr.index(i+1)
    #     if i != index:
    #         swap += 1
    #         arr[i], arr[index] = arr[index], arr[i]
    #
    #     index = arr.index(length-i)
    #     if length-1-i != index:
    #         swap += 1
    #         arr[length-1-i], arr[index] = arr[index], arr[length-1-i]

    # .index를 쓰지 않고, 직접 array에 접근해서 해결
    # 각 숫자들이 원래 있어야 할 위치로 옮겨짐
    # 여기서 포인트는 바꿔진 위치에서 다시 한번 실행한다는 점
    i = 0
    while i < len(arr):
        if arr[i] == arr[arr[i]-1]:
            i += 1
            continue

        elif arr[i] != arr[arr[i]-1]:
            swap += 1
            # temp = arr[i]
            # arr[i] = arr[arr[i]-1]
            # arr[temp-1] = temp

            # 위 식과 같은 식
            # 여기서 arr[arr[i]-1]과 arr[i]의 순서가 바뀌면 안되는데
            # 순서가 바뀌면 arr[i]에 다른 숫자가 먼저 들어가고
            # 그 뒤에 arr[arr[i]-1]에 적용되기 때문에 의도치 않게 숫자가 바뀌게 된다.
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]

    return swap


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
