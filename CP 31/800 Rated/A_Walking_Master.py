t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    if d<b:
        print(-1)
    else:
        y = abs(b-d)
        a+=y
        x = abs(a-c)
        if a<c:
            print(-1)
        else:
            print(y+x)