#!/bin/python3

import math
import os
import random
import re
import sys

def mergeSort(a):
    if len(a) > 1:
        mid = len(a) // 2
        lx, rx = a[:mid], a[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0

        while li < len(lx) and ri < len(rx):
            # 왼쪽 Array의 값이 오른쪽보다 작다면
            if lx[li] < rx[ri]:
                a[i] = lx[li]
                li += 1
            # 그 반대라면
            else:
                a[i] = rx[ri]
                ri += 1
            i += 1

        # 위 While문을 나왔다면, lx나 rx 둘 중 하나는 끝까지 도달
        # 도달하지 못한 Array를 x에 붙여줌
        a[i:] = lx[li:] if li != len(lx) else rx[ri:]

# Complete the countSwaps function below.
def countSwaps(a):
    """
    1. Number of swaps
    2. First Element
    3. Last Element
    """

    """
    폰 노이만이 개발했으며, 두 부분으로 쪼개는 작업을 재귀적으로 반복한 뒤,
    쪼갠 순서의 반대로 작은 값부터 병합해나가는 분할 정복 알고리즘의 일종이다.

    두 부분으로 쪼개는데 O(logn)이고, 데이터 병합이 O(n)이므로, 정렬 상태와
    무관하게 언제나 O(nlogn)이다. 데이터 크기만한 메모리가 더 필요한게 단점이다.
    """
    swap_count = 0

    # Using Shell Sort
    mergeSort(a)

    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    print("Array:", a)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
