# Enter your code here. Read input from STDIN. Print output to STDOUT

# Task
# The probability that machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the first 5 inspections?

# 첫 5개 검사에서 첫 번째 결함이 발견될 확률은 얼마입니까?
# # => 첫 5개의 검사에서 최소 하나의 결함이 발견될 확률은 얼마입니까?
# 첫 번째에서 발견될 확률 + 두 번째에서 발견될 확률 + 세 번째에서 발견될 확률 + 네 번째에서 발견될 확률 + 다섯 번째에서...

numer, denom = list(map(int, input().split()))
inspect = int(input())
px = numer / denom

print(round(sum([((1-px)**(i-1))*px for i in range(1, inspect+1)]), 3))

# 혹은
