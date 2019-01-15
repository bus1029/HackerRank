#!/bin/python3

import os
import sys


#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    final = []

    for grade in grades:
        if grade < 38:
            final.append(grade)
        else:
            value = grade // 5

            if (5 * (value + 1)) - grade < 3:
                final.append(5 * (value + 1))
            else:
                final.append(grade)

    return final


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
