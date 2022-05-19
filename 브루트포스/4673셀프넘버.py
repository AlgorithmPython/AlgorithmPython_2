num = 0
list1 = [i for i in range(1,10001)]
list2 = [0 for _ in range (1,10001)]
for i in range(10000):
    num = 0
    for j in str(i):
        num = num + int(j)
    num = num + i
    if num<10000:
        list2[num-1] = 1
for i in range(10000):
    if list2[i] == 0:
        print(list1[i])

# list1 = [i for i in range(1,10001)]
# list2 = [0 for _ in range (1,10001)]
# num = 0
# for i in range(0,10001):
#     num = 0
#     for j in str(i):
#         num = num + int(j)
#     num = num + i
#     if num<10000:
#         list2[num-1] = num
        
    
# for i in range(10000):
#     if list2[i] == 0:
#         print(list1[i])

# num = 0
# a = int(input())
# for i in str(a):
#     num = num+ int(i)
# num = num + a
# print (num)