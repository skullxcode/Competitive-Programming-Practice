t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(set(a))
    b.sort()
    c = []
    for i in b:
        c.append(a.count(i))
    c.sort()
    k = len(c)
    d = []
    for j in range(len(c)):
        d.append(c[j]*(k-j))
    d.sort()
    print(d[-1])