t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [0]*n
    cnt = n
    ans = 0
    for i in range(n):
        if a[i]==0:
            prefix[i]=1
            cnt-=1
    if cnt==0:
        print(0)
    elif n==1:
        print(1)
    else:
        for i in range(n-1):
            if prefix[i]==1 and prefix[i+1]==0:
                ans+=1
        print(ans)
    
