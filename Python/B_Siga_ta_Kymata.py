t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    mx = a.index(n)
    mn = a.index(1)
    x = input()
    if int(x[0])==1 or int(x[n-1])==1 or int(x[mx])==1 or int(x[mn])==1:
        print(-1)
        continue
    else:
        print(x.count("1"))
        for i in range(1,len(x)-1):
            if x[i]=="1":
                if min(a[0:i])<a[i]<max(a[i+1:n]):
                    print(a.index(min(a[0:i]))+1,a.index(max(a[i+1:n]))+1)
                else:
                    print(a.index(max(a[0:i]))+1,a.index(min(a[i+1:n]))+1)
