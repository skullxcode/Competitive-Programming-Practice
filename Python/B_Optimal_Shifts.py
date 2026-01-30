t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt = 0
    su = 0
    li = []
    for i in range(n):
        if s[i]=="0":
            cnt+=1
        else:
            li.append(cnt)
            cnt = 0
    li.append(cnt)
        

    if s[0]=="0" and s[-1]=="0":
        li.append(li[0]+li[-1])
    print(max(li))