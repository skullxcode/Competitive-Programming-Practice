t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    k = max(a,b)
    y = []
    for i in range(1,k+1):
        if a % i == 0 and b % i == 0:
            y.append(int(a*i + b/i))
    m = list(sorted(y))
    if m[0] % 2 == 0:
        print(m[0])
    else:
        print(-1)