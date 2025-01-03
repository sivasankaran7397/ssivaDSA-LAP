from queue import Queue
q=Queue(maxsize=3)
print(queue.qsize())
for i in range(3):
    element=input("enter the element: ")
    queue.put(element)
print("\n full: ",queue.full())
print("\n elements dequeue form the queue")
while not queue.empty():
    print(queue.get())
print("\n empty: ",queue.empty())
queue.put(1)
print("\n empty: ",queue.empty())
print("full:",queue.full())
