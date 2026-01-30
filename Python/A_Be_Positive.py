t = int(input())
for _ in range(t):
    n= int(input())
    a = list(map(int,input().split()))
    zero = a.count(0)
    one = a.count(-1)
    if one%2==0:
        print(zero)
    else:
        print(zero+2)