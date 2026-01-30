t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    _sum = 0
    _sum1 = 0
    _sum2 = 0
    for i in range(n):
        _sum+=a[i]
        if _sum%3==0:
            for j in range(i,n):
                _sum1+=a[j]
                if _sum1%3==0:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==0:
                            print(i,j)
                            break
                elif _sum1%3==1:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==2:
                            print(i,j)
                            break
                elif _sum1%3==2:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==1:
                            print(i,j)
                            break
        elif _sum%3==1:
            for j in range(i,n):
                _sum1+=a[j]
                if _sum1%3==1:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==1:
                            print(i,j)
                            break
                elif _sum1%3==0:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==2:
                            print(i,j)
                            break
                elif _sum1%3==2:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==0:
                            print(i,j)
                            break
        elif _sum%3==2:
            for j in range(i,n):
                _sum1+=a[j]
                if _sum1%3==2:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==2:
                            print(i,j)
                            break
                elif _sum1%3==0:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==1:
                            print(i,j)
                            break
                elif _sum1%3==1:
                    for k in range(j,n):
                        _sum2+=a[k]
                        if _sum2%3==0:
                            print(i,j)
                            break