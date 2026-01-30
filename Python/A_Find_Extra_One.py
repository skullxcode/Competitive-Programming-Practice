n = int(input())
l = []
for _ in range(n):
    a,b = map(int,input().split())
    if a!=0:
        k = a//abs(a)
        l.append(k)
if l.count(-1)<=1 or l.count(1)<=1:
    print("Yes")
else:
    print("No")
    