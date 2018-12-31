#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
# Using Bubble Sort!

swap_count = 0

for i in range(len(a)):
    # 마지막에는 이미 정렬되어 있기 때문에 제외
    for j in range(len(a)-1-i):
        # 전 요소가 다음 요소보다 크다면
        if a[j] > a[j+1]:
            swap_count += 1
            # Swap
            a[j], a[j+1] = a[j+1], a[j]

print("Array is sorted in " + str(swap_count) + " swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])