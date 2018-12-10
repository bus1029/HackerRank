# 각 값에 가중치를 줘서 평균을 구함

count = input()
numbers = list(map(int, input().strip().split(' ')))
weights = list(map(int, input().strip().split(' ')))

total = sum(list(number * weight for number, weight in zip(numbers, weights)))

print(round(total / sum(weights), 1))