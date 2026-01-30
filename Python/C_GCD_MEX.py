def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

t = int(input())
for _ in range(t):
    n = int(input())
    ans = 1
    for i in range(1,n):
        ans = lcm(ans,i)
    print(n)
    for i in range(1,n):
        print(i,end=" ")
    print(ans)