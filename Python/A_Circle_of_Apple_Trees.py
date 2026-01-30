t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int,input().split()))
    c = set(b)
    print(len(c))