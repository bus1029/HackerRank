#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    """
    Sherlock considers a string to be valid if all characters of the string appear the same number of times.
    It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will
    occur the same number of times.

    e.g., abc, abcc
    """
    # Make Counter Dictionary
    s_counts = Counter(s)
    # Only extracts count in dictionary
    s_list = [count for _, count in s_counts.items()]

    # 최소 최대 값이 같은 경우
    if max(s_list) == min(s_list):
        return "YES"
    # 최소값의 개수가 하나이면서 값이 1인 경우
    elif s_list.count(min(s_list)) == 1 and s_list.count(max(s_list)) != 1 and min(s_list) == 1:
        return "YES"
    # 최대값의 개수가 하나이면서
    elif s_list.count(min(s_list)) != 1 and s_list.count(max(s_list)) == 1:
        # 최대값과 최소값의 차이가 1이나면 Yes
        if abs(max(s_list) - min(s_list)) == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
