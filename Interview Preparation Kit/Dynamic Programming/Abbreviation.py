#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the abbreviation function below.
def abbreviation(a, b):
    # # 이건 다이나믹 프로그래밍이 아니다.
    # b_idx = 0
    #
    # for i in range(len(a)):
    #     if b_idx < len(b):
    #         if a[i].upper() == b[b_idx]:
    #             b_idx += 1
    #         else:
    #             if a[i].upper() != a[i]:
    #                 continue
    #             else:
    #                 return "NO"
    #     else:
    #         if a[i].upper() != a[i]:
    #             continue
    #         else:
    #             return "NO"
    #
    # if b_idx == len(b):
    #     return "YES"
    # else:
    #     return "NO"
    m, n = len(a), len(b)
    # b의 길이가 0일때부터 n일 때까지 모든 a 길이 만큼에 대해서 False인 2차원 배열을 생성
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # a, b가 모두 비어있는 경우 True
    dp[0][0] = True

    # b가 비어있고, a[i-1]이 소문자로 이루어진 경우 True
    for i in range(1, m + 1):
        dp[i][0] = a[i - 1].islower()

    """
        a = AaB
        b = AB

        dp = 
            0   A   B
        0   T   F   F
        a   T   T   F
        A   F   T   F
        b   T   T   T
        
        dp[3][2] = True => 'YES'
        'a' - 'A' = ' ' - ' ' | ' ' - 'A'
        'a'-'A'가 만들어지려면, ' '-' '에서 만들어지던지, 
        ' ' - 'A'에서 만들어져야 한다. 그래서 OR를 통해서 True / False를 판단한다.

        'a' - 'AB' = ' ' - 'AB'에서 밖에 안만들어지므로 False.
    """

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a_dp = a[i - 1]
            b_dp = b[j - 1]

            # a가 대문자인 경우
            if a_dp.isupper():
                if a_dp == b_dp:
                    dp[i][j] = dp[i - 1][j - 1]
            # a가 소문자인 경우
            else:
                if a_dp.upper() == b_dp:
                    dp[i][j] = dp[i - 1][j - 1] | dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

    return "YES" if dp[m][n] else "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        # fptr.write(result + '\n')
    #
    # fptr.close()
