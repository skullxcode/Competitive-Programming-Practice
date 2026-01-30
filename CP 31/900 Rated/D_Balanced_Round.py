t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    if n==1:
        print(0)
        continue
    arr.sort()
    cnt = 1
    li = []
    for i in range(n-1):
        if arr[i+1]-arr[i]<=k:
            cnt+=1
        else:
            li.append(cnt)
            cnt = 1
    li.append(cnt)  
    print(n-max(li))
        