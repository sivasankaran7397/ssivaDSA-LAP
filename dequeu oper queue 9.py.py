from collections import deque
queue=deque()
n=int(input("enter the size of the queue: "))
for i in range(n):
    element=input(f'enter the element{i+1}: ')
    queue.append(element)
print('initial quene')
print(queue)
print("\n element dequend form the queue")
while queue:
    print(queue.popleft())
print('\n Queue after removing elements')
print(queue)
