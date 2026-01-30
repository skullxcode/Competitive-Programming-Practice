n,m = map(int,input().split())
x = list(map(int,input().split()))
ans = 0
for i in range(m):
    a,b = map(int,input().split())
    ans+=min(x[a-1],x[b-1])
print(ans)