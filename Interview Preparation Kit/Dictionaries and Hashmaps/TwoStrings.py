#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_s2 = Counter(s1) - Counter(s2)

    # Counter Dictionary끼리 빼면, 사라지는 Key들과 Count가 줄어드는 Key들이 발생함
    for word, count in Counter(s1).items():
        try:
            # Count가 달라지는 경우에는 사용되었다는 의미이므로, YES
            if s1_s2[word] != count:
                return "YES"
        # Key가 사라지는 경우에는 사용되었다는 의미이므로, YES
        except KeyError:
            return "YES"

    # 그 외의 경우에는 모두 NO
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
