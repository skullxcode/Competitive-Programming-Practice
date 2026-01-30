t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = 0
    for i in range(n-2,-1,-1):
        while arr[i]>=arr[i+1]:
            ans+=1
            arr[i]//=2
            if arr[i]==0:
                break
        if arr[i]==0 and arr[i+1]==0:
            ans = -1
            break
            
    print(ans)        