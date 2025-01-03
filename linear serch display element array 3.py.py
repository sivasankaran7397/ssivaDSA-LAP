def linear_search(L, key, i):
    if i >= len(L):
        return -1
    if L[i] == key:
        return i
    return linear_search(L, key, i + 1)
L = [1, 2, 3, 4, 5, 6, 7, 22, 33, 44, 55, 66, 77, 88 ,99, 100, 33]
key = int(input ("enter the number: "))
x = linear_search(L, key, 0)
print('List : ', L)
print(f'Element {key} is available on index : {x}')
    
 

