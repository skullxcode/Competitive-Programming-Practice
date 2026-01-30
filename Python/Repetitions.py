s = input()
cnt = 1
ans = 0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        cnt+=1
    else:
        ans = max(ans,cnt)
        cnt = 1
ans = max(ans,cnt)
print(ans)