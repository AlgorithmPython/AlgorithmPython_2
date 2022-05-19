num = int(input())
list1 = []
list2 = []
sum = 0
list1  = list(map(int,input().split()))
for i in range(num):
    for j in range(num-1):
        if list1[j]>list1[j+1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
for i in range(num):
    sum = sum + list1[i]
    list2.append(sum)
for i in range(num-1):
    sum = sum +list2[i]
print(sum)