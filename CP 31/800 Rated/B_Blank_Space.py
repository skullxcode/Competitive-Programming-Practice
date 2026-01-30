t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]
    prev = 0
    cnt = 0
    for i in range(n):
        if prev == a[i]:
            cnt+=1
        else:
            b.append(cnt)
            cnt = 0
    b.append(cnt)
    print(max(b))