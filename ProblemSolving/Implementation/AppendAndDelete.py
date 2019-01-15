#!/bin/python3

import math
import os
import random
import re
import sys
from difflib import SequenceMatcher


# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # s => start letter
    # t => destination letter
    # k => number of operation
    # seq_matcher = SequenceMatcher(None, s, t)
    # match = seq_matcher.find_longest_match(0, len(s), 0, len(t))

    # # match.a => 첫번째 문자열의 공통 부분 시작 index
    # # match.b => 두번째 문자열의 공통 부분 시작 index
    # # match.size => 공통 문자열의 길이

    # if match.size != 0:
    #     not_common_a = s[match.a+match.size:]
    #     not_common_b = t[match.b+match.size:]

    #     if len(not_common_a) == 0 and len(not_common_b) == 0:
    #         return "Yes"
    #     elif len(not_common_a) == 0 and len(not_common_b) != 0:
    #         if len(not_common_b) <= k and (k - len(not_common_b)) % 2 == 0:
    #             return "Yes"
    #         else:
    #             return "No"
    #     elif len(not_common_a) != 0 and len(not_common_b) == 0:
    #         if len(not_common_a) <= k and (k - len(not_common_a)) % 2 == 0:
    #             return "Yes"
    #         else:
    #             return "No"
    #     else:
    #         if len(not_common_a) + len(not_common_b) <= k and (k - len(not_common_a) - len(not_common_b)) % 2 == 0:
    #             return "Yes"
    #         else:
    #             return "No"
    # # 공통 부분이 없는 경우
    # else:
    #     if len(s) + len(t) <= k:
    #         return "Yes"
    #     else:
    #         return "No"

    i = 0
    d = 0
    # 처음부터 겹친만큼 Count
    # 처음부터 안겹치면 Count = 0
    while (i < len(s) and i < len(t) and s[i] == t[i]):
        i += 1

    d = len(s) - i  # number of deleting needed
    d += len(t) - i  # number of adding needed

    #     // Case 1: See if we can convert String "s" to String "t" without completely erasing String "s".
    # //     We keep erasing charcters from String "s" until it becomes a prefix of String "t". We
    # //     then add the characters needed to turn String "s" into String "t". If we need to waste
    # //     operations to reach "k" operations, we can only do so in groups of 2 by doing an append
    # //     and a delete.

    # // Case 2: See if we can completely erase String "s" and append String "t". If we need to waste
    # //         operations to reach "k" operations, we can do so when String "s" has no characters.

    if ((k >= d and (k - d) % 2 == 0) or (k >= len(s) + len(t))):
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
