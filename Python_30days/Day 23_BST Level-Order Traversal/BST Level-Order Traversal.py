import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        #Write your code here
        queue = []
        data_list = []
        current = root

        # 처음 루트노드를 큐에 집어넣어주고
        queue.append(current)

        while len(queue) > 0:
            # Dequeue First Element
            element = queue.pop(0)
            data_list.append(element.data)

            # 인접한 Node를 Queue에 집어넣어주기
            if element.left:
                queue.append(element.left)
            if element.right:
                queue.append(element.right)

        print(*data_list, sep=" ")


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
