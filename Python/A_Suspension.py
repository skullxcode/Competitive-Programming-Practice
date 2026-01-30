t = int(input())
for _ in range(t):
    n = int(input())
    y,r = map(int,input().split())
    print(min(y//2+r,n))