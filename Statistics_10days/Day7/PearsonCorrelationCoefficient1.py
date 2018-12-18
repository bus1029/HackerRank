# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

"""
Task

Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

"""


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

# Mean
x_m = sum(X) / len(X)
y_m = sum(Y) / len(Y)

# Variance
x_v = sum(list((num - x_m)**2 for num in X)) / len(X)
y_v = sum(list((num - y_m)**2 for num in Y)) / len(Y)

# Standard Deviation
x_sd = math.sqrt(x_v)
y_sd = math.sqrt(y_v)

# Pearson Correlation Coefficient
p_xy = sum(list((xi - x_m) * (yi - y_m) for xi, yi in zip(X, Y))) / (n * x_sd * y_sd)

print(round(p_xy, 3))
