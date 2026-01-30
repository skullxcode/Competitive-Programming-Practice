t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    temp = a[0]
    temp2=False
    for i in range(n):
        if a[i] != temp:
            temp2=True
            break
    if temp2:
        a.sort(reverse=True)
        b = a[-1]
        a.pop()
        print("YES")
        print(b,*a)
    else:
        print("NO")