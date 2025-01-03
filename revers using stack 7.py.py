from collections import deque
stack = deque()
num=int(input("enter the size of the stack: "))
for i in range(num):
    element=input(f'enter the element{i+1}: ')
    stack.append(element)
print("initial stack: ")
while stack:
    print(stack.pop())
print("\n stack after element are popped: ")
print(stack)
