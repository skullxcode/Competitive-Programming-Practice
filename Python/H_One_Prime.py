n = int(input())
p = True
for i in range(2,n):
    if n%i == 0:
        p = False
        break
    else:
        p = True
if p == True:
    print("YES")
else:
    print("NO")
    