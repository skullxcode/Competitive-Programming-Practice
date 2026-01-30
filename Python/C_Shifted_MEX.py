t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    s = sorted(set(arr))
    cnt = 0
    li = []
    for i in range(len(s)-1):
        if s[i+1]-s[i]==1:
            cnt+=1
        else:
            li.append(cnt)
            cnt=0
    li.append(cnt)
    print(max(li)+1)