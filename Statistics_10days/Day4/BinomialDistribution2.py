# Enter your code here. Read input from STDIN. Print output to STDOUT

import operator as op
from functools import reduce

# Task
# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are
# rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:
# 1. No more than 2 rejects?
# 2. At least 2 rejects?


def ncr(n, r):
    r = min(r, n-r)

    # reduce(function, iterable, initializer=None)
    # iterable이 만약 Empty면, initializer를 return

    # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    # = ((((1+2)+3)+4)+5)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)

    return numer // denom


# Reject Prob, Batch Size
prob, batch = list(map(int, input().split()))
prob = prob / 100

# No more than 2 rejects (0, 1, 2)
more_than_prob = 0

# b(x < 2, n, p)
for i in range(0, 2+1):
    more_than_prob += ncr(batch, i) * prob ** i * (1-prob) ** (batch-i)

# At least 2 rejects
at_least_prob = 0

# b(x >= 2, n, p)
for i in range(2, batch+1):
    at_least_prob += ncr(batch, i) * prob ** i * (1-prob) ** (batch-i)

print(round(more_than_prob, 3))
print(round(at_least_prob, 3))
