t = int(input())
for _ in range(t):
    s = input()
    i = []
    c =[]
    p=[]
    for j in range(len(s)):
        if(s[j]=='I'):
            i.append(j+1)
        elif(s[j]=='C'):
            c.append(j+1)
        else:
            p.append(j+1)
    # print(i,c,p,sep="\n")
    w=0
    x=0
    y=len(c)-1
    z=0
    cnt=0
    l=[]
    ans=[]
    while(w<len(i) and x<len(c) and x<y and z<len(p)):
        l=[]
        if(i[w]<c[x]):
            if(c[x]<p[z]):
                if(p[z]<c[y]):
                    l.append(i[w])
                    l.append(c[x])
                    l.append(p[z])                    
                    l.append(c[y])
                    cnt+=1
                    w+=1
                    x+=1
                    z+=1
                    y-=1
                    ans.append(l)
                else:
                    break
            else:
                z+=1
        else:
            x+=1
    print(cnt)
    for i in ans:
        print(*i)
                

            
        