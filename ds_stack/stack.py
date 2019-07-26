import array
class Node:
    def __init__(self, d, node):
        self.data = d
        self.nextNode = node


class StackLinkedList:
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

class StackArray:
    data = []
    top = -1

    def push(self, data):
        self.top = self.top+1
        self.data.insert(self.top, data)


    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.data.pop(self.top)
            self.top = self.top-1

    def isempty(self):
        return self.top == -1

    def listofelement(self):
        for value in self.data:
            print(value)


class Switcher:
    def stack_type(self, option):
        switcher = {
            1:
            self._stack_linked_list(),
            2:
            self._stack_array()


        }
        return switcher.get(option)

    def _stack_linked_list(self):
        print("Stack - Linked List ------------->")
        n = int(input("Enter the no of element to insert into stack"))
        print("enter element to insert:")
        stackElement = StackLinkedList()
        for i in range(0, n):
            stackElement.push(input())

        print("list all element in stack\n--------------------------------------------")
        stackElement.listElement()
        print("pop operation")
        stackElement.pop()
        print("list all element in stack\n--------------------------------------------")
        stackElement.listElement()

    def _stack_array(self):
         print("Stack - Array -------------->")
         n = int(input("Enter the no of element to insert into stack"))
         stackArrar = StackArray()
         print("enter element to insert:")
         for i in range(0, n):
             stackArrar.push(input())
         print("list all element in stack\n--------------------------------------------")

         stackArrar.listofelement()

         print("Pop operation:")
         stackArrar.pop()

         print("list all element in stack\n--------------------------------------------")

         stackArrar.listofelement()










