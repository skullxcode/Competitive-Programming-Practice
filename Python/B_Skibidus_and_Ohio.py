t = int(input())
for _ in range(t):
    x = input()
    k = len(x)
    for i in range(k-1):
        if x[i] == x[i+1]:
            print(1)
            break
    else:
        print(k)