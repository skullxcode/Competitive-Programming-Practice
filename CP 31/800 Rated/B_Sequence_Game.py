t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if sorted(a)==a:
        print(len(a))
        print(*a)
    else:
        b = [a[0]]
        for i in range(1,len(a)):
            if a[i]<a[i-1]:
                b.append(a[i])
            b.append(a[i])
        print(len(b))
        print(*b)