n,k = map(int,input().split())
a = list(map(int,input().split()))
if k%2==0:
    print(*a[k//2:-k//2])
else:
    s = reversed(a[k//2+1:-k//2+1])
    print(*(s))