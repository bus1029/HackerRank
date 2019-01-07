#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
import math


# Complete the minTime function below.
def minTime(machines, goal):
    # 13개의 Test Case 중에서 4개 Time out
    """
    machines = sorted(machines)
    machines_dict = {}

    # Making Hashmap for removing duplicates
    for machine in machines:
        try:
            machines_dict[machine] += 1
        except KeyError:
            machines_dict[machine] = 1

    # Get Keys
    machines_key = list(machines_dict.keys())

    produces = 0
    day = 0

    while produces < goal:
        day += 1
        # 이진 탐색을 이용
        # day보다 작은 생산 횟수를 가진 기계들을 먼저 뽑아내기
        smaller_index = bisect.bisect(machines_key, day)

        for machine_index in range(smaller_index):
            if day > 3 and (day // 2) < machines_key[machine_index]:
                # 100일을 예로 들경우, 51~99까지는 의미가 없지만 100은 의미가 있음
                # 하지만, day가 엄청나게 커질 경우 결국 for문을 다돌 수 밖에 없음
                try:
                    produces += machines_dict[day]
                except KeyError:
                    break
                finally:
                    break
            elif day % machines_key[machine_index] == 0:
                produces += machines_dict[machines_key[machine_index]]

    return day
    """
    # day를 1씩 더하는게 아니라면...?
    # day가 아무리 커져도 결국 총합의 Produces는 기계들의 날짜수 / 연산이다.
    # 알맞은 day를 Search 하는게 결국 이 문제의 목적이다
    # Binary Search 를 이용해서 알맞은 day를 찾기
    # Binary Search이기 때문에 O(logn)으로 구할 수 있다.
    # 이 때 기계 전체를 for문으로 돌면서 생산값을 구하기 때문에 n이 곱해져서
    # Time Complexity: O(n logn)

    # 가장 빠른 기계와 가장 느린 기계를 통해
    # Binary Search에 사용할 min과 max를 구함
    min_day = math.ceil(goal / len(machines)) * min(machines)
    max_day = math.ceil(goal / len(machines)) * max(machines)

    """
    밑의 코드가 Binary Search의 기본 구조다.
    잘 알아두면 좋을 것 같다.
    """
    # 최소 일자가 최대 일자를 넘지 않을때 까지 진행
    while min_day < max_day:
        mid_day = (min_day + max_day) // 2

        if sum(mid_day // m for m in machines) >= goal:
            max_day = mid_day
        else:
            min_day = mid_day + 1

    return min_day


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
