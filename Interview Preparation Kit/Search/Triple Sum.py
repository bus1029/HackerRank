#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


# Complete the triplets function below.
def triplets(a, b, c):
    # 10개의 Test Case 중에서 5개가 Time out이 발생
    """
    # b의 원소들을 기준으로 triplets을 만들어보자
    a, b, c = list(set(a)), list(set(b)), list(set(c))
    triplets = 0

    a.sort()
    c.sort()

    # Triplet (p, q, r)의 q를 기준으로
    for q in b:
        # Initialize p_count and r_count
        p_c, r_c = 0, 0

        for p in a:
            if p <= q:
                p_c += 1
            else:
                break

        for r in c:
            if r <= q:
                r_c += 1
            else:
                break

        # Total Triplets (q를 기준으로 했기 때문에 p, r의 쌍만큼 갯수가 나온다)
        triplets += p_c * r_c

    return triplets
    """
    # 위 코드의 문제점은 b를 기준으로 순회할 때
    # a와 c가 항상 처음부터 다시 돈다는 점이다.
    # 이 때, 처음부터 다시 돌지말고 돈 곳부터 다시 돌린다면 더 빠르게 해결할 수 있다.
    # 왜냐하면 b를 정렬한 상태에서 순회할 때, b가 커질수록 기존에 구해놓은 a와 c의
    # 값들이 모두 포함되기 때문이다.
    # Time Complexity: O(n + n + n)
    a, b, c = list(sorted(set(a))), list(sorted(set(b))), list(sorted(set(c)))
    triplets = 0

    ai, bi, ci = 0, 0, 0

    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1

        triplets += ai * ci
        bi += 1

    return triplets


    # 이진탐색 알고리즘으로도 해결할 수 있다.
    # 말그대로 b의 원소보다 작은 a와 c의 원소의 개수를 구하면 되기 때문에
    # Python의 내장 함수 중 하나인 bisect를 사용한다.
    # bisect(a, x)를 사용하게 되면 a배열에 x를 집어넣고 난 뒤의 index 값을 리턴한다.
    # index 값을 리턴하기 때문에, x 값보다 작은 원소들의 갯수로 그대로 사용하면 된다.
    # 이 때, bisect는 같은 값이 있다면 그 값의 오른쪽 위치를 취한다.
    """
    a, b, c = sorted(set(a)), sorted(set(b)), sorted(set(c))
    
    return sum([bisect.bisect(a, x) * bisect.bisect(c, x) for x in b])
    """


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
