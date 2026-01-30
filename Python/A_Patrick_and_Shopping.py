a,b,c = map(int,input().split())
if a+b<c:
    print(2*(a+b))
elif a+c<b:
    print(2*(a+c))
elif b+c<a:
    print(2*(b+c))
else:
    print(a+b+c)