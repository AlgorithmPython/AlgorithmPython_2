def zari(n):
    if len(n) == 1:
        d = int(n) + int(n[0])
    if len(n) == 2:
        d = int(n) + int(n[0])+ int(n[1])
    if len(n) == 3:
        d = int(n) + int(n[0])+ int(n[1])+ int(n[2])
    if len(n) == 4:
        d = int(n) + int(n[0])+ int(n[1])+ int(n[2])+ int(n[3])
    if d<10000:
        check_selfnum[d]=d
        
check_selfnum = [0]*10000

for i in range(10000):
    zari(str(i))
    
for i in range(1,10000):
    if check_selfnum[i]==0:
        print(i)