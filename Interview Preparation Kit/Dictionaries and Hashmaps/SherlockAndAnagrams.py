#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
from itertools import permutations

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagram_cnt = 0

    # For One Word e.g kkkk
    # k = 4
    # k anagram => 4 * 3 / 2
    counts = Counter(s)

    for word, count in counts.items():
        if count >= 2:
            anagram_cnt += (count * (count-1)) / 2

    # More than 2
    # Save all Word Counts into Dictionary
    # And Hashing...
    # But Time-out
    # for i in range(2, len(s)):
    #     word_counts = {}
    #
    #     # Get All Substrings in String and Make Hashmap
    #     for j in range(0, len(s)):
    #         if len(s[j:j + i]) == i:
    #             word_counts[s[j:j + i]] = Counter(s[j:j + i])
    #
    #     # Check Anagram
    #     for k in range(0, len(s)):
    #         for l in range(k+1, len(s)):
    #             try:
    #                 if word_counts[s[k:k+i]] - word_counts[s[l:l+i]] == {}:
    #                     anagram_cnt += 1
    #             except KeyError:
    #                 continue

    # More than 2
    # 단어의 Counter를 저장하는게 아니고,
    # Anagram이라는건 단어를 정렬했을 때 같은 형태로 단어가 나오면 성립
    for i in range(2, len(s)):
        word_counts = {}

        for j in range(0, len(s)):
            if len(s[j:j+i]) == i:
                try:
                    word_counts[''.join(sorted(s[j:j+i]))] += 1
                except KeyError:
                    word_counts[''.join(sorted(s[j:j+i]))] = 1

        for _, count in word_counts.items():
            if count >= 2:
                anagram_cnt += (count * (count-1)) / 2

    return int(anagram_cnt)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)

        # fptr.write(str(result) + '\n')
    #
    # fptr.close()
