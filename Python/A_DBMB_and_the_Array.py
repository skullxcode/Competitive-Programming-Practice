t = int(input())
for _ in range(t):
    n,s,x = map(int,input().split())
    arr = list(map(int,input().split()))
    k = sum(arr)
    if k>s:
        print("NO")
    elif (s-k)%x==0:
        print("YES")
    else:
        print("NO")