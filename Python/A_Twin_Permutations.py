t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(n):
        k = min(a)+max(a)-a[i]
        b.append(str(k))
        separator = " "
    result = separator.join(b)
    print(result)