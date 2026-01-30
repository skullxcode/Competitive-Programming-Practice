n = int(input())
a = list(map(int,input().split()))
a.sort()
s = sum(a)
if s%n==0:
    s = s//n
else:
    s = s//n + 1
l = 0 
for i in range(n//2+1):
    if a[n-i-1]>s:
        temp = a[n-i-1]
        a[n-i-1]=s
        a[i] += temp-s
odd = 0
even = 0
a.sort()
for i in range(len(a)-1):
    if a[i]!=a[i+1] and a[i]%2==1:
        odd+=1
if a[-1]%2==1:
    odd+=1
if odd%2==0:
    print(max(a))
else:
    ans = 0
    for i in range(n):
        ans|=a[i]
    print(ans)