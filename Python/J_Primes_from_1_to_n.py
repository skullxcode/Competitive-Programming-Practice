n = int(input())
for i in range(2,n+1):
    k=1
    if i ==2:
        print(2,end=" ")
    else:
        for j in range(2,int(i**0.5)+2):
            if i%j == 0:
               k=1
               break
            else:
                k=0
        if k == 0:
            print(i,end=" ")