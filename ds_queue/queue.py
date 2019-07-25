class Node:
    def __init__(self, data, node):
        self.data = data
        self.nextNode = node


class Queue:
    front = None
    rear = Node

    def enqueue(self, data):
        node = Node(data, self.rear)
        if self.rear is None:
            self.front = node
        self.rear = node

    def dequeue(self):
        if self.rear is not None:
            print(self.rear.data)

