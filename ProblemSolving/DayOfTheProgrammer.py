#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    # Check Julian and Gregorian
    # 윤년이면 244, 윤년아니면 243 (8월까지)

    # Julian
    if year <= 1917:
        # 윤년
        if year % 4 == 0:
            return str(256-244)+"."+"09"+"."+str(year)
        else:
            return str(256-243)+"."+"09"+"."+str(year)
    # Gregorian
    elif year >= 1919:
        # 윤년
        if year % 400 == 0:
            return str(256-244)+"."+"09"+"."+str(year)
        elif year % 4 == 0 and year % 100 != 0:
            return str(256-244)+"."+"09"+"."+str(year)
        else:
            return str(256-243)+"."+"09"+"."+str(year)
    # 바뀐날 (2월 14일로 건너뛰어버림)
    elif year == 1918:
        # 윤년이 아니기 때문에
        return str(256-230)+"."+"09"+"."+str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
