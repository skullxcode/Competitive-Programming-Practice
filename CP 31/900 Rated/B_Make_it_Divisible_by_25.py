t = int(input())
for _ in range(t):
    n = input()
    cnt00 = 0
    cnt25 = 0
    cnt50 = 0
    cnt75 = 0
    isfive = False
    iszero = False
    
    for i in range(len(n)-1,-1,-1):
        if n[i] == "0" and not iszero:
            iszero = True
        elif n[i] == "5" and not isfive:
            isfive = True
        else:
            cnt00 += 1
            cnt25 += 1
            cnt50 += 1
            cnt75 += 1