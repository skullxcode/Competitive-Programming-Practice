t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a==b:
        print(0)
    else:
        k = abs(a-b)
        x = k//10
        if k%10==0:
            print(x)
        else:
            print(x+1)