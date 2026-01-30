t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n

    for i in range(n):
        b[i] = n-a[i]+1
        
    print(*b)