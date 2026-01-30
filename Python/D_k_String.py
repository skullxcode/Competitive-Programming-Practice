n = int(input())
a = input()
l = list(set(a))
t=""
f = True
for i in l:
    k = a.count(i)
    m = k//n
    if k%n==0:
        f = True
        t+=m*i
    else:
        print(-1)
        f = False
        break
if f:
    print(t*n)
