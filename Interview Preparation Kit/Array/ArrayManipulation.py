#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    """

    :param n:
    :param queries:
    :return:
    """
    # Input Format::
    # The first line contains two space-separated integers n and m,
    # the size of the array and the number of operations.
    # Each of the next m lines contains three space-separated integers a, b and k.
    # the left index, right index and summand.

    # Constraints
    # 3 <= n <= pow(10, 7)
    # 1 <= m <= 2 * pow(10, 5)
    # 1 <= a <= b <= n
    # 0 <= k <= pow(10, 9)

    # 단순히 더하기로 해서는 Timeout...
    # result = [0 for _ in range(n+1)]
    # for query in queries:
    #     for i in range(query[0], query[1]+1):
    #         result[i] += query[2]

    # return max(result)

    """
        숫자를 다 더하면 시간이 오래걸리기 때문에, 비교값만을 Array에다 기록한다.
        예를 들어,
        
        a b k
        1 5 3
        4 8 7
        6 9 1
        이 있을 때, 
        
        init -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        1, 5, 3 -> [3, 0, 0, 0, 0, -3, 0, 0, 0, 0] => 1~5까지는 3이고 6부터는 3보다 작은 값이다.
        4, 8, 7 -> [3, 0, 0, 7, 0, -3, 0, 0, -7, 0] => 1~3까지는 3이고 4~5까지는 10이고 6~8은 7이고 9~10은 0이다.
        6, 9, 1 -> [3, 0, 0, 7, 0, -2, 0, 0, -7, -1] => 1~3까지는 3이고 4~5까지는 10이고 6~8까지는 8이고 9는 1, 10은 0이다.
        
        기록한 후, 양수의 합이 Max가 되는 값을 찾으면 된다.
    """
    result = [0] * (n+1)
    p_sum, max_val = 0, 0

    for (b, e, s) in queries:
        # Index로 접근하기 때문에 1을 빼야됨
        result[b-1] += s
        result[e] -= s

    for i in result:
        p_sum += i

        # Find the Largest Value in Result List
        if max_val < p_sum:
            max_val = p_sum

    return max_val


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
