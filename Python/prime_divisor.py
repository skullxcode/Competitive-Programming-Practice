n = int(input())
a = []
x = 0
for i in range(2,n):
    if n % i == 0:
        for j in range(2,i):
            if i%j == 0:
                x = 1
        if x == 0:
            a.append(i)
print(a)