t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    f = []
    k=0
    for i in range(n):
        for j in range(i):
            if a[i]>=a[j]:
                k+=1
                f.append(str(i+1))
                break
    sep = " "
    ans = sep.join(f)
    print(k)
    print(ans)