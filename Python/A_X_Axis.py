t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    d = max(a)-min(a)
    print(d)