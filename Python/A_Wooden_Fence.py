t = int(input())
for _ in range(t):
    n,x,y = map(int, input().split())
    if (n-1)//2 <= y and (n+1)//2 <= x:
        print("YES")
    else:
        print("NO")