#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0

    # 함정에 빠진거네...
    # 1~5 사이의 수가 중복되서 초콜릿 바에 나올 수 있는데
    # 처음부터 차례대로 해도 어짜피 같은 수가 나오기 때문에
    # 상관없는 거였다
    for i in range(len(s)+1-m):
        if sum(s[i:i+m]) == d:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
