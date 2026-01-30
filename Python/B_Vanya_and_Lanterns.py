n,l = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
li = [a[0]-0]
for i in range(1,n):
    dist = (a[i]-a[i-1])/2
    li.append(dist)
li.append(l-a[-1])
print(round(max(li),10))
