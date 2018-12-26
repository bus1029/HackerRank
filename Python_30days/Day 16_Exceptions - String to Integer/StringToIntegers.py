#!/bin/python3

import sys


S = input().strip()

try:
    S_integer = int(S)
    print(str(S_integer))

except ValueError:
    print("Bad String")