stack =[]
n= int(input("enter the size of the stack:"))
for i in range(n):
       element=input (f'enter the element{i+1}: ')
       stack.append(element)
print("initial stack")
print(stack)
print("\n element popped form stack: ")
while stack:       
    print(stack.pop())
print('\n stack after elements are popped')
print(stack)
