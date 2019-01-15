#!/bin/python3

import os
import sys


#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #

    while len(a) != 1:
        result = []

        # 순차적으로 순회할 수도 있지만,
        # 양쪽 것들을 합쳐가면서
        # log 단위로 시간복잡도를 낮춤
        for i in range(int((len(a) + 1) // 2)):
            result.append(lcm(a[i], a[-1 - i]))

        a = result

    lcm_a = a[0]
    count = 0
    multi = 1
    flag = True

    # b의 최소보다 작을 경우에만
    while lcm_a * multi <= min(b):
        flag = True

        for num in b:
            # 모두 나눠지면 count++
            if num % (lcm_a * multi) != 0:
                flag = False
                break

        if flag:
            count += 1

        multi += 1
    return count


# 최대공약수
def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)

    return b


# 최소공배수
def lcm(a, b):
    return a * b / gcd(a, b)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
