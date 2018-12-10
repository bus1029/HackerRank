#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    # Queen은 8방향으로 움직일 수 있다
    # r_q 세로
    # c_q 가로
    # 장애물 개수 k
    # 보드판 크기 n
    # 장애물 위치 obstacles
    # possible_positions = get_queen_possible_positions(n, r_q, c_q)

    # for (a, b) in obstacles:
    #     # obstacle_list = []
    #     # 여기서 뭔가 생략할 수 있는 수단이 있을 것 같은데

    #     for i in range(len(possible_positions)):
    #         if (a, b) in possible_positions[i]:
    #             index = possible_positions[i].index((a, b))
    #             # obstacle_list += possible_positions[i][index:]
    #             # 여기서 왜 실수했지...
    #             possible_positions[i] = possible_positions[i][:index]
    #             break

    # return sum(list(len(possible_position) for possible_position in possible_positions))

    # 퀸이 가는 길을 다 구해서, Obstacle과의 비교를 통해 구할 수도 있지만
    # 이렇게 하면 time out에 걸리는 케이스를 잡아내지 못한다
    # 다른 방법으로는, 퀸이 갈 수 있는 길을 모두 구해서 비교하는 것이 아니라
    # 퀸의 위치로부터 8방향의 길을 하나씩 구해보면서, 장애물에 걸리지 않는 위치까지 Count 하는 것이다
    # l = 1
    # attack_position = 0

    # # North Case
    # # Row가 n과 같을 때까지 비교해봄(Column 고정)
    # r_q2 = r_q
    # while True:
    #     r_q2 += 1
    #     if r_q2 > n: break
    #     if [r_q2, c_q] in obstacles: break
    #     else:
    #         attack_position += 1

    # # East Case
    # # Column이 n과 같을 때까지 비교해봄(Row 고정)
    # c_q2 = c_q
    # while True:
    #     c_q2 += 1
    #     if c_q2 > n: break
    #     if [r_q, c_q2] in obstacles: break
    #     else:
    #         attack_position += 1

    # # South Case
    # # Row가 0보다 클 때까지 비교해봄(Column 고정)
    # r_q2 = r_q
    # while True:
    #     r_q2 -= 1
    #     if r_q2 < l: break
    #     if [r_q2, c_q] in obstacles: break
    #     else:
    #         print((r_q2, c_q))
    #         attack_position += 1

    # # West Case
    # # Column이 0보다 클 때까지 비교해봄(Row 고정)
    # c_q2 = c_q
    # while True:
    #     c_q2 -= 1
    #     if c_q2 < l: break
    #     if [r_q, c_q2] in obstacles: break
    #     else:
    #         attack_position += 1

    # # North East Case
    # # Column, Row가 같이 커짐
    # r_q2, c_q2 = r_q, c_q
    # while True:
    #     r_q2 += 1
    #     c_q2 += 1
    #     if r_q2 > n or c_q2 > n: break
    #     if [r_q2, c_q2] in obstacles: break
    #     else:
    #         attack_position += 1

    # # South East Case
    # # Row는 작아지고 Column은 커짐
    # r_q2, c_q2 = r_q, c_q
    # while True:
    #     r_q2 -= 1
    #     c_q2 += 1
    #     if r_q2 < l or c_q2 > n: break
    #     if [r_q2, c_q2] in obstacles: break
    #     else:
    #         attack_position += 1

    # # South West Case
    # # Row, Column 모두 작아짐
    # r_q2, c_q2 = r_q, c_q
    # while True:
    #     r_q2 -= 1
    #     c_q2 -= 1
    #     if r_q2 < l or c_q2 < l: break
    #     if [r_q2, c_q2] in obstacles: break
    #     else:
    #         attack_position += 1

    # # North West Case
    # # Row는 커지고 Column은 작아짐
    # r_q2, c_q2 = r_q, c_q
    # while True:
    #     r_q2 += 1
    #     c_q2 -= 1
    #     if r_q2 > n or c_q2 < l: break
    #     if [r_q2, c_q2] in obstacles: break
    #     else:
    #         attack_position += 1

    # return attack_position

    # 하지만 이 방법도 비교를 2번 거치기 때문에 Time Out이 발생한다...

    # 다른 방법은?
    # 모든 장애물들을 for문으로 돌면서
    # Queen이 갈 수 있는 길의 Boundary를 구하는 방법이다
    # 8 방향으로 갈 수 있는 모든 길들의 경계선들을 구하면
    # 각 방향의 길이를 측정하면 갈 수 있는 길의 개수가 나온다

    # initialization

    # 오른쪽으로 갈 수 있는 Column 길이
    horizon_r = n - c_q
    # 왼쪽으로 갈 수 있는 Column 길이
    horizon_l = c_q - 1
    # 위로 갈 수 있는 Row 길이
    verti_u = n - r_q
    # 아래로 갈 수 있는 Row 길이
    verti_l = r_q - 1
    # 우측 위로 갈 수 있는 대각선 길이 (North East)
    diapos_u = min(n - r_q, n - c_q)
    # 좌측 아래로 갈 수 있는 대각선 길이 (South West)
    diapos_l = min(r_q - 1, c_q - 1)
    # 좌측 위로 갈 수 있는 대각선 길이 (North West)
    dianeg_u = min(n - r_q, c_q - 1)
    # 우측 아래로 갈 수 있는 대각선 길이 (South East)
    dianeg_l = min(r_q - 1, n - c_q)

    # 장애물들을 하나씩 돌면서 길이를 줄여나감
    for row, col in obstacles:
        # print (row,col)
        if row == r_q:  # Row가 같은 경우 Column의 길이를 줄일 수 있다
            if (col - c_q > 0) and (col - c_q - 1 < horizon_r):  # right_obs
                horizon_r = col - c_q - 1
            if (col - c_q < 0) and (c_q - col - 1 < horizon_l):  # left_obs
                horizon_l = c_q - col - 1
        if col == c_q:  # Column이 같은 경우 Row의 길이를 줄일 수 있다
            if (row - r_q > 0) and (row - r_q - 1 < verti_u):  # upper_obs
                verti_u = row - r_q - 1
            if (row - r_q < 0) and (r_q - row - 1 < verti_l):  # lower_obs
                verti_l = r_q - row - 1
        if row - col == r_q - c_q:  # 우측 대각선 상에 있는 경우 (Row-Column의 차가 같은 경우)
            # Row로 비교하는 이유는 일직선 상에 내려서 점으로 비교하기 때문
            if (row - r_q > 0) and (row - r_q - 1 < diapos_u):  # positive_diagnose_up_obs
                diapos_u = row - r_q - 1
            if (row - r_q < 0) and (r_q - row - 1 < diapos_l):  # positive_diagnose_low_obs
                diapos_l = r_q - row - 1
        if row + col == r_q + c_q:  # 좌측 대각선 상에 있는 경우 (Row+Column의 합이 같은 경우)
            # Row로 비교하는 이유는 일직선 상에 내려서 점으로 비교하기 때문
            if (row > r_q) and (row - r_q - 1 < dianeg_u):  # negative_diagose_up_obs
                dianeg_u = row - r_q - 1
            if (row < r_q) and (r_q - row - 1 < dianeg_l):  # negative_diagose_low_obs
                dianeg_l = r_q - row - 1

                # 퀸으로부터의 남은 거리들을 모두 더하면, 갈 수 있는 모든 지점이 나오게 됨
    return horizon_l + horizon_r + verti_l + verti_u + diapos_l + diapos_u + dianeg_l + dianeg_u


def get_queen_possible_positions(n, r_q, c_q):
    possible_positions = []

    # NORTH
    possible_positions.append([(i, c_q) for i in range(r_q + 1, n + 1)])
    # WEST
    possible_positions.append([(r_q, i) for i in range(c_q - 1, 0, -1)])
    # EAST
    possible_positions.append([(r_q, i) for i in range(c_q + 1, n + 1)])
    # SOUTH
    possible_positions.append([(i, c_q) for i in range(r_q - 1, 0, -1)])
    # NORTH_EAST
    possible_positions.append([(r_q + i, c_q + i) for i in range(1, min(n - r_q, n - c_q) + 1)])
    # SOUTH_WEST
    possible_positions.append([(r_q - i, c_q - i) for i in range(1, min(r_q, c_q))])
    # NORTH_WEST
    possible_positions.append([(r_q + i, c_q - i) for i in range(1, min(n - r_q, c_q - 1) + 1)])
    # SOUTH_EAST
    possible_positions.append([(r_q - i, c_q + i) for i in range(1, min(r_q - 1, n - c_q) + 1)])

    return possible_positions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
