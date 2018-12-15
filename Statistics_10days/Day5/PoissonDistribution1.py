# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

# Task
# A Random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with
# which the random variable X is equal to 5.

# l
mean = float(input())
# k
var = float(input())

# P(k, l) = l**k * exp(-l) / k!
prob = mean ** var * math.exp(-mean) / math.factorial(var)

print(round(prob, 3))
