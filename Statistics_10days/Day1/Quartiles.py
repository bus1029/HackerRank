# Enter your code here. Read input from STDIN. Print output to STDOUT
"""

Interpreting Quartiles

The median is a measure of the 'central tendency' of the data but says
nothing about how the data is distributed in the two arms on either side of the
median. Quartiles help us measure this.

Thus, if the first quartile is far away from the median while the third quartile is closer to
it, it means that the data points that are smaller than the median are spread far apart
while the data points that are greater than the median are closely packed together.

"""

"""
IQR: Inter Quartile (Q3 - Q1)

The maximum difference in the test scores for the middle 50% of the data is xx.x points.
"""


def get_median(arr):
    # 짝수일 경우
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
    # 홀수일 경우
    else:
        return arr[len(arr)//2]


counts = input()
numbers = list(map(int, input().split()))
numbers.sort()

# Get Q2
q2 = int(get_median(numbers))

# Get Lower and Upper Part
l_part, u_part = [], []

for i in range(len(numbers) // 2):
    l_part.append(numbers[i])
    u_part.append(numbers[-1-i])

# for문 말고 if 문으로 길이 짝 / 홀 비교해서 바로 자르는 방법도 있다.
# q1 = get_median(numbers[:len(numbers)//2]
# if len(numbers) % 2 == 0:
#    q3 = get_median(numbers[len(numbers) // 2:])
# else:
#    q3 = get_median(numbers[len(numbers) // 2+1:])

# Get Q1 and Q3
q1 = int(get_median(l_part))
q3 = int(get_median(u_part))

print(q1)
print(q2)
print(q3)

