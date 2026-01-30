n,q = map(int,input().split())
p = list(map(int,input().split()))
p.sort(reverse=True)
for _ in range(q):
    x,y = map(int,input().split())
    l1 = p[0:x]
    l1.sort()
    sum_ = sum(l1[0:y])
    print(sum_)