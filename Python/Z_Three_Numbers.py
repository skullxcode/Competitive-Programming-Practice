k,s = map(int,input().split())
count=0
for n in range(k+1):
    for m in range(k+1):
            if n+m<=s and s-n-m<=k:
                count+=1
print(count)