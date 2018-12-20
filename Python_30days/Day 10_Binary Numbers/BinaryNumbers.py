#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby



if __name__ == '__main__':
    n = int(input())

    n_bin = bin(n)[2:]
    groups = groupby(n_bin)

    # result = [(label, sum(1 for _ in group)) for label, group in groups]
    result = [sum(1 for _ in group) for _, group in groups]

    print(max(result))
