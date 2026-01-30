n,m = map(int,input().split())
a = list(map(int,input().split()))
b = []
for i in range(n):
    if a[i]%m==0:
        k = a[i]//m
    else:
        k = a[i]//m + 1
    b.append(k)
l = max(b)
c = [i for i, val in enumerate(b) if val == l]
print(c[-1]+1)