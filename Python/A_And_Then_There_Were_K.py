t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    ans = n
    sol = 0
    while n>0:
        cnt+=1
        n>>=1
    for i in range(cnt-1):
        sol+=2**i
    print(sol)