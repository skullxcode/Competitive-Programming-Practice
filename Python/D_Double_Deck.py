n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a1 = [k]*(n)
b1 = [k]*(n)

i = 0
j = 0

ans = 0

while i<len(a) and j<len(b):
    if a[i]==b[j]:
        i+=1
        j+=1
        ans+=1
        a1[a[i]-1]-=1
        b1[b[j]-1]-=1
    else:
        