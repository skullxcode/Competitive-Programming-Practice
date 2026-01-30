n,k = map(int,input().split())
if n-k<1:
    print(-1)
else:
    a = []
    for i in range(1,k+2):
        a.append(i)
    if k+1<=n:
        for i in range(k+2,n+1,2):
            if i<n:
                a.append(i+1)
                a.append(i)
            else:
                a.append(i)
                a[0],a[-1]=a[-1],a[0]
    print(*a)
        
