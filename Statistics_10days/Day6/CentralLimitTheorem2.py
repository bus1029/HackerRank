# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

"""
Task

The number of tickets purchased by each student for the University X vs. University Y football game 
follows a distribution that has a mean of m = 2.4 and a standard deviation of s = 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
If there are only 250 tickets left, what is the probability that all 100 students will be able
to purchase tickets?

"""


# Cumulative Distribution Function for a function with normal distribution
def cdf(m, s, x):
    return 0.5 * (1 + math.erf((x-m) / (s * math.sqrt(2))))


x = 250
n = 100
m = 2.4
s = 2.0

"""
For large n, the distribution of sample sums S_n is close to normal distribution N(m', s') where:

    - m' = n * m
    - s' = n**0.5 * s
"""
m_p = n * m
s_p = n**0.5 * s

print(round(cdf(m_p, s_p, x), 4))
