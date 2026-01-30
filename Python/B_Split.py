t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    frq = {}
    for i in a:
        frq[i] = frq.get(i,0)+1
    ans = 0
    ce = 0
    co = 0
    for value in frq:
        if frq[value]%2==0:
            ans+=2
            ce += 1 
        else:
            ans+=1
            co+=1
    if n%2 != len(set(a))%2:
        if co:
            ans = ans
        else:
            ans -= 2
    print(ans)