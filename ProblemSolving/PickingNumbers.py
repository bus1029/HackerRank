#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
from collections import Counter


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    # 순열로 해결되는 경우 (1, 2), (98, 99), ...
    a.sort()

    a_comb = list(set(itertools.permutations(a, 2)))
    a_comb = list(filter(lambda x: x[0] - x[1] == 1, a_comb))

    result = []

    for (num1, num2) in a_comb:
        count = 0
        for comparison in a:
            if comparison > max(num1, num2):
                break
            if comparison == num1 or comparison == num2:
                count += 1

        result.append(count)

    # 단일 개체로 가장 많은 경우
    counter = Counter(a)
    max_number = max(a, key=counter.get)

    count = 0
    for num in a:
        if num > max_number:
            break
        if max_number == num:
            count += 1

    result.append(count)

    return max(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
