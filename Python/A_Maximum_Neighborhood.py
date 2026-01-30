t = int(input())
for _ in range(t):
    n = int(input())
    if n==1:
        print(1)
    else:
        a = []
        for i in range(n):
            li = []
            for j in range((i*n)+1,(i*n)+n+1):
                li.append(j)
            a.append(li)
        ans = []
        for i in range(n):
            for j in range(n):
                if i==0 and j==0:
                    res = a[i][j]+a[i+1][j]+a[i][j+1]
                elif i==0 and j==n-1:
                    res = a[i][j]+a[i+1][j]+a[i][j-1]
                elif i==n-1 and j==0:
                    res = a[i][j]+a[i-1][j]+a[i][j+1]
                elif i==n-1 and j==n-1:
                    res = a[i][j]+a[i-1][j]+a[i][j-1]
                elif i==0:
                    res = a[i][j]+a[i+1][j]+a[i][j-1]+a[i][j+1]
                elif j==0:
                    res = a[i][j]+a[i+1][j]+a[i-1][j]+a[i][j+1]
                elif i==n-1:
                    res = a[i][j]+a[i-1][j]+a[i][j-1]+a[i][j+1]
                elif j==n-1:
                    res = a[i][j]+a[i+1][j]+a[i][j-1]+a[i-1][j]
                else:
                    res = a[i][j]+a[i+1][j]+a[i-1][j]+a[i][j+1]+a[i][j-1]
                ans.append(res)
        print(max(ans))

