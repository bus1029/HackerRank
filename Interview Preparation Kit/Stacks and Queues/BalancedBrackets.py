#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []

    for ch in s:
        # 왼쪽 괄호가 들어오면 Stack에 쌓음
        if ch == "(" or ch == "{" or ch == "[":
            stack.append(ch)

        # 오른쪽 괄호의 타입에 따라서 나눔
        elif ch == ")":
            try:
                if stack[len(stack)-1] == "(":
                    stack.pop()
                else:
                    return "NO"
            except IndexError:
                return "NO"
        elif ch == "}":
            try:
                if stack[len(stack)-1] == "{":
                    stack.pop()
                else:
                    return "NO"
            except IndexError:
                return "NO"

        elif ch == "]":
            try:
                if stack[len(stack)-1] == "[":
                    stack.pop()
                else:
                    return "NO"
            except IndexError:
                return "NO"

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')
        # print(result)

    fptr.close()
