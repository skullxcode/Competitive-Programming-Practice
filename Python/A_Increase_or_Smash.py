t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = len(set(a))
    count = 2*c -1
    print(count)