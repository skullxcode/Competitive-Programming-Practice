n = int(input())
l = list(map(str,input().split()))
k = []
for i in l:
    k.append(tuple(sorted(set(i))))
ans = len(set(k))
print(ans)