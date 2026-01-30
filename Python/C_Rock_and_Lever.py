import math

def decToBinary(n):
	return bin(n)[2::]

t=int(input())
for _ in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    li.sort()
    li2=[]
    cnt = 0
    old_len=0
    for i in li:
        len1= len(decToBinary(i))
        if old_len==len1:
            cnt+=1
            old_len=len1
        else:
            li2.append(cnt)
            cnt=0
            old_len=len1
    li2.append(cnt)
    ans = sum([(x*(x+1)//2) for x in li2])
    print(ans)
        