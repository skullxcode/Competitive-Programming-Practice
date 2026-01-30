t = int(input())
for _ in range(t):
    n,h,l = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(n):
        if arr[i]>max(l,h):
            arr = arr[:i]
            break
    s = set()
    for i in range(len(arr)//2):
        if arr[i]<l and
        s.add((arr[i],arr[len(arr)-i-1]))
    print(len(s))