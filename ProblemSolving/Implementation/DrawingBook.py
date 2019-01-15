#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    pages = [i for i in range(n + 1)]
    front_found, back_found = 0, 0

    # 책을 꽉 채워주고
    if n % 2 == 0:
        pages.append(0)

    # 앞, 뒤에서 동시에 찾음
    for i in range(0, len(pages), 2):
        front_part = [pages[i], pages[i + 1]]
        back_part = [pages[-1 - i], pages[-2 - i]]

        if p in front_part:
            back_found += 1
            break
        elif p in back_part:
            front_found += 1
            break

        front_found += 1
        back_found += 1

    # 미친 솔루션...
    # return min(p//2,n//2-p//2)

    return min([front_found, back_found])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
