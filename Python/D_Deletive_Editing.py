t = int(input())
for _ in range(t):
    s, a = input().split()
    freq = {}
    j = 0
    ans = ""
    for i in s:
        freq[i] = freq.get(i,0)+1
    for i in range(len(s)):
        if j==len(a):
            break
        if s[i]==a[j] and freq[s[i]]==a.count(a[j]):
            j+=1
            ans+=s[i]
        else:
            freq[s[i]]=freq.get(s[i],0)-1
    if j==len(a):
        print("YES")
    else:
        print("NO")