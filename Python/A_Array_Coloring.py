t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = {}
    for i in range(0,n,2):
        freq[arr[i]]=freq.get(arr[i],"R")
    for i in range(1,n,2):
        freq[arr[i]]=freq.get(arr[i],"B")
    arr.sort()
    f = 1
    for i in range(n-1):
        if freq[arr[i]]==freq[arr[i+1]]:
            f = 0
    if f:
        print("YES")
    else:
        print("NO")