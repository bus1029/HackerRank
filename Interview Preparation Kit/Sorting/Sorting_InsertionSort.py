#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    """
    1. Number of swaps
    2. First Element
    3. Last Element
    """

    """
    아직 정렬되지 않은 값을 이미 정렬한 배열 사이에 끼워 넣는 과정을 반복한다.
    여전히 O(n**2)이지만 평균적으로 삽입정렬이 선택정렬과 버블정렬에 비해 빠르다.

    버블정렬과 마찬가지로 데이터가 이미 정렬되어 있다면 O(n)이다. 그러나, 데이터가 역순으로
    정렬된 상태라면 삽입을 위해 값을 하나씩 뒤로 밀어내는 과정을 아주 많이 반복해야 하므로 느리다.
    """
    swap_count = 0

    # Using Insertion Sort
    for size in range(1, len(a)):
        val = a[size]
        i = size

        # 현재 값과 비교해서 전 값이 현재 값보다 크면
        # 전 Index의 값을 현재 Index에 넣음
        while i > 0 and a[i-1] > val:
            a[i] = a[i-1] # 비워주는 과정
            i -= 1

        # 현재 값이 전 Index의 값보다 크면,
        # 전 Index 자리에 현재 값을 Insert
        a[i] = val # Insert

    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    print("Array:", a)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
