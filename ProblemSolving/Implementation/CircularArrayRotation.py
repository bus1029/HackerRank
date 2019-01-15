#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    # a => array of integers to rotate
    # k => the rotation count
    # queries => the indices to report

    # Rotation을 돌 때, 제일 마지막껄 빼서 처음으로 넣어줌
    for i in range(k):
        last_number = a.pop()
        a.insert(0, last_number)

    result = [a[query] for query in queries]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
