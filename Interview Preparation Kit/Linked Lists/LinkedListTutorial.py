# Node 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List 클래스 정의
class LinkedList:
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    # Append 메소드 (insert, 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    # Delete 메소드 (delete, current 노드 삭제, 인접 노드의 current, next 변경, 데이터 개수 변경)
    def delete(self):
        pop_data = self.current.data

        # 삭제할 노드가 가장 뒷 노드라면
        # 현재 노드의 바로 전 노드를 tail로 지정한다
        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        # Current가 next가 아닌 before로 변경됨
        self.current = self.before

        # Before도 Current의 전으로 옮겨야지
        if self.current.data == 'dummy':
            self.before = self.head
        else:
            self.before = self.head

            while True:
                if self.before.next.data == self.current.data:
                    break
                else:
                    self.before = self.before.next

        self.num_of_data -= 1

        return pop_data

    # First 메소드(search1, 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        if self.num_of_data == 0:
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current.data


    # next 메소드 (search2, current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되여야 함)
    def next(self):
        if self.current.next == None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data


    def size(self):
        return self.num_of_data


if __name__ == "__main__":
    l_list = LinkedList()
    l_list.append(5)
    l_list.append(2)
    l_list.append(1)
    l_list.append(2)
    l_list.append(7)
    l_list.append(2)
    l_list.append(11)

    print('first :', l_list.first())  # first : 5
    print('next :', l_list.next())  # next : 2
    print('size :', l_list.size())  # size : 7
    print('delete :', l_list.delete())  # delete : 2
    print('before:', l_list.before.data)  # before: 5
    print('size :', l_list.size())  # size : 6
    print('current:', l_list.current.data)  # current: 5
    # print('before:', l_list.before.data)  # before: 5
    print('delete :', l_list.delete())  # delete : 5
    print('before:', l_list.before.data)  # before:
    print('tail:', l_list.tail.data)  # tail: 11
    print('first :', l_list.first())  # first : 5
    print('next :', l_list.next())  # next : 1
    print('next :', l_list.next())  # next : 2
    print('next :', l_list.next())  # next : 7