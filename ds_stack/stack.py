class Node:
    def __init__(self, d, node):
        self.data = d
        self.nextNode = node


class Stack:
    head = None

#Stack ------------------> PUSH
    def push(self, d):
        node = Node(d, self.head)
        self.head = node
#Stack --------------->
    def listElement(self):
        searchNode = self.head
        while searchNode is not None:
            print(searchNode.data+"\n")
            searchNode = searchNode.nextNode

#Stack -------------> Pop
    def pop(self):
        if self.head is not None:
            print(self.head.data + " is poped from stack")
            node = self.head.nextNode
            self.head = None
            self.head = node
        else:
            print("No more element to pop")







