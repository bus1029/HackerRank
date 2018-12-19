# Enter your code here. Read input from STDIN. Print output to STDOUT
#
# import numpy as np
# from sklearn import linear_model

"""
Task
A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the
following list of (x, y) points:

1. (95, 85)
2. (85, 95)
3. (80, 70)
4. (70, 65)
5. (60, 70)

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics?
Determine the equation of the best-fit line using the least squares method, then compute and print the
value of y when x = 80.

"""

xl = [95, 85, 80, 70, 60]
# x = np.asarray(xl).reshape(-1, 1)
y = [85, 95, 70, 65, 70]
# lm = linear_model.LinearRegression()
# lm.fit(x, y)
#
# y = lm.intercept_ + (lm.coef_[0] * 80)
#
# print(round(y, 3))

n = len(xl)
sum_x = sum(xl)
m_x = sum_x / n
sum_y = sum(y)
m_y = sum_y / n

x_square = sum([num ** 2 for num in xl])
xy = sum([xi * yi for xi, yi in zip(xl, y)])

b = (n * xy - sum_x * sum_y) / (n * x_square - sum_x**2)
a = m_y - b * m_x

print(round(a + b * 80, 3))
