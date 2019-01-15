#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    # 최소, 최대 갱신 횟수 구하기
    min_count, max_count = 0, 0
    min_score, max_score = -1, -1

    for score in scores:
        # 처음엔 무시
        if min_score == -1 and max_score == -1:
            min_score, max_score = score, score

        # Check Min
        elif min_score > score:
            min_score = score
            min_count += 1

        # Check Max
        elif score > max_score:
            max_score = score
            max_count += 1

    return max_count, min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
