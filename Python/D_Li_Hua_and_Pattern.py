import copy
t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    lis1 = []
    count = 0
    for i in range(n):
        a = list(map(int,input().split()))
        lis1.append(a)
    org = copy.deepcopy(lis1)
    for i in range(n):
        for j in range(i,n):
            lis1[i][j], lis1[j][i] = lis1[j][i], lis1[i][j]
    for i in range(n):
        for j in range(n//2):
            lis1[i][j], lis1[i][n-j-1] = lis1[i][n-j-1], lis1[i][j]

    for i in range(n):
        for j in range(i,n):
            lis1[i][j], lis1[j][i] = lis1[j][i], lis1[i][j]
    for i in range(n):
        for j in range(n//2):
            lis1[i][j], lis1[i][n-j-1] = lis1[i][n-j-1], lis1[i][j]

    for i in range(n):
        for j in range(n):
            if org[i][j]!=lis1[i][j]:
                count+=1

    if (count//2)<=k and (k - count//2)%2 == 0:
        print("YES")
    else:
        print("NO")
