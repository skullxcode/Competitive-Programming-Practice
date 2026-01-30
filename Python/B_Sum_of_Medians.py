t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = (n*k - n//2 - 1)
    d = n//2+1
    sum_ = 0
    for i in range(k):
        sum_ += a[m]
        m-=d
    print(sum_)