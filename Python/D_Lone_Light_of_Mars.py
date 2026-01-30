n = int(input())
x = list(map(int,input().split()))
x.sort()
a = []
if n%2==1:
    mid = n//2
else:
    mid = n//2-1
for i in range(n-mid):
    k = (x[i]+x[mid+i])//2
    l = k - x[i]
    r = x[mid+i]-k
    a.append(max(l,r))
print(min(a))