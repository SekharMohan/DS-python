from ds_queue.queue import Queue

print("Queue using Linked List \n---------------------------------------------------")

n = int(input("Enter the no of element to insert into queue"))

print("Enter the elements:")
queue = Queue()
for x in range(0, n):
    queue.enqueue(input())

print("List the Queue elements: \n ----------------------------------------------------")

queue.listelementqueue()

print("Dequeue \n --------------")

queue.dequeue()

print("List of remaining queue elements: \n ---------------------------------------------")

queue.listelementqueue()