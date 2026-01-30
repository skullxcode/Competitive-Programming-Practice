n, a, b, c = map(int, input().split())
l = [a,b,c]
l.sort()
mi = l[0]
ma = l[2]
mid = l[1]
if n%mi==0:
    print(n//mi)
elif n%(mi+mid)==0:
    print(2+ (n-(mi+mid))//mi)
else:
    print(3+ (n-(mi+mid+ma))//mi)
