t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if "".join(list(sorted(s)))==s:
        print("Bob")
    else:
        print("Alice")
        ind = []
        z = s.count("0")
        for i in range(z):
            if s[i]=="1":
                ind.append(i+1)
        for j in range(z,n):
            if s[j]=="0":
                ind.append(j+1)
        print(len(ind))
        print(*ind)