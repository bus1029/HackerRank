#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):

    """
    Dynamic Programming은 세부 계산으로 나뉘어지는 하나의 큰 문제를
    세부 계산 결과를 미리 구해서 저장한 후, 큰 계산의 결과를 빠르게 도출해내는 해결 기법이다.

    처음에는 감도 안잡혔는데...
    더 연습해야겠다.
    """
    # Brute Force...
    """
    # 정렬
    sorted_arr = sorted(arr)
    idx_list = []
    sum_list = []

	for i in range(len(sorted_arr)-1, -1, -1):
    	# Initialize
    	sum = sorted_arr[i]
    	idx_list = [arr.index(sorted_arr[i])]

	    # 가장 큰 수 다음부터 반복문
	    for j in range(i-1, -1, -1):
	    	cur_val = sorted_arr[j]
	    	j_idx = arr.index(cur_val)
	    	adjecent = False

	    	# 인접 여부를 판단
	    	for idx in idx_list:
	    		if j_idx == idx-1 or j_idx == idx+1:
	    			adjecent = True
	    			break

	    	if adjecent is False:
	    		if sum < sum + cur_val:
	    			sum = sum + cur_val
	    			idx_list.append(j_idx)
	    		else:
	    			break

	    sum_list.append(sum)

    return max(sum_list)
    """

    # Array 길이 만큼의 리스트를 생성한 후
    dp = [0] * len(arr)
    # 첫 번째 원소는 누구와도 더할 수 없기 때문에 그대로 넣어줌
    dp[0] = arr[0]
    # 두 번째 원소는 첫 번째 원소와 비교해서(Not Adjacent) 큰 값을 넣어줌
    # Sublist의 합이 최대가 되는 값을 찾아야 하기 때문에
    dp[1] = max(arr[1], dp[0])

    # 2번째 원소부터 순회하면서 이전에 계산해놓은 값을 활용하면서 더해간다.
    for i in range(2, len(arr)):
        # 원소 하나만 있는게 큰지, 이전에 더해놓은 값이 더 큰지,
        # 두 칸전에 있는 값이랑 현재 값이랑 더한 값이 큰지 결정
        # 여기서 두 칸전에 있는 값도 예전에 더해놓은 값들이 저장되어 있기 때문에 활용 가능하다.
        dp[i] = max(arr[i], dp[i-1], arr[i] + dp[i-2])

    # 항상 max 값을 저장해놓기 때문에, 가장 마지막 원소를 반환한다.
    return dp[-1]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    # fptr.write(str(res) + '\n')
    #
    # fptr.close()
