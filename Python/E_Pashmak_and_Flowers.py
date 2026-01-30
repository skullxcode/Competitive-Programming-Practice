n = int(input())
a = list(map(int,input().split()))
if len(set(a))==1:
    
    print(0,n*(n-1)//2)
else:
    min_ = max(a)-min(a)
    x = a.count(max(a))
    y = a.count(min(a))
    ans = x*y
    print(min_ , ans)
