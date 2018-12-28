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
    주어진 배열에서 최댓값(최솟값)을 찾아 맨 오른쪽(왼쪽)값과 교체한다. 
    최댓값을 맨 오른쪽으로 보낸다는 점에서 버블정렬과 비슷하지만, 
    이웃한 두 값을 정렬하는 과정이 없기 때문에 대체로 버블정렬보다 빠르다.

    최댓값을 찾아야 하므로 정렬 상태와 관계없이 언제나 O(n**2)이다.
    """
    swap_count = 0

    # Using Selection Sort
    for end in reversed(range(len(a))): # len(a)-1부터 0까지
        max_i = 0

        for j in range(1, end+1):
            if a[j] > a[max_i]:
                max_i = j

        swap_count += 1
        a[end], a[max_i] = a[max_i], a[end]

    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    print("Array:", a)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
