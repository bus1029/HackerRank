import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    # Implement Stack
    # First In -> Last Out
    """
    w: the specific character
    """
    def pushCharacter(self, w):
        self.stack.append(w)

    def popCharacter(self):
        # pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소를 삭제하는 함수
        return self.stack.pop()

    # Implement Queue
    # First In -> First Out
    """
    w: the specific character
    """
    def enqueueCharacter(self, w):
        self.queue.append(w)

    def dequeueCharacter(self):
        # pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소를 삭제
        return self.queue.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")