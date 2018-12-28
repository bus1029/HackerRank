#!/bin/python3

import math
import os
import random
import re
import sys

def shellSort(a):
    # 항상 gap을 절반만큼 줄여나감
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap):
            gapInsertionSort(a, i, gap)

        # 최종적으로는 gap이 1이 될때까지 Insertion Sort 반복
        gap = gap // 2


def gapInsertionSort(a, start, gap):
    # gap 만큼 뛰어가면서 Sublist 내부에서 Insertion Sort 진행
    for i in range(start+gap, len(a), gap):
        val = a[i]
        position = i

        while position >= gap and a[position-gap] > val:
            a[position] = a[position-gap]
            position = position - gap

        a[position] = val

# Complete the countSwaps function below.
def countSwaps(a):
    """
    1. Number of swaps
    2. First Element
    3. Last Element
    """

    """
    삽입 정렬이 거의 정렬된 배열에서 최적의 성능을 냄과 동시에 값 하나씩 위치를 결정하여 비효율적이라는 점에서 착안.
    셸 정렬은 주어진 간격만큼 듬성듬성 떨어진 서브배열을 만들어 삽입정렬을 수행한다.
    모든 서브배열에 대한 삽입정렬을 마쳤다면, 간격을 (보통 절반으로) 줄여 반복한다. 간격이 1이 되면 거의 정렬된 
    상태이므로 빠르게 정렬할 수 있다.

    간격 정의에 따라 성능이 제각각이라 시간복잡도 분석이 쉽지 않다. 배열이 이미 정렬되어 있다면 O(n)이고,
    최악의 경우 아래 구현처럼 간격을 절반씩 줄인다면 O(n**1.5)이다. 
    다른 간격정의를 사용한다고 하더라도 현재까지 알려진 바로는 O(n**1.5)이 최선이다.
    """
    swap_count = 0

    # Using Shell Sort
    shellSort(a)

    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    print("Array:", a)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
