t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    xorA = 0
    xorB = 0
    for i in range(n):
        if i%2==0:
            if xorA^a[i]>=xorB^b[i]:
                xorA^=a[i]
                xorB^=b[i]
            else:
                xorB^=a[i]
                xorA^=b[i]
        else:
            if xorB^b[i]>=xorA^a[i]:
                xorA^=a[i]
                xorB^=b[i]
            else:
                xorB^=a[i]
                xorA^=b[i]
    if xorA>xorB:
        print("Ajisai")
    elif xorA<xorB:
        print("Mai")
    else:
        print("Tie")