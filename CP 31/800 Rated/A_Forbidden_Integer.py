t = int(input())
for _ in range(t):
    n,k,x = map(int,input().split())
    ans = False
    for i in range(1,k+1):
        if i==x:
            continue
        else:
            s = n
            b = []
            while s>0:
                s-=i
                if s<=k and s!=x and s>=0:
                    b.append(i)
                    if s!=0:
                        b.append(s)
                    ans = True
                    break
                else:
                    b.append(i)
            
            if ans:
                print("YES")
                print(len(b))
                print(*b)
                break
    else:
        print("NO")