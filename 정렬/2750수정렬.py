list = []
a = int(input())
for i in range(a):
    num = int(input())
    list.append(num)
for j in range(a):
    for k in range(a-1):
        if list[k]>list[k+1]:
            temp = list[k]
            list[k] = list[k+1]
            list[k+1] = temp
for i in range(a):
    print(list[i])