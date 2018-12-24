#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hour_glass_results = []

    # 한번에 읽을 수 있는 Glass는 현재 Line에서 +2

    for i in range(0, len(arr)-2):
        for j in range(0, len(arr)-2):
            first_hour_glass = sum(arr[i][j:j+3])
            second_hour_glass = arr[i+1][j+1]
            third_hour_glass = sum(arr[i+2][j:j+3])

            hour_glass_results.append(first_hour_glass + second_hour_glass + third_hour_glass)

    return max(hour_glass_results)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
