t = int(input())
for _ in range(t):
    n = int(input())
    ny = False
    k = (n//2021)+1

    for i in range(k+1):
        if n % 2020 == 0 or n % 2021 == 0:
            ny = True
            break
        elif (n-i*2021)%2020 == 0 and (n-i*2021)//2020 >= 0:
            ny = True
            break
    if ny == True:
        print("YES")
    else:
        print("NO")