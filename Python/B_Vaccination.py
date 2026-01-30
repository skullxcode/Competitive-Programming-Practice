t= int(input())
for _ in range(t):
    n,k,d,w = map(int,input().split())
    a = list(map(int,input().split()))
    m = max(a)
    for i in range(len(a)):
        if a[i]+w >=m:
            a[i] = a[i]+w
    cnt = 0
    temp = d
    ans = 0
    s = 0
    for i in range(len(a)-1):
        if abs(a[s]-a[i])<=d and temp>0:
            cnt+=1
            temp-=1
            # print(cnt)
        else:
            s = i
            ans += 1
            # print(ans)
            cnt = 0
            temp = d
    print(ans)