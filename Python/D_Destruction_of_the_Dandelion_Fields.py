t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    odd_min = 0
    for i in range(n):
        if a[i]%2==1:
            b.append(a[i]) 
    k = len(b)
    if len(b)==0:
        print(0)
    elif len(b)%2==1 :
        add=0
        for j in range(k,((k//2)-1),-1):
            add+=b[j]
        print(sum(a)-sum(b)+add)
    else:
        odd_min = min(b)
        total = sum(a)-odd_min
        print(total)