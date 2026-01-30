t = int(input())
for _ in range(t):
    a = []
    for i in range(10):
        l = input()
        a.append(l)
    res = 0
    for i in range(10):
        for j in range(10):
            if a[i][j]=="X":
                if i==0 or i==9 or j==0 or j==9:
                    res+=1
                elif i==1 or i==8 or j==1 or j==8:
                    res+=2
                elif i==2 or i==7 or j==2 or j==7:
                    res+=3
                elif i==3 or i==6 or j==3 or j==6:
                    res+=4
                elif i==4 or i==5 or j==4 or j==5:
                    res+=5
    print(res)