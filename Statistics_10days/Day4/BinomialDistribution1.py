# Enter your code here. Read input from STDIN. Print output to STDOUT

import operator as op
from functools import reduce

# Task
# The ratio of boys to girls for babies born in Russia is 1.09 : 1. If there is 1 child born per birth,
# what proportion of Russian families with exactly 7 children will have at least 3 boys?


def ncr(n, r):
    r = min(r, n-r)

    # reduce(function, iterable, initializer=None)
    # iterable이 만약 Empty면, initializer를 return

    # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
    # = ((((1+2)+3)+4)+5)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)

    return numer // denom


# Boy : Girl
boy, girl = list(map(float, input().split()))

# Boy Prob.
p = boy / (boy + girl)

# Girl Prob.
q = 1 - p
n = 6
total_prob = 0

# b(x>=3, 6, p)
for i in range(3, n+1):
    total_prob += ncr(n, i) * p**i * q**(n-i)

print(round(total_prob, 3))
