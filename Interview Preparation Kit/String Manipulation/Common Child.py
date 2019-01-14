#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below.
def commonChild(s1, s2):
    # 14개 Test Case 중 5개 Timeout
    # PyPy3 로 하면 모든 Case 통과...
    """
    # Common Child => Common Subsequence in Two Strings
    m, n = len(s1), len(s2)

    dp = [[0] * (n+1) for _ in range(m+1)]

    # Bottom-up 방식으로 전에 계산됐던 것들이 재사용됨

    # 예를 들어, SA-HAR은
    # S-HAR과 SA-HA 둘 중 하나에서 파생될 수 있는데,
    # 두 개 중 Common Child가 큰 쪽으로 파생되게 한다.

    for i in range(1, m+1):
        for j in range(1, n+1):
            # 같은 경우
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    """

    # 여기서 2차원 배열을 모두 사용하지 말고
    # 이전 결과를 불러오는 전 Row만 사용한다면
    # Space Complexity를 줄일 수 있다.
    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[1][j] = dp[0][j - 1] + 1
            else:
                dp[1][j] = max(dp[1][j - 1], dp[0][j])

        # 마지막 Row를 그 전 Row로 옮겨주고
        # 다음 Row를 0으로 채움
        dp[0] = dp[1]
        dp[1] = [0] * (n + 1)

    # 마지막에 한칸 올려졌기 때문에
    return dp[0][n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
