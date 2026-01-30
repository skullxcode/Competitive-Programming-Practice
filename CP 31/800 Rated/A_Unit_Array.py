t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    minus = a.count(-1)
    plus = a.count(1)
    if plus>=minus:
            if minus%2==0:
                print(0)
            else:
                print(1)
    else:
        mid = n//2
        if mid%2==0:
            print(minus-mid)
        else:
            print(minus-mid+1)