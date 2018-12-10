#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the squares function below.
def squares(a, b):
    result = set()

    i = a

    while i <= b:
        sqrt = int(math.sqrt(i))
        square = int(math.pow(sqrt, 2))

        if a <= square <= b:
            result.add(square)

        i = int(math.pow(sqrt + 1, 2))

    return len(list(result))

    # Or...
    # 두 정수 사이의 제곱근의 개수를 구하는 것만으로도
    # 답을 구할 수 있다.
    # 여기서 b는 내림을 해주고, a는 올림을 해준 다음에 +1을 하면 개수가 나온다.
    return int(math.sqrt(b)) - int(math.ceil(math.sqrt(a))) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
