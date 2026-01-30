n = int(input())
s = set()
for _ in range(n):
    li = set(input())
    s.update(li)
lis = []
for i in range(1,n+1):
    for j in range(1,n+1):
        if ((i+j) not in s):
            lis.append(i+j)

print(set(lis))