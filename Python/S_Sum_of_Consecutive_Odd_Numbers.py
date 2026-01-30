t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    k = max(x,y)
    h = min(x,y)
    sum=0
    for i in range(h+1,k):
        if i%2==1:
            sum+=i
    print(sum)