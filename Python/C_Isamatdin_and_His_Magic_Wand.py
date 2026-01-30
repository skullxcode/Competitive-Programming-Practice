t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    odd = len([x for x in a if x%2==0])
    even = len([x for x in a if x%2==1])
    if even and odd:
        b = sorted(a)
        print(*b)
    else:
        print(*a)