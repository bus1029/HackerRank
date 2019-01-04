# 3개의 경우에 대해서 Timeout이 발생. 루트n으로 줄이지 못한 것 같다.
"""
def is_prime(number):
    if number == 2:
        return True
    elif number == 1:
        return False

    start = 2
    i = 1

    # 절반으로 쪼갠 횟수만큼 반복
    # e.g., 0, 1, 2, 3, 4, 5, 6, 7
    # 소수인지를 판단하는 방법은
    # 0, 1, 7을 제외한 나머지 숫자들을 7과 나눠서 안나눠떨어지면 소수
    # (2, 6)을 같이 나누고
    # (3, 5)를 같이 나누고
    # 4를 마지막으로 나눠보는 방식
    # 그러면 7번 반복하는 식에서
    # 루트 7 반복하는 식으로 바뀐다고 생각합니다.
    for j in range(number//2):
        if number % start == 0 or number % (number-i) == 0:
            return False
        start += 1
        i += 1

    return True



n = int(input())

for i in range(n):
    number = int(input())

    print("Prime") if is_prime(number) else print("Not prime")
"""

# 2와 3으로 안나눠진다고 무조건 소수는 아니다...
"""
# 소수가 아닌 모든 수들은 2와 3으로 나눠지는데
# 소수들은 2와 3으로 나눠지지 않는다.

def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True

    if number % 2 != 0 and number % 3 != 0:
        return True

    return False

n = int(input())

for i in range(n):
    number = int(input())

    print("Prime") if is_prime(number) else print("Not prime")
"""


# n을 sqrt해서 나온 값까지 for문을 돌면서 나머지 Check를 하면
# 소수인지 아닌지가 판별된다.

def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


n = int(input())

for i in range(n):
    number = int(input())

    print("Prime") if is_prime(number) else print("Not prime")