t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if len(set(a))==1:
        print(-1)
    else:
        a.sort()
        k = a.index(a[-1])
        b = a[:k]
        c = a[k:]
        print(len(b),len(c))
        print(*b)
        print(*c)