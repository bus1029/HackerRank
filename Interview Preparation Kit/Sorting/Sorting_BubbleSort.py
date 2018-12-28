#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    """
    for i in range(len(a)):
        for j in range(i, len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    Given an array if integers, sort the array in ascending order using Bubble Sort Algorithm above.
    Once sorted, print the following three lines:

    1. Number of swaps
    2. First Element
    3. Last Element
    """

    """
    이웃한 두 값을 비교하여 정렬한다. 큰 값이 오른쪽으로 이동하는 과정이 반복되면서
    비교했던 모든 값들의 최대값이 맨 오른쪽으로 옮겨지게 된다.
    
    최악의 경우 (n−1)+(n−2)+⋯+1번 비교가 이루어지므로 O(n**2)이다. 
    그러나, 데이터가 잘 졍렬돼있다면 O(n)이므로 데이터의 정렬 여부를 파악하기 위한 
    알고리즘으로 사용될 수 있다. 
    """
    swap_count = 0

    # Using Bubble Sort
    # 큰 숫자가 마치 거품이 올라가는 것처럼 뒤쪽으로 올라가서 Bubble Sort...!
    for i in range(len(a)):
        # 마지막은 이미 정렬되어 있으니까, 마지막까진 갈 필요가 없다
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                swap_count += 1
                a[j], a[j+1] = a[j+1], a[j]

    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
