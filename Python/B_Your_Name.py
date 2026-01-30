q = int(input())
for _ in range(q):
    n = int(input())
    s,t = map(str,input().split())
    s = sorted(s)
    s = "".join(s)
    t = sorted(t)
    t = "".join(t)
    if s==t:
        print("YES")
    else:
        print("NO")