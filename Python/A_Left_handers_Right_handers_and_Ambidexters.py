l,r,a = map(int,input().split())
min = min(l,r)
max = max(l,r)
if l==r:
    print(l+r+(a//2)*2)
elif min+a<=max:
    print(2*(min+a))
elif min+a>=max:
    print(2*(max)+((min+a-max)//2)*2)