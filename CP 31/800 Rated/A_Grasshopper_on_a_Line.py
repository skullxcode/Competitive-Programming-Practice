t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a<b or a%b!=0:
        print(1)
        print(a)
    else:
        print(2)
        print(a-1,1)