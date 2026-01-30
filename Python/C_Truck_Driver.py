n,A,B = map(int,input().split())
s = input()
count = 0
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        k = s[i:j]
        a = k.count("a")
        b = k.count("b")
        if a>= A and b<B:
            count+=1
        elif b<B:
            continue
        elif b==B:
            break
print(count)