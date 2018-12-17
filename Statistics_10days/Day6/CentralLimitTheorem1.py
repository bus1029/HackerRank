# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

"""
Task

A large elevator can transport a maximum 9800 pounds. Suppose a load of cargo containing 49 boxes must
be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean
of m = 205 pounds and a standard deviation of s = 15 pounds. Based on this information, what is the probability
that all 49 boxes can be safely loaded into to freight elevator and transported?

"""


# Cumulative Distribution Function for a function with normal distribution
def cdf(m, s, x):
    return 0.5 * (1 + math.erf((x-m) / (s * math.sqrt(2))))


max_w = 9800
n_box = 49
m = 205
sd = 15

"""
For large n, the distribution of sample sums Sn is close to normal distribution N(m', s') where:

    - m' = n * m
    - s' = n**0.5 * s
"""

m_prime = n_box * m
s_prime = n_box**0.5 * sd

print(round(cdf(m_prime, s_prime, max_w), 4))
