a = input()
b = input()
if a==b:print("YES")
elif len(a)!=len(b):print("NO")
else:
    if a.count("1")>=1 and b.count("1")>=1:
        print("YES")
    else:
        print("NO")