t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    d = False
    if n % 2 == 0 or n % k ==0 or (k % 2 == 1 and n % 2 == 1):
        print("YES")
    else:
        print("NO")
        