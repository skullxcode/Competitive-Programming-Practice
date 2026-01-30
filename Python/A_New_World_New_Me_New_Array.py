t = int(input())
for _ in range(t):
    n,k,p = map(int,input().split())
    if k<0 or k%p==0:
        m = abs(k//p)
    else:
        m = k//p + 1
    if m<=n:
        print(m)
    else:
        print(-1)