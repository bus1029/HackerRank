import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def depthOrder(self, root):
        # Write your code here
        current = root
        data_list = []
        stack = []

        stack.append(current)

        while len(stack) > 0:
            element = stack.pop(-1)
            data_list.append(element.data)

            # 인접한 Node들을 찾음
            if element.right:
                stack.append(element.right)
            if element.left:
                stack.append(element.left)

        print(*data_list, sep=' ')


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.depthOrder(root)
