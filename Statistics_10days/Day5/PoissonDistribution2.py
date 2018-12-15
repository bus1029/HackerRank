# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

# Task
# The manager of a industrial plant is planning to buy a machine type A or type B.
# For each day's operation:
# The number of repairs, X, that machine A needed is a Poisson random variable with mean 0.88.
# The daily cost of operating
# A is Ca = 160 + 40X**2.
# The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55.
# The daily cost of operating
# B is Cb = 128 + 40Y**2.
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly
# to ensure that they operate like new at the start of each day.
# Find and print the expected daily cost for each machine.

"""
Special Case
Consider some Poisson random variable, X. Let E[X] be the expectation of X. Find the value of E[X**2].

Let Var(X) be the variance of X. Recall that if a random variable has a Poisson distribution, then:

- E[X] = l(lambda)
- Var(X) = l

Now, we'll use the following property of expectation and variance for any random variable, X:

    Var(X) = E[X**2] - (E[X])**2
    => E[X**2] = Var(X) + (E[X])**2

So, for any random variable X having a Poisson distribution, the above result can be rewritten as:
    => E[X**2] = l + l**2
"""


def special_poisson(l):
    return l + l**2


mean_a, mean_b = list(map(float, input().split()))

cost_a = round(160 + (40 * special_poisson(mean_a)), 3)
cost_b = round(128 + (40 * special_poisson(mean_b)), 3)

print(cost_a)
print(cost_b)

