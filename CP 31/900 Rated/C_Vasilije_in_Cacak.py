t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    ma = (n*(n+1))//2 - ((n-k)*(n-k+1))//2
    mi = (k*(k+1))//2
    if mi<=x<=ma:
        print("YES")
    else:
        print("NO")