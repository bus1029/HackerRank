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


def quartiles(n, arr):
    q2 = get_median(arr)
    q1 = get_median(arr[:n//2])

    if n % 2 == 0:
        q3 = get_median(arr[n//2:])
    else:
        q3 = get_median(arr[n//2+1:])

    return q1, q2, q3


counts = input()
numbers = list(map(int, input().split()))
freqs = list(map(int, input().split()))

freq_array = []

# Make Frequency Array
for num, freq in zip(numbers, freqs):
    for i in range(freq):
        freq_array.append(num)

# 좀 더 Pythonic 한 방법은
# for i in range(counts):
#   freq_array += [numbers[i]] * freqs[i]

freq_array.sort()

q1, q2, q3 = quartiles(len(freq_array), freq_array)

print(float(round(q3-q1, 1)))
