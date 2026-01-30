t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    dist = []
    prev = 0
    for i in range(n):
        dist.append(a[i]-prev)
        prev = a[i]
    dist.append(2*(x-a[-1]))
    print(max(dist))