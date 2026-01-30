t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ind = arr.index(max(arr))
    if ind != 0:
        print(*arr[ind::-1],*arr[ind+1:])
    else:
        rev = [arr[0]] + arr[:0:-1]
        if rev > arr:
            ans = rev
        else:
            ans = arr
        print(*ans)