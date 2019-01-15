#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Real distance of apple and orange
    apples = [apple + a for apple in apples]
    oranges = [orange + b for orange in oranges]

    a_count, o_count = 0, 0

    for apple in apples:
        if s <= apple <= t:
            a_count += 1
    for orange in oranges:
        if s <= orange <= t:
            o_count += 1

    print(a_count)
    print(o_count)

    # Another solution
    # print(sum([1 for apple in apples if (apple + a) >= s and (apple + a) <= t]))
    # print(sum([1 for orange in oranges if (orange + b) >= s and (orange + b) <= t]))


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
