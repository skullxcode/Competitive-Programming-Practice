t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    ans = -1
    
    for i in range(32):
        res = n>>i
        if res==k:
            ans = i
            break
        if res+1 == k:
            if n%(2**i)>0:
                ans = i
                break
        if res<k:
            break
    print(ans)