n, k = map(int,input().split())
a = 0
e = 0
i = 0
o = 0
u = 0
for _ in range(n):
    s = input()
    if s[-1]=="a":
        a+=1
    if s[-1]=="e":
        e+=1
    if s[-1]=="i":
        i+=1
    if s[-1]=="o":
        o+=1
    if s[-1]=="u":
        u+=1
if (a//2+e//2+i//2+o//2+u//2)//2>=k:
    print("YES")
else:
    print("NO")