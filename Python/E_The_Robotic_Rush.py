t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    robot = list(map(int,input().split()))
    spike = list(map(int,input().split()))
    
    ins = input()
    robots = n
    for i in ins:
        if robots==0:
            break
        if i=="L":
            for j in range(n):
                robot[i]-=1
            for i in range()