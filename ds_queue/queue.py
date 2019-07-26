class Node:
    def __init__(self, data, node):
        self.data = data
        self.nextNode = node


class Queue:
    front = None
    rear = None

    def enqueue(self, data):
        node = Node(data, None)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.nextNode = node
            self.rear = node

    def dequeue(self):

        if self.isempty():
            print("Queue is empty")
        else:
            temp = self.front.nextNode
            self.front = None
            self.front = temp

    def listelementqueue(self):
        searchQueue = self.front
        while searchQueue is not None:
            print(searchQueue.data)
            searchQueue = searchQueue.nextNode

    def isempty(self):
        return  self.rear is None

