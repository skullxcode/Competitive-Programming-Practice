t = int(input())
for _ in range(t):
    start,n = map(int,input().split())
    left = (n*(n+1)//2)-((n//2)*((n//2)+1)//2)
    right = ((n//2)*((n//2)+1)//2)