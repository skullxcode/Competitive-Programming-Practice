def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    ans = False
    for i in range(n):
        for j in range(i+1,n):
            if gcd(a[i],a[j])<=2:
                ans = True
                break
    if not ans:
        print("No")
    else:
        print("Yes")