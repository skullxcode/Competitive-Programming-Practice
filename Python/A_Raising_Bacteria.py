n = int(input())
count = 0
if n&(n-1)==0:
    print(1)
else:
    while n>0:
        n&=(n-1)
        count+=1
    print(count)