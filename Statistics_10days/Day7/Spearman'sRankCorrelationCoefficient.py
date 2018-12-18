# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from copy import deepcopy

"""
Task

Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.

Constraints

Data set X contains unique values.
Data set Y contains unique values.

"""

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

# Ranking
X_tmp = sorted(X)
Y_tmp = sorted(Y)

X_rank, Y_rank = [], []

for x, y in zip(X, Y):
    X_rank.append(X_tmp.index(x)+1)
    Y_rank.append(Y_tmp.index(y)+1)

r_xy = 1 - ((6 * sum(list((x_r - y_r)**2 for x_r, y_r in zip(X_rank, Y_rank)))) / (n * (n**2 - 1)))

print(round(r_xy, 3))
