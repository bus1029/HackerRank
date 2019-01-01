#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the abbreviation function below.
def abbreviation(a, b):
    # # 이건 다이나믹 프로그래밍이 아니다.
    # b_idx = 0
    #
    # for i in range(len(a)):
    #     if b_idx < len(b):
    #         if a[i].upper() == b[b_idx]:
    #             b_idx += 1
    #         else:
    #             if a[i].upper() != a[i]:
    #                 continue
    #             else:
    #                 return "NO"
    #     else:
    #         if a[i].upper() != a[i]:
    #             continue
    #         else:
    #             return "NO"
    #
    # if b_idx == len(b):
    #     return "YES"
    # else:
    #     return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
