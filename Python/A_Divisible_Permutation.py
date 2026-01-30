t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0]*n
    cnt = 1
    cntl = n
    for i in range(n-1,-1,-2):
        arr[i]=cnt
        cnt+=1
    for i in range(n-2,-1,-2):
        arr[i]=cntl
        cntl-=1
    print(*arr)