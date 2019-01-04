class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        # Write your code here
        # 중복을 제거할 때,
        # 1. 링크드리스트에서 데이터를 다 뽑는다.
        # 2. 리스트에 옮긴 후, 리스트에서 중복을 제거한다.
        # 3. 제거된 데이터를 다시 링크드리스트로 만든다.

        # 1. Extract Data in Linked List and remove duplicates
        data = []
        duplicate_map = {}

        while head:
            try:
                # 여기서 +=1을 해줘서 KeyError로 간다.
                # =1로 하면 배정해주는 것이기 때문에 KeyError로 가지 않는다.
                duplicate_map[head.data] += 1
            except KeyError:
                # Key Error가 떴다는건 중복이 아니라는 의미
                duplicate_map[head.data] = 1
                data.append(head.data)
            finally:
                # Exception 여부와 상관없이 무조건 head는 다음으로 진행
                head = head.next

        # 2. Make Linked List
        new_head = None

        for i in range(len(data)):
            new_head = self.insert(new_head, data[i])

        return new_head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head);