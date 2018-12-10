#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    # s => string
    # n => consider number

    # 한 문장의 길이
    divisor = len(s)
    # 문장에 포함된 a의 개수
    a_count = s.count('a')

    remain = n % divisor

    count = (n // divisor) * a_count
    count += sum(list(1 for i in range(remain) if s[i] == 'a'))

    # Or
    # return (s.count("a") * (n // len(s)) + s[:n%len(s)].count("a"))

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
