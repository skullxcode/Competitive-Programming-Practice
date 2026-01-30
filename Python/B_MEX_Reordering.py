t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    frq = {}
    for i in arr:
        frq[i] = frq.get(i,0)+1
    
    mex = 0
    while mex in frq:
        mex+=1
    
    if mex==1:
        if frq[0]==1:
            print("YES")
        else:
            print("NO")
    elif mex==0:
        print("NO")
    else:
        print("YES")
