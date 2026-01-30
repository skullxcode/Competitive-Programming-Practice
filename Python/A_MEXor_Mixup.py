t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    m = 0
    if (a-1)%4==0:
        m = a-1
    elif (a-1)%4==1:
        m = 1
    elif (a-1)%4==2:
        m = a
    else:
        m = 0
    x = m^b
    if x==0:
        print(a)
    elif x==a:
        print(a+2)
    else:
        print(a+1)
