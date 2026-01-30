t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cons = 0
    cnt = 1
    for i in range(n-1):
        if s[i]==s[i+1]:
            cnt+=1
        else:
            cons = max(cons,cnt)
            cnt = 1
        
    cons = max(cons,cnt)
    print(cons+1)