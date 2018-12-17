# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Task

You have a sample of 100 values from a population with mean m = 500 and with standard deviation s = 80.
Compute the interval that covers the middle 95% of the distribution of the sample mean;
in other words, compute A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96.

"""

"""
The z-score is a factor telling you with what probability you land in an interval of z standard deviations away 
from the mean (in both directions) e.g.:

- with probability 68% you are 1 sd away from the mean (z-score = 1)

- with probability 95% you are within 2 sd from the mean

- with probability 99.7% you are within 3 sd ...

this is called the 68 95 99.7 rule. (google it for meaningful illustrations).

Now the author tells us to take 1.96 as z-score instead of 2 because 1.96 is a more exact z-value for 95%, 
coming from a z-table or inverse PDF function.

if you read the question carefully, you will notice he tells you the population mean and population standard deviation 
but asks you for the interval on the sample.

So you need to convert the population standard deviation into the sample standard deviation 
by dividing it by the square-root of the sample size (sqrt(100) = 10).

Further you need to know that the mean of the sample is the mean of the population.

Since you get the z-value your lower limit of the interval is mean - z_score * sd_sample, 
the upper limit is symmetrical.

There a good tutorial on Kahn university and the MIT OCW has a wonderful course on probability.
"""
n = 100
m = 500
sd = 80
d_ptg = 0.95
z = 1.96


# mean_sample = mean_population, and sd_sample = sd_population / sqrt(n)
s_sd = sd / n**0.5  # Sample standard deviation
moe = s_sd * z  # Margin of Error

print(round(m-moe, 2))
print(round(m+moe, 2))
