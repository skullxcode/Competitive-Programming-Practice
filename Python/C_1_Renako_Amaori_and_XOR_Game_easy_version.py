t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if (sum(a)+sum(b))%2==0:
        print("Tie")
    else:
        winner = False
        for i in range(n-1,-1,-1):
            if a[i]!=b[i]:
                if i%2==0:
                    print("Ajisai")
                else:
                    print("Mai")
                winner = True
                break
        if not winner:
            print("Tie")