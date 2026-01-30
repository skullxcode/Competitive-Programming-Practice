t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = max(a)
    s = k
    b = [False]*n
    b[a.index(k)]=True
    next = a.index(k)
    for i in range(n-1):
        if i%2==1:
            if b[next]==False:
                s+=a[next]
                temp = a[next]
                next = temp
                b[next]=True
                a[next] = 0
            else:
                s+=max(a)
                k = max(a)
                next = a.index(k)
                temp = a[next]
                next = temp
                b[next]=True
                a[next] = 0
        else:
            if b[next]==False:
                s-=a[next]
                temp = a[next]
                next = temp
                b[next]=True
                a[next] = 0
            else:
                s-=max(a)
                k = max(a)
                next = a.index(k)
                temp = a[next]
                next = temp
                b[next]=True
                a[next] = 0
    print(s)