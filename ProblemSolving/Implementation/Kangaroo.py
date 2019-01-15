#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # Condition of EXACTLY NO
    if (x1 < x2) and (v1 <= v2):
        return "NO"
    elif (x1 > x2) and (v1 >= v2):
        return "NO"

    count, value1, value2 = 0, 0, 0

    while True:
        value1 = x1 + (v1 * count)
        value2 = x2 + (v2 * count)
        count += 1

        if value1 == value2:
            return "YES"
        else:
            # 시작점이 뒤처진 캥거루가 앞선 캥거루를 앞지른 순간 끝
            if (x1 > x2) and (v1 < v2):
                if value1 < value2:
                    return "NO"
                else:
                    continue
            elif (x1 < x2) and (v1 > v2):
                if value1 > value2:
                    return "NO"
                else:
                    continue


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
