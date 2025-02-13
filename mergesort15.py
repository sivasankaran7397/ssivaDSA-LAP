def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    merged=[]
    i=j=0
    while i<len(left)and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged+=left[i:]
    merged+=right[j:]
    return merged
arr=[]
n=int(input("Enter a size:"))
for i in range(n):
      arr.append(int(input("Enter a element:")))
print("Before sorting:",arr)
sort=merge_sort(arr)
print("After sorting:",sort)
