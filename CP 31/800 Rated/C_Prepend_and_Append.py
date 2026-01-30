def twoPointer(s):
    l = 0
    r = len(s)-1
    cnt = 0
    while l<=r:
        if s[l]==s[r]:
            return cnt
        else:
            l+=1
            r-=1
            cnt+=2
    return cnt    
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = n - twoPointer(s)
    print(ans)