t = True
while t:
    l = ""
    n,m = map(int,input().split())
    if n<=0 or m<=0:
        break
    sum = 0
    k = max(n,m)
    h = min(n,m)
    for i in range(h,k+1):
        l+=str(i)+" "
        sum+=i
    print(l,end="")
    print(f"sum ={sum}")