t = int(input())
ans = 1
for _ in range(t):
    n = int(input())
    if n%2==0:
        print(n//2,n//2)
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                ans = n//i
                break
            else:
                ans = 1
        print(ans,n-ans)