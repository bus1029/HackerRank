import math

"""

The Standard Deviation is a measure of how spread out numbers are.

it is the square root of the Variance.

Variance is defined as:
    The average of the squared differences from the Mean.

Although both standard deviations measure variability, there are differences between
a population and a sample standard deviation. The first has to do with the distinction
between statistics and parameters.

The population standard deviation is a parameter, which is a fixed value calculated from
every individual in the population.

A sample standard deviation is a statistic. This means that it is calculated from only
some of the individuals in a population.

Since the sample standard deviation depends upon the sample, it has greater variability.
Thus, the standard deviation of the sample is greater than that of the population.

Now the calculation of these standard deviations differs:

If we are calculating the population standard deviation, then we divide by n, the number of data values.
If we are calculating the sample standard deviation, then we divide by n -1, one less than the number of data values.

The final step, in either of the two cases that we are considering,
is to take the square root of the quotient from the previous step.

The larger the value of n is, the closer that the population and sample standard deviations will be

"""

counts = input()
nums = list(map(int, input().split()))

avg = sum(list(num for num in nums)) / len(nums)
variance = sum(list((num-avg) ** 2 for num in nums)) / len(nums)
sd = round(math.sqrt(variance), 1)

print(sd)
