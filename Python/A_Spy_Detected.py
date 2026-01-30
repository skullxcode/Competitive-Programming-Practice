t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    k = False
    t = sorted(a)
    if t[0]==t[1]:
        j = t[-1]
    else:
        j = t[0]
    for i in range(n):
        if a[i]==j:
            print(i+1)
            break