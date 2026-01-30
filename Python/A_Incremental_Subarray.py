t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if a[0]==1:
        k = max(a)
        if m>k:
            print(1)
        else:
            print(n-m+1)
    elif m==1:
        print(n-a[0]+1)
    else:
        print(1) 