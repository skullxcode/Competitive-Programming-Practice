t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if (s[0]=="0") or (s[-1]=="0") or (s.count("0")>s.count("1")) or ("00" in s):
        print(s.count("1"))
    else:
        a = []
        cnt = 1
        k=0
        for i in range(n):
            if(s[i]=='1'):
                k+=1
            else:
                a.append(k)
                k=0
        a.append(k)
        a.sort()
        # print(a)
        ans = sum(a[1:])+2*a[0]
        print(ans)