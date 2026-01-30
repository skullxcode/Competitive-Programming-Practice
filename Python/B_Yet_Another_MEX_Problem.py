t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    last = a[0]
    mex = -1
    for i in range(n):
        if a[i]==last or a[i]==last+1:
            last = a[i]
            mex = a[i]
        else:
            mex = a[i]+1
            break
    
    cnt = n-k+1
    
    for i in range(n-1):
        if a[i]==a[i+1]:
            mex = mex
            cnt-=1
        else:        
            print(min(mex,a[-1-cnt]))
            break
    
    
    
    # s = set(a)
    # freq = {}
    # for i in a:
    #     freq[i]= freq.get(i,0)+1
    # left = n-k+1
    # for i in s:
    #     if freq[i]>1:
    #         left -= (freq[i]-1)
    #         freq[i] = 1
    #     if left == 0:
    #         print(max(list(freq.keys())))