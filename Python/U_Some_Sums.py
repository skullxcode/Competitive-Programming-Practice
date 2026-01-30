n,a,b = map(int,input().split())
sum1 = 0
for i in range(1,n+1):
    sum =0
    c=i
    while i>0:
        sum += i%10
        i//=10
    if a<=sum<=b:
        sum1+=c
print(sum1)
