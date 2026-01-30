t = int(input())
for _ in range(t):
    n = input()
    l = len(n)
    if l>2:
        k = n[0:2]
        f = int(k)
        m = n[2:l+1]
        p = int(m)
        g = len(str(p))
        if f == 10 and p>1 and g==l-2:
            print("YES")
        else:
            print("NO")
    else:
            print("NO")