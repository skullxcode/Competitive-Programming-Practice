n = int(input())
a = int(input())
b = int(input())
h = False
k = (n//b)+1

for i in range(k+1):
    if n % a == 0:
        h = True
        u = n // a
        v = 0
        break
    elif n % b == 0:
        h = True
        u = 0
        v = n // b   
        break   
    elif (n-i*b)%a == 0 and (n-i*b)//a >= 0:
        h = True
        u = (n-i*b)//a
        v = i
        break
if h == True:
    print("YES")
    print(u,v)
else:
    print("NO")