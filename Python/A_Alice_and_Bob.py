t = int(input())
for i in range(t):
    n,a = map(int,input().split())
    l = list(map(int,input().split()))
    more = 0
    less = 0
    for i in l:
        if i>a:
            more+=1
        elif i<a:
            less+=1
    if less<=more:
        print(a+1)
    else:
        print(a-1)