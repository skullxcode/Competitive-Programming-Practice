n = int(input())
a = list(map(int,input().split()))
a.sort()
flag = True
for i in range(len(a)):
    if a[i]!= i+1:
        print(i+1)
        flag = False
        break
if flag:
    print(n)