t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    ans=0
    i = 0
    while k>0:
        if (k&1)==1:
            ans+=n**i
        k>>=1
        i+=1
    ans = ans%(10**9+7)
    print(ans)
