# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
Task

Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for name is not found, print Not found instead.

"""

n = int(input())
p_book = {}

for i in range(n):
    name, phone = list(map(str, input().split()))
    p_book[name] = phone

for i in range(n):
    name = input()

    try:
        phone = p_book[name]
        print(name + "=" + phone)

    except KeyError:
        print("Not found")
