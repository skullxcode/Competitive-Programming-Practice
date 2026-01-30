s = input()
l = ["A", "O", "Y", "E", "U", "I","a","o","y","e","u","i"]
ans = ""
for i in range(len(s)):
    if s[i] not in l:
        ans+="."
        ans+=s[i].lower()
print(ans)