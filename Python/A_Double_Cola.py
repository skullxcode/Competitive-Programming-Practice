n = int(input())
i = 0
ans = 0
while (n>=0):
    if(n-5*(2**i))<0:
        break
    n-=5*(2**i)
    i+=1

ans = n//(2**i)
if n%(2**i)!=0:
    ans+=1

if ans == 1:
    print("Sheldon")
elif ans == 2:
    print("Leonard")
elif ans == 3:
    print("Penny")
elif ans == 4:
    print("Rajesh")
elif ans == 5:
    print("Howard")