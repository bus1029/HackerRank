#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    # n => number of prisoners
    # m => number of candies
    # s => start number of prisoner

    # Candy가 몇바퀴 돈 후 남은 갯수
    remain_candy = m % n
    # 출발 죄수번호로부터 몇개까지 나눠줄 수 있는가?
    # 본인 포함이기 때문에 1을 뺌
    start_from_index = (s + remain_candy - 1) % n

    # 딱 맞아 떨어졌다는건 마지막까지 갔다는 의미
    return n if start_from_index == 0 else start_from_index


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
