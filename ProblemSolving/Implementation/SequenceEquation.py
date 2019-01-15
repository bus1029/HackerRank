#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    # p => an array of integers
    result = []

    for i in range(1, len(p)+1):
        # Index가 위치한 숫자값을 받아옴
        p_i = p.index(i) + 1
        # 숫자값의 Index를 숫자값으로 변환
        result.append(p.index(p_i) + 1)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
