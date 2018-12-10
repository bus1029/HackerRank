#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    # height = 0

    # for i in range(n+1):
    #     if i % 2 == 0:
    #         height += 1
    #     else:
    #         height *= 2

    # return height

    # year 1 (2 cycles) : 1*2+1 = 3     ->      11
    # year 2 (4 cycles) : 3*2+1 = 7     ->     111
    # year 3 (6 cycles) : 7*2+1 = 15    ->    1111
    # year 4 (8 cycles) : 15*2+1 = 31   ->   11111
    # year 5 (10 cycles) : 31*2+1 = 63  ->  111111


    # you can get the answer by putting 1 as much as (year + 1).
    # how to make this? shift 1 by (year + 1) and subtract 1.

    # straight forward bit calculation is this:

    # (1<<((N>>1)+1))-1
    # * N>>1 : devide N by 2 to get year
    # 1 << (year+1) : if year is 5, it will make 1000000
    # -1 will make 1000000 to 111111.

    # if cycle is odd, that means the tree will be doubled again.

    # ((1<<((N>>1)+1))-1) << n%2

    return ((1<<((n>>1)+1))-1) << n%2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
