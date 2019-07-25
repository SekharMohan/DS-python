from ds_stack.stack import Stack

print("Stack------------->")

n = int(input("Enter the no of element to insert into stack"))
print("enter element to insert:")
stackElement = Stack()
for i in range(0, n):
    stackElement.push(input())

print("list all element in stack\n--------------------------------------------")
stackElement.listElement()
print("pop operation")
stackElement.pop()