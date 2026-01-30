tramp = input()
q,r = map(str,input().split())
a=q[0:1]
b=q[1:2]
d=r[0:1]
e=r[1:2]
if a == "T":
    a=10
elif a =="J":
    a=11
elif a == "Q":
    a=12
elif a=="K":
    a=13
elif a =="A":
    a=14

if d == "T":
    d=10
elif d =="J":
    d=11
elif d == "Q":
    d=12
elif d=="K":
    d=13
elif d =="A":
    d=14
    
if b==tramp and e==tramp:
    if int(a)>int(d):
        print("YES")
    else:
        print("NO")
elif b==tramp:
    print("YES")
elif e==tramp:
    print("NO")
elif b==e :
    if int(a)>int(d):
        print("YES")
    else:
        print("NO")
else:
    print("NO")