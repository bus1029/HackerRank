# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

"""
Task

Andrea has a simple equation:

    Y = a + b1f1 + b2f2 + ... + bmfm

for (m + 1) real constants(a, f1, f2, ..., fm). We can say that the value of Y depends on m features.
Andrea studies this equation for n different feature sets (f1, f2, f3, ..., fm) and records each respective value of Y.
If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?

Note: You are not expected to account for bias and variance trade-offs.

"""

# Number of observed features m, Number of feature sets Andrea studied n
m, n = list(map(int, input().split()))

X = []
Y = []

# Make X, Y Matrix
for i in range(n):
    xy = list(map(float, input().split()))

    X.append([1.0] + xy[:m])
    Y += xy[m:]

# q, denoting the number of feature sets Andrea wants to query for.
q = int(input())

query_b = []
for i in range(q):
    b = list(map(float, input().split()))

    query_b.append([1.0] + b)

X = np.array(X, float)
Y = np.array(Y, float)
query_b = np.array(query_b, float)

XtX = np.dot(X.transpose(), X)
XtX_inv = np.linalg.inv(XtX)
XtX_inv_Xt = np.dot(XtX_inv, X.transpose())

B = np.dot(XtX_inv_Xt, Y)
query_Y = list(np.dot(b, B) for b in query_b)

for q_y in query_Y:
    print(round(float(q_y), 3))





