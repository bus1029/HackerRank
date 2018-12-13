#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    if int(N) % 2 == 1:
        print("Weird")
    elif int(N) % 2 == 0 and 2 <= int(N) <= 5:
        print("Not Weird")
    elif int(N) % 2 == 0 and 6 <= int(N) <= 20:
        print("Weird")
    elif int(N) % 2 == 0 and 20 < int(N):
        print("Not Weird")