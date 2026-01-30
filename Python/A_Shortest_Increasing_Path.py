t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if b==1 or a==b:
        print(-1)
    elif b>a:
        print(2)
    elif a>b:
        if a-1>b:
            print(3)
        else:
            print(-1)