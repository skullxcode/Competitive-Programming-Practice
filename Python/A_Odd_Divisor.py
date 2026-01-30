t = int(input())
for _ in range(t):
    n = int(input())
    odd = False
    while n>0 and n*(n-1)!=0 and n%2==0:
        n//=2
    if n==1:
        print("NO")
    else:
        print("YES")