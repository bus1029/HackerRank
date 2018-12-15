# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

"""
Task
In a certain plant, the time taken to assemble a car is random variable, X,
having a normal distribution with a mean of 20 hours and standard deviation of 2 hours.
What is the probability that a car can be assembled at this plant in:

1. Less than 19.5 hours?

2. Between 20 and 22 hours?

"""

# Cumulative Distribution Function for a function with normal distribution
def cdf(m, s, x):
    return 0.5 * (1 + math.erf((x-m) / (s * math.sqrt(2))))

mean, std = 20, 2

# less than 19.5
print(round(cdf(mean, std, 19.5), 3))
# between 20 and 22
print(round(cdf(mean, std, 22) - cdf(mean, std, 20), 3))
