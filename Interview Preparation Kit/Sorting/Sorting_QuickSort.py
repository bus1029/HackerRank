#!/bin/python3

import math
import os
import random
import re
import sys


def pivotFirst(a, lmark, rmark):
    # 처음엔 List의 첫번째 원소를 피벗으로 잡음
    pivot_val = a[lmark]
    pivot_idx = lmark

    # 두 마크가 서로 Cross되면 멈춤
    while lmark <= rmark:
        # lmark는 피벗보다 작거나 같으면 이동
        while lmark <= rmark and a[lmark] <= pivot_val:
            lmark += 1
        # rmark는 피벗보다 크거나 같으면 이동
        while lmark <= rmark and a[rmark] >= pivot_val:
            rmark -= 1

        # 크로스 되기 전까지는 서로의 마크가 멈춘 지점에서 값을 서로 바꿔줌
        # 바꿔줌으로써 최종적으로는 피벗의 오른쪽에는 피벗보다 큰 값이
        # 피벗의 왼쪽에는 피벗보다 작은 값이 오게 됨
        if lmark <= rmark:
            a[lmark], a[rmark] = a[rmark], a[lmark]
            lmark += 1
            rmark -= 1

    a[pivot_idx], a[rmark] = a[rmark], a[pivot_idx]

    return rmark


def quickSort(a, pivotMethod=pivotFirst):
    def _qsort(a, first, last):
        if first < last:
            split_point = pivotMethod(a, first, last)
            _qsort(a, first, split_point - 1)
            _qsort(a, split_point + 1, last)

    _qsort(a, 0, len(a) - 1)


# Complete the countSwaps function below.
def countSwaps(a):
    """
    1. Number of swaps
    2. First Element
    3. Last Element
    """

    """
    피벗(Pivot, 기준값) 원소를 정하여 피벗보다 작은 값은 피벗 앞 쪽에, 큰 값은 피벗 뒤 쪽에
    오도록 한다. 피벗 양쪽 배열에 대해 같은 작업을 반복해 나간다. 
    분할 정복 방법의 일종이며, 재귀 호출이 진행될 때마다 최소한 하나의 원소(피벗)는 최종적으로 위치가 정해진다.
    병합정렬은 데이터를 쪼갠 뒤 합치는 과정에서 정렬하지만, 퀵 정렬은 데이터를 쪼개면서 정렬한다. 

    데이터를 절반씩 쪼갠다면 O(log n)이고, n개의 값을 피봇과 비교하므로 O(n log n)이다. 
    피봇 선정 기준에 따라 쪼개는 위치가 한 쪽에 치우져 있을 수도 있다. (예: 데이터가 이미 정렬되어 있고,
    맨 끝 원소를 피봇으로 선정하는 경우). 이 때는 쪼개는 비용이 O(n)이므로 퀵정렬의 시간복잡도가 O(n**2)까지 증가한다.
    재귀 호출을 위한 스택을 사용하므로 추가 메모리가 필요하다.

    퀵 정렬은 병합 정렬과 달리 데이터를 복제할 필요가 없는 in-place 알고리즘이다. 
    하지만, 퀵 정렬의 파이썬 구현을 인터넷에 검색해보면 데이터를 복제하여 O(n)의 추가 메모리를 사용하는 방식으로 
    구현한 코드가 많다. 이렇게 구현하면 추가 메모리를 사용하긴 하지만 실행속도가 빨라지며, Stable한 퀵 정렬이 된다.

    파이썬은 퀵정렬을 하지 않는다. 그 이유는 파이썬은 stable한 정렬을 하는데, 퀵정렬은 stable하지 않기 때문이다. 
    예를 들어 한글의 키값이 2, 숫자의 키값이 1이라 두면 1, ㄱ , ㄷ, ㄹ, 2를 퀵정렬해서 2, 1, ㄹ, ㄱ, ㄷ 같은 게 나올 수도 있다. 
    O(n)의 추가 메모리를 이용하면 stable한 퀵정렬을 만들 수 있다.

    """
    swap_count = 0

    # Using Shell Sort
    quickSort(a)

    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    print("Array:", a)


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
