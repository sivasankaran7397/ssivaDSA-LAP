import heapq as hq
n = int(input('Enter the number of student : '))
list_stu = []
for _ in range(n):
    roll_no = int(input('Enter Roll number :'))
    name=input("enter the name: ") 

    list_stu.append((roll_no,name))
hq.heapify(list_stu)
print("The order of presentation is :")
for i in list_stu:
    print(i[0], ":" ,i[1])
