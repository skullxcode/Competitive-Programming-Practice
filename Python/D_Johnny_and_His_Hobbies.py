t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    m = max(a)
    found = False
    for i in range(1,100000):
        li = [x^i for x in a]
        li.sort()
        if a==li:
            found = True
            ans = i
            break
    if found:
        print(ans)
    else:
        print(-1)
