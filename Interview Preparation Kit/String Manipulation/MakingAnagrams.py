#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    """
    Anagram이란 기존의 문자들을 재배열해서 새로운 문자가 만들어지는 것
    => 기존의 문자 외에 다른 문자가 있으면 그 단어는 Anagram이 될 수 없다.
    """
    to_anagram = 0

    # 공통 문자를 제외하고 나머지만 남게됨 (Dictionary)
    a_b = Counter(a) - Counter(b)
    b_a = Counter(b) - Counter(a)

    # 나머지들의 숫자를 Count하면 a, b가 Anagram이 되기위해 지워야할 문자수가 나옴
    to_anagram += sum([count for _, count in a_b.items()])
    to_anagram += sum([count for _, count in b_a.items()])

    # 또다른 방법으로는 Set을 이용하는 방법이 있음
    # 같은 문자들은 사라질거고, 다른 문자들은 count가 달라서 더해짐
    """
    count = 0
    for i in list(set(a+b)):
        count += abs(a.count(i) - b.count(i))
    return count
    """

    # 또다른 방법으로는 subtract하는 방법이 있음
    # aTable.subtract(bTable)을 하게되면
    # aTable에 없는 Key들은 - Value를 가지게 됨
    # 공통된 것들은 0으로 변하고
    # 0이 아닌 것들을 더해주면 됨.
    """
    aTable = Counter(a)
    bTable = Counter(b)

    aTable.subtract(bTable)
    deletions = 0
    for key, value in aTable.items():
        if value != 0:
            deletions += abs(value)
    return deletions
    """

    return to_anagram


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
