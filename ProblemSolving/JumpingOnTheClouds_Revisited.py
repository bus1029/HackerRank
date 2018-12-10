#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    # c => an array of clouds
    # k => jumping hops
    total_energy = 100

    # 처음으로 되돌아 올 수 있는 가장 작은 수를 구함(최소공배수)
    start_point = lcm(len(c), k)

    # 처음으로 돌아올 때까지 k씩 더해줌
    for i in range(k, start_point + 1, k):
        cloud_index = i % len(c)
        consumption = 1 if c[cloud_index] == 0 else 3
        total_energy -= consumption

    # Easy Solution
    # start_point = 0

    # while True:
    #     start_point = (start_point + k) % len(c)
    #     consumption = 1 if c[start_point] == 0 else 3
    #     total_energy -= consumption

    #     if start_point == 0:
    #         break

    return total_energy


def gcd(n, m):
    if n < m:
        n, m = m, n
    while m != 0:
        n, m = m, n % m
    return n


def lcm(n, m):
    return n * m // gcd(n, m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
