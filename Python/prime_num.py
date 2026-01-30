n = int(input())
l = []
for i in range(2,n):
    if n%i == 0:
        l.append(i)
if l == []:
    print("Prime Number")
else:
    print(l)