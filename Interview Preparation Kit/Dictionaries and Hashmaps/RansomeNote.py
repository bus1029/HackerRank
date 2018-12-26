#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # if Counter(note) - Counter(magazine) == {}:
    #     print("Yes")
    # else:
    #     print("No")
    magazine_words = {}

    # 매거진 워드들을 하나씩 뽑아서 Dictionary에 저장
    for word in magazine:
        try:
            magazine_words[word] += 1
        except KeyError:
            magazine_words[word] = 1

    # 매거진 Dictionary에 해당 단어가 없거나, 단어의 카운트가 0이 됐는데 사용하려고 한다면 No Return
    for word in note:
        try:
            if magazine_words[word] == 0:
                return print("No")
            else:
                magazine_words[word] -= 1
        except KeyError:
            return print("No")

    return print("Yes")



if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
