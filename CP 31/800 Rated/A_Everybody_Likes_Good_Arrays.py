t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    li = []
    cnt = 0
    for i in range(n-1):
        if a[i]%2==a[i+1]%2:
            cnt+=1
    print(cnt)