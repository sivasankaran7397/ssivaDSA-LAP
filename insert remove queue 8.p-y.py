queue = []
n=int(input("enter the size of the queue"))
for i in range(n):
    element=input(f'enter the element{i+1}: ')
    queue.append(element)
print("intial queue")
print(queue)
print("\n element dequeued form queue: ")
while queue:
    print(queue.pop(0))
print("\n queue after removing element")
print(queue)
