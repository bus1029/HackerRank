# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

"""
Task
The final grades for a Physics exam taken by a large group of students have a mean of m=70
and a standard deviation of s=10.
If we can approximate the distribution of these grades by a normal distribution,
what percentage of the students:

1. Scored higher than  (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade >= 60)?
3. Failed the test (i.e., have a grade < 60)?

"""

# Cumulative Distribution Function for a function with normal distribution
def cdf(m, s, x):
    return 0.5 * (1 + math.erf((x-m) / (s * math.sqrt(2))))


mean, std = 70, 10

# First grade > 80
print(round((1 - cdf(mean, std, 80)) * 100, 2))

# Second grade >= 60
print(round((1 - cdf(mean, std, 60)) * 100, 2))

# Third grade < 60
print(round(cdf(mean, std, 60) * 100, 2))
