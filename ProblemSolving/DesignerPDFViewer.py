#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    word = word.upper()
    # Using ASCII
    heights = [h[ord(w)-65] for w in word]
    # for w in word:
    #     if height <= h[ord(w)-65]:
    #         height = h[ord(w)-65]

    return len(word) * max(heights)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
