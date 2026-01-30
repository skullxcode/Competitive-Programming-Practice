t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if sorted(a)!=a:
        print(0)
    else:
        diff = 10**18
        for i in range(1,n):
            diff = min(diff,a[i]-a[i-1])
        print(diff//2+1)