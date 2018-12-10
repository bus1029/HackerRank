#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    type_list = [0, 0, 0, 0, 0]

    for bird in arr:
        if bird == 1:
            type_list[0] += 1
        elif bird == 2:
            type_list[1] += 1
        elif bird == 3:
            type_list[2] += 1
        elif bird == 4:
            type_list[3] += 1
        else:
            type_list[4] += 1

    return int(type_list.index(max(type_list))) + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
