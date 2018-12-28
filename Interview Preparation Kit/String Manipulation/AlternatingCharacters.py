#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    """
    같은 문자가 반복되면 반복되는 문자를 지워서 Count
    """
    repeated = 0
    before_word = ""

    for word in s:
        # 처음엔 무조건 배정
        if before_word == "":
            before_word = word
        # 같은 경우 => 반복되는 문자 발견
        elif before_word == word:
            repeated += 1
        # 다른 경우
        else:
            before_word = word

    # 좀 더 단순하게 생각하면,
    # 현재 단어와 다음 단어가 같으면 count++
    """
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            repeated += 1
    """

    return repeated

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
