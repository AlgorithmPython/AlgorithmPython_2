num = (input())
han = 0
num = int(num)
if(num<100):
    han = num
else:
    han = 99
    for i in range(100,num+1):
        i = str(i)
        if (int(i[1]) - int(i[0])) == (int(i[2]) - int(i[1])):
            han = han +1
print(han)
    