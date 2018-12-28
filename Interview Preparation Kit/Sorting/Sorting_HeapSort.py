#!/bin/python3

import math
import os
import random
import re
import sys

def heapify(a, index, heap_size):
    largest = index # Initialize largest as root
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    # 왼쪽 자식이 존재하고, 루트보다 크면
    if left_index < heap_size and a[left_index] > a[largest]:
        largest = left_index

    # 오른쪽 자식이 존재하고, 루트보다 크면
    if right_index < heap_size and a[right_index] > a[largest]:
        largest = right_index

    # 루트의 인덱스가 바꼈다면
    if largest != index:
        a[largest], a[index] = a[index], a[largest]
        # 바뀐 자식 노드에서 다시 heapify 실행
        heapify(a, largest, heap_size)


def heapSort(a):
    n = len(a)
    # 최초 힙 구성시 리스트의 중간부터 시작하면
    # 이진트리의 성질에 의해 모든 요소값을
    # 서로 한번씩 비교할 수 있게 됨: O(n)
    for i in range(n // 2, -1, -1):
        heapify(a, i, n)

    # 힙이 구성되면, 최악의 경우에도 트리의 높이(log n) 만큼의 자리 이동을 하게 됨
    # 이런 노드들이 n개 있으므로 O(nlogn)
    for i in range(n-1, 0, -1):
        # 루트가 가장 큰 값을 가지기 때문에
        a[0], a[i] = a[i], a[0]
        heapify(a, 0, i) # 마지막 값 빼고 다시 Heap 구성

    return a


# Complete the countSwaps function below.
def countSwaps(a):
    """
    1. Number of swaps
    2. First Element
    3. Last Element
    """

    """
    Heap은 큰 키(우선 순위)에 자주 액세스하거나 키(우선 순위) 중심으로 정렬된 시퀀스를 활용해야 할 때
    유용한 자료구조입니다. 힙은 한 노드가 최대 두 개의 자식노드를 가지면서, 마지막 레벨을 제외한
    모든 레벨에서 노드들이 꽉 채워진 완전이진트리를 기본으로 합니다.

    Heapify: 주어진 자료구조에서 힙 성질을 만족하도록 하는 연산 (O(log n))
    부모노드는 자식노드들보다 큰 값을 가져야 한다. (Max Heap)
    부모노드는 자식노드들보다 작은 값을 가져야 한다. (Min Heap)
    
    힙 정렬의 수행 방법은 다음과 같다.
    1. 주어진 원소들로 최대힙을 구성한다.
    2. 최대 힙의 루트노드와 말단노드를 교환해준다.
    3. 새 로트노드에 대해 최대 힙을 구성한다.
    4. 원소의 개수만큼 2, 3을 반복 수행한다.
    """
    swap_count = 0

    # Using Shell Sort
    a = heapSort(a)

    print("Array is sorted in " + str(swap_count) + " swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    print("Array:", a)

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
