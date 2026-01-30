t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        print("YES")
    elif b == 0:
        if a % 2 == 0:
            print("YES")
        else:
            print("NO")
    elif a == 0:
        if b % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        if a > b:
            if (a - 2*b) % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            if (a - 2*b) % 2 == 0:
                print("YES")
            else:
                print("NO")