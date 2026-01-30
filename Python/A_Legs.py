t = int(input())
for _ in range(t):
    n = int(input())
    total = n//4 + (n-(n//4)*4)//2
    print(total)