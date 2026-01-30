t = int(input())
for _ in range(t):
    k,x = map(int,input().split())
    for i in range(k):
        if ((x-1)//3) % 2 == 1 and (x-1) % 3 == 0:
            x = (x-1)//3
        else:
            x = 2*x
    print(int(x))
    
