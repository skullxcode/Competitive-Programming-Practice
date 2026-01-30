t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    freq = {}
    for i in a:
        freq[i]=freq.get(i,0)+1
    if len(freq)>=3:
        print("No")
    elif len(freq)==1:
        print("Yes")
    else:
        k = sorted(set(a))
        if abs(freq[k[0]]-freq[k[1]])<=1:
            print("Yes")
        else:
            print("No")