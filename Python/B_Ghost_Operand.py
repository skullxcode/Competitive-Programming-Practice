x,z = map(int,input().split())
ans = -1
for i in range(min(x,z),max(x,z)+1):
    if x&i==z:
        ans = i
    break
print(ans)