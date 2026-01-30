t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    cnt2_=0
    cnt2 = a.count(2)
    ans = 0
    for i in range(n):
        if a[i]==2:
            cnt2_+=1
            cnt2-=1
        if cnt2_ == cnt2:
            ans = i+1
            break
    if ans:
        print(ans)
    else:
        print(-1)