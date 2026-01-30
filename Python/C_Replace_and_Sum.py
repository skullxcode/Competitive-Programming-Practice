t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    for i in range(n):
        if a[i]<b[i]:
            a[i]=b[i]
    
    for i in range(n-1,0,-1):
        if a[i]>a[i-1]:
            a[i-1]=a[i]
    
    pre = [0]
    
    for i in range(n):
        pre.append(pre[-1]+a[i])
    
    
    for _ in range(q):
        l,r = map(int,input().split())
        print(pre[r]-pre[l-1],end=" ")
    print()