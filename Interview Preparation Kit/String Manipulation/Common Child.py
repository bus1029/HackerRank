#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
def commonChild(s1, s2):
    # 14개 Test Case 중 5개 Timeout
    """
    # Common Child => Common Subsequence in Two Strings
    m, n = len(s1), len(s2)

    dp = [[0] * (n+1) for _ in range(m+1)]

    # Bottom-up 방식으로 전에 계산됐던 것들이 재사용됨

    # 예를 들어, SA-HAR은
    # S-HAR과 SA-HR 둘 중 하나에서 파생될 수 있는데,
    # 두 개 중 Common Child가 큰 쪽으로 파생되게 한다.

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

    return dp[m][n]
    """


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
