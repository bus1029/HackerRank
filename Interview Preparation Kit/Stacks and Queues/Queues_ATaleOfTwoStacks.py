class MyQueue(object):
    def __init__(self): # Queue
        self.queue = []

    def peek(self): # Print First Element in Queue
        return self.queue[0]

    def pop(self): # Return First Element in Queue(FIFO)
        return self.queue.pop(0)

    def put(self, value): # Put Element in Queue
        self.queue.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

