t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if len(s)==1:
        print(n)
    else:
        cnts=0
        cntd=0
        cntr=0
        for i in range(len(s)-1):
            if s[i]=="D":
                cntd+=1
            if s[i]=="R":
                cntr+=1
            if s[i]==s[i+1] and s[i]=="D":
                cnts+=2*(n-cntr)
            if s[i]==s[i+1] and s[i]=="R":
                cnts+=2*(n-cntd)
        cnt1 = s.count("RDR")
        cnt2 = s.count("DRD")
        ans = n*n - cnts - cnt1 - cnt2  
        print(ans)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
