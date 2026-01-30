t = int(input())
for _ in range(t):
    n = int(input())
    i = 1
    while True:
        if n%i==0:
            i+=1
        else:
            break
    print(i-1)