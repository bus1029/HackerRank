#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import groupby


# Complete the substrCount function below.
def substrCount(n, s):
    # Special Palindrome:
    # 모두 같은 문자일 경우
    # 중간 하나를 제외하고 모두 같은 문자일 경우

    # 일단 Brute-Force로 접근해보자
    # 하지만 이러면 타임아웃에 걸림
    """
    p_count = 0

    # Window Range
    for i in range(0, len(s)):
        for j in range(0, len(s)-i):
            string = s[j:j+i+1]

            # 홀수면 중간 문자를 제외하고 같은 문자여야 함
            if len(string) == 1:
                p_count += 1
            elif len(string) > 1 and len(string) % 2 == 1:
                # 중간 문자를 지워주고
                string = string[:len(string)//2]+string[len(string)//2+1:]

                # 모두 같은 문자로 이루어져 있으면
                if len(Counter(string)) == 1:
                    p_count += 1

            # 짝수면 모두 같은 문자여야 함
            elif len(string) > 1 and len(string) % 2 == 0:
                if len(Counter(string)) == 1:
                    p_count += 1

    return p_count
    """

    # groupby를 써서 반복되는 문자들을 Count할 수 있다면?
    groups = groupby(s)

    # [(label, value), (label, value), ...]
    # 이런식으로 표현됨
    # [(label, list(group)) for label, group in groups]
    # [('a', ['a', 'a']), ('s', ['s', 's']), ('d', ['d', 'd']), ('f', ['f', 'f'])]
    group_list = [(label, sum(1 for _ in group)) for label, group in groups]
    p_count = 0

    # 모두 하나의 문자로만 이루어진 경우
    # 1, 3, 6, 10, 15, 21, ... 순서로 경우의 수가 늘어남
    if len(group_list) == 1:
        # for i in range(1, group_list[0][1]+1):
        #     p_count += i

        # 위 for문을 공식으로 표현하면
        value = group_list[0][1]
        p_count += (value * (value + 1)) // 2

    else:
        for (label, count) in group_list:
            # 연속되는 문자는 모두 Special Palindrome 취급
            # 연속되는 문자의 경우 모든 경우의 수를 다 따져서 더해줌
            if count > 1:
                p_count += (count * (count + 1)) // 2
            # 하나인 경우는 하나만 더해주고
            else:
                p_count += 1

        # 중간 하나를 제외하고 양쪽으로 같은 문자가 나오는 경우
        for i in range(0, len(group_list) - 2):
            left, center, right = group_list[i], group_list[i + 1], group_list[i + 2]

            # 튜플 접근 ->  [0], [1]
            # 중간 값이 하나고 중간 문자가 좌우 문자와 다르고
            if center[1] == 1 and center[0] != left[0] and center[0] != right[0]:
                # 좌 우의 키가 같으면
                # 여기서 좌우의 Value의 min이 2이상일 경우
                # 그것 만큼 Palindrome이 나올 수 있음
                if left[0] == right[0]:
                    p_count += min(left[1], right[1])
                else:
                    continue
            else:
                continue

    return p_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
