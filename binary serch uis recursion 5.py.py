def binary_search(L, key, low, high):
    if high >= low:
        mid = (low + high) // 2
        if key == L[mid]:
            return mid
        elif key > L[mid]:
            return binary_search(L, key, mid + 1, high)
        else:
            return binary_search(L, key, low, mid - 1)
    else:
        return -1
L = [11, 22, 33, 44, 55, 66, 77]
key = int(input("enter the element: "))
idx = binary_search(L, key, 0, len(L) - 1)
if idx!=-1:
        print(f'In list {L} the key {key} lies on index : {idx} ')
else:
	print("The element is not present in array")

