n = int(input())
a = list(map(int,input().split()))
if n == 1:
    if a[0]==1:
        print(0)
    else:
        print(1)
elif n==2:
    if set(a)[0]==1:
        print(0)
    else:
        print(2)
else:
    li = []
    cnt = 0
    for i in range(len(a)):
        if a[i]==0:
            cnt+=1
        else:
            li.append(cnt)
            cnt = 0
    li.append(cnt)
    print(max(li)+2)