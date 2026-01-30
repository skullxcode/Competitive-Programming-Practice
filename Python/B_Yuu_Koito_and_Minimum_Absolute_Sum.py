t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    sum_ = 0
    if a[-1]==-1 and a[0]==-1:
        a[-1]=0
        a[0]=0
    if a[-1]==-1:
        a[-1]=a[0]
    if a[0]==-1:
        a[0]=a[-1]
    for i in range(n):
            if a[i]==-1:
                a[i]=0
    for i in range(n-1):
        sum_+=a[i+1]-a[i]
    print(abs(sum_))
    print(*a)