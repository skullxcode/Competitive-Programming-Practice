t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    net = 0
    while True:
        l = len(a)
        min_ = min(c)
        ind = c.index(min_)
        net+=min_*sum(a[ind:])
        c = c[:ind]
        a = a[:ind]
        if len(a)==0:
            break
    print(net)