t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    brr = sorted(arr)
    ans = []
    for i in range(n):
        if arr[i]!=brr[i]:
            ans.append(arr[i])
    ans.sort()
    res = []
    if ans:
        L = brr[0]
        R = brr[-1]
        
        k = 10**12
        
        for x in ans:
            reach = max(x - L, R - x)
            if reach < k:
                k = reach
        print(k)
    else:
        print(-1)
