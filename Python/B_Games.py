t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    k = max(n,m)
    l = min(n,m)
    identical = 0
    if n==1 and m==1:
        print(1)
    elif n==1 or m==1:
        print(2)
    else:
        for i in range(k):
            for j in range(l):
                if k==n:
                    if a[i]==b[j]:
                        identical +=1
                else:
                    if b[i]==a[j]:
                        identical +=1
        print(n+m-(2*identical))