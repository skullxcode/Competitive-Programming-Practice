t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(1,n-1):
        if arr[i-1]<arr[i]>arr[i+1]:
            ans = 1
            break
    if ans:
        print("YES")
        print(i,i+1,i+2)
    else:
        print("NO")