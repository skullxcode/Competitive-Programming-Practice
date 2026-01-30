t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    xor = 0
    for i in a:
        xor^=i
    if n%2==1 or (n%2==0 and xor==0):
        print(xor)
    else:
       print(-1)