t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort
    s = list(set(a))

    cnt = 0
    for i in s:
        cm = 0
        for j in a:
            if j==i:
                cm +=1
        if cm>i:
            cnt+=abs(cm-i)
        else:
            cnt+=cm%i
    print(cnt)