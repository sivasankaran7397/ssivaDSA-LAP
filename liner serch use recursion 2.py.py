l= [2,4,6,8,10,3,999,9,88,44,17,55,44,67,4]
x=int(input("enter the value: "))
i=0  
while i<len(l):
    if l[i]==x:
        print(f'element {x} present at {i}th position')
        break
    i+=1
if i>=len(l):
    print('Element is not present')

