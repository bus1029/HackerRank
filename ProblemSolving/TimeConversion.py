#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    am_pm = "".join(s[-2:]).upper()
    #     time = list(s[:-2])
    #     hour = "".join(time[:2])

    #     if am_pm == "PM":
    #         if int(hour) == 12:
    #             return "".join(time)
    #         else:
    #             hour = list(str(int(hour) + 12))
    #             time[:2] = hour[:2]
    #             return "".join(time)
    #     else:
    #         if int(hour) == 12:
    #             time[:2] = ['0', '0']
    #             return "".join(time)
    #         else:
    #             return "".join(time)
    
    if am_pm == "PM":
        if int(s[:2]) == 12:
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]
    else:
        if int(s[:2]) == 12:
            return '00' + s[2:-2]
        else:
            return s[:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
