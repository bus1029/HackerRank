#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ranking_list = []
    sub_rank = -1
    alice_rank = []

    # 순서를 유지하면서 List에서 중복 제거
    scores = list(OrderedDict.fromkeys(scores))

    # 거꾸로 for
    last_index = len(scores)

    # Rank Alice's Scores
    for a_score in alice:
        rank_flag = False

        for i in reversed(range(last_index)):
            # 작은 경우, Ranking List 순위 변경
            print(scores[i])
            if a_score < scores[i]:
                rank_flag = True
                alice_rank.append(i + 2)
                scores.insert(i + 1, a_score)
                last_index = i + 1
                break

            elif a_score == scores[i]:
                rank_flag = True
                alice_rank.append(i + 1)
                last_index = i + 1
                break

        # Ranking에 반영이 못된 경우 => 1등
        if rank_flag is False:
            alice_rank.append(1)
            ranking_list.insert(0, a_score)

    return alice_rank


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
