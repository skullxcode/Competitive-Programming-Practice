n = int(input())
ans = 0
sa=0
sb=0
for _ in range(n):
    a,b = map(int,input().split())
    sa+=a
    sb+=b
print(abs(sa-sb))