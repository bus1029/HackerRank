#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        """
        k가 홀수일 때, k-1은 짝수이면 (k-1) & k = k-1이 항상 성립한다.
        즉, (k-1) | k = k이고, ((k-1) | k) <= n이 항상 성립한다.

        k가 짝수일 때, k-1이 홀수이면

        k   = 10110
        k-1 = 10101
        pos = 10111
        k-1 == (k-1) & pos

        (k-1) | k = pos가 n안에 속해 있으면, (k-1) & pos가 k-1이기 때문에 k-1이 나올 수 있지만
        그렇지 않은 경우에는 k-2가 나올 수 있다.
        """
        print(k - 1 if ((k - 1) | k) <= n else k - 2)

        # Brute Force
        # max_i = 0
        # for i in range(0, len(n_list)):
        #     for j in range(i+1, len(n_list)):
        #         i_j = i & j
        #         if i_j > max_i and i_j < k:
        #             max_i = i_j

        # print(str(max_i))




