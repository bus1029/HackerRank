# Enter your code here. Read input from STDIN. Print output to STDOUT

# Task
# The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect
# is found during the 5th inspection?

numer, denom = list(map(int, input().split()))
inspect = int(input())

p = numer / denom

print(round((1-p) ** (inspect-1) * p, 3))

