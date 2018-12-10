#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0

    # Seok Hyun Solution
    # First, Sorting?
    # for i in range(0, len(arr)-1):
    #     for j in range(0, len(arr)-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]

    # Another Bubble Sort Solution
    # 이러면 이미 정렬된 끝 인덱스는 볼 필요가 없음
    # for size in reversed(range(len(arr))):
    #     for i in range(size):
    #         if arr[i] > arr[i+1]:
    #             arr[i], arr[i+1] = arr[i+1], arr[i]

    # Using Selection Sort
    # 주어진 배열에서 최댓값(최솟값)을 찾아 맨 오른쪽(왼쪽) 값과 교체한다.
    # 이웃한 두 값을 정렬하는 과정이 없기 때문에 대체로 버블정렬보다 빠르다.
    #     for size in reversed(range(len(arr))):
    #         max_i = 0

    #         for i in range(1, 1+size):
    #             if arr[i] > arr[max_i]:
    #                 max_i = i

    #         arr[max_i], arr[size] = arr[size], arr[max_i]

    # Selection Sort
    #     for size in reversed(range(arr)):
    #         max_i = 0
    #         for i in range(1, size+1):
    #             if arr[i] > arr[max_i]:
    #                 max_i = i
    #         arr[max_i], arr[size] = arr[size], arr[max_i]

    #     # Insertion Sort
    #     for size in (1, len(arr)):
    #         val = arr[size]
    #         i = size

    #         while i > 0 and arr[i-1] > val:
    #             arr[i] = arr[i-1]
    #             i -= 1

    #         arr[i] = val

    # Using Insertion Sort
    # 아직 정렬되지 않은 값을 이미 정렬된 배열 사이에 끼워 넣는 과정을 반복한다.
    # 평균적으로 삽입정렬이 선택정렬과 버블정렬에 비해 빠르다
    # 그러나, 데이터가 역순으로 정렬된 상태라면 삽입을 위해 값을 하나씩 뒤로 밀어내는 과정을 아주 많이
    # 반복해야되므로 느리다
    #     for size in range(1, len(arr)):
    #         val = arr[size]
    #         i = size

    #         while i > 0 and arr[i-1] > val:
    #             arr[i] = arr[i-1]
    #             i -= 1

    #         arr[i] = val

    # Using Merge Sort
    # n 만큼의 데이터 공간이 더 들지만, 최악의 경우에도 nlogn으로 가장 복잡도가 낮다
    # arr = merge_sort(arr)

    #     # Min Sum
    #     for k in range(0, len(arr)-1):
    #         min_sum += arr[k]

    #     # Max Sum
    #     for l in range(len(arr)-1, 0, -1):
    #         max_sum += arr[l]

    arr = itertools.combinations(arr, 4)
    arr = [sum(n) for n in arr]
    print("{} {}".format(min(arr), max(arr)))

    # Print
    # return print(str(min_sum) + " " + str(max_sum))


def merge_sort(x):
    if len(x) > 1:
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        lx = merge_sort(lx)
        rx = merge_sort(rx)

        li, ri, i = 0, 0, 0

        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1

            i += 1

        x[i:] = lx[li:] if li != len(lx) else rx[ri:]

    return x


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
