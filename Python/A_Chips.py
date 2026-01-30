n,m = map(int,input().split())
m = m%(n*(n+1)//2)
i = 1
while m>0:
    if m-i>=0:
        m-=i
    else:
        break
    i+=1
print(m)