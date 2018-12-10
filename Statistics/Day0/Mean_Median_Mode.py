import numpy as np
from collections import Counter
from scipy import stats

counts = input()
numbers = list(map(int, input().split()))

# To get the smallest number in array
numbers.sort()

data = Counter(numbers)

# Get the highest occurring item
number, count = data.most_common(1)[0]

# Mean
print(np.mean(numbers))
# Median
print(np.median(numbers))
# Mode
# print(number)

# Useful solution...
print(int(stats.mode(numbers)[0]))
