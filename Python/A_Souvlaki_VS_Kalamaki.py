t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = True
    a.sort()
    if n%2==0:
        for i in range(1,n-1,2):
            if a[i]!=a[i+1]:
                ans = False
                break
    else:
        for i in range(1,n,2):
            if a[i]!=a[i+1]:
                ans = False
                break
    if ans:
        print("YES")
    else:
        print("NO")