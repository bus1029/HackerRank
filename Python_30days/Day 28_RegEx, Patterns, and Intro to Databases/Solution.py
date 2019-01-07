#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    name_list = []
    # $은 문자열의 마지막을 의미한다.
    # 예를 들어 정규식이 ^python인 경우 문자열의 처음은 항상 python으로 시작해야 매치되고,
    # 만약 정규식이 python$ 이라면 문자열의 마지막은 항상 python으로 끝나야 매치가 된다는 의미이다.
    pattern = re.compile(r"@gmail\.com$")

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        # 이 방법 말고도 정규표현식을 사용하는 방법도 있다
        name, email = emailID.split('@')

        if email == 'gmail.com':
            name_list.append(firstName)

        # Using RegEx
        # if pattern.search(emailID):
        #     name_list.append(firstName)


    name_list.sort()
    for name in name_list:
        print(name)