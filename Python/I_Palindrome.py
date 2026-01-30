n = input()
l = len(n)
for i in range(l//2+1):
    if int(n[i])==int(n[l-1-i]):
        t = True
    else:
        t = False
        break
n = int(n[::-1])
print(n)
if t:
    print("YES")
else:
    print("NO")