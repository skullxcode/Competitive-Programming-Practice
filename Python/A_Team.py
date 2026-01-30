n = int(input())
total =0
for _ in range(n):
    a,b,c = map(int,input().split())
    count = 0
    if a==1:
        count+=1
    if b==1:
        count+=1
    if c==1:
        count+=1
    if count>=2:
        total+=1
print(total)