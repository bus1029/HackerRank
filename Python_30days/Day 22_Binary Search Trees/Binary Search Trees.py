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

    def getHeight(self, root):
        #Write your code here
        # 끝까지 타고 들어가야 하기 때문에, 재귀적으로 접근해야 한다.
        if root:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        # 만약 자식 노드로 타고 들어갔는데, 자식 노드가 존재하지 않는다면
        # 해당 Edge부터 루트노드 까지의 Edge개수를 세어야 하기 때문에 -1을 리턴한다.
        # 그러면, 리프노드에선 return 값이 0부터 시작한다.
        else:
            return -1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)