#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    # Time Out이 떴다.
    # Money의 수가 기하급수적으로 클 때
    # 너무 많은 경우의 수 비교가 일어나서
    # 그런것으로 분석된다.
    """
    # Making Money HashTable
    cost_table = {}
    m1, m2 = -1, -1

    for c in cost:
        try:
            cost_table[c] += 1
        except KeyError:
            cost_table[c] = 1

    # for문을 돌면서 cost에 부합하는 Money가 있는지 찾음
    # 예를 들어서 money = 4
    # (1, 3), (2, 2)
    # cost = 5
    # (1, 4), (2, 3)
    for i in range(1, (money//2)+1):
        remain = money-i

        if remain == i:
            try:
                if cost_table[i] == 2:
                    m1, m2 = i, remain
                    break
            except KeyError:
                continue
        else:
            try:
                if cost_table[i] == 1 and cost_table[remain] == 1:
                    m1, m2 = i, remain
                    break

            except KeyError:
                continue

    # 같은 경우에는 모든 Index를 찾아서
    if m1 == m2:
        indices = [i for i, v in enumerate(cost) if v == m1]
        print(str(indices[0]+1) + " " + str(indices[1]+1))
    else:
        # Index는 Ascending으로 출력되야함
        m1_idx = cost.index(m1)+1
        m2_idx = cost.index(m2)+1
        print(str(min(m1_idx, m2_idx)) + " " + str(max(m1_idx, m2_idx)))
    """

    # money // 2만큼 for문을 도는게 아니라
    # 만들어놓은 HashTable로 for문을 돌면 해결 될 것 같다.

    # Making Money HashTable
    cost_table = {}
    m1, m2 = -1, -1

    for c in cost:
        try:
            cost_table[c] += 1
        except KeyError:
            cost_table[c] = 1

    for m, count in cost_table.items():
        # 만약 money가 5고 m이 3이라면 remain은 2
        remain = money - m

        try:
            # 같은 경우에는 count가 2개이상 있어야 되기 때문에
            # 답을 찾았으면 바로 break (하나의 정답만 있다고 했기 때문에)
            if remain == m:
                if cost_table[remain] > 1:
                    m1, m2 = m, remain
                    break
            else:
                if cost_table[remain] > 0:
                    m1, m2 = m, remain
                    break
        except KeyError:
            continue

    # 같은 경우에는 모든 Index를 찾아서
    if m1 == m2:
        indices = [i for i, v in enumerate(cost) if v == m1]
        print(str(indices[0]+1) + " " + str(indices[1]+1))
    else:
        # Index는 Ascending으로 출력되야함
        m1_idx = cost.index(m1)+1
        m2_idx = cost.index(m2)+1
        print(str(min(m1_idx, m2_idx)) + " " + str(max(m1_idx, m2_idx)))



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
