t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    while n%2==0 and n>0:
        n//=2
        ans+=1
    if n==1:
        print(ans)
    elif n==3:
        print(ans+1)
    else:
        if n%4==0:
            print(ans)
        else:
            print(-1)