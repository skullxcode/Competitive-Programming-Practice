t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    arr = [1]
    for i in range(1,n):
        if s[i]=="(":
            arr.append(arr[-1]+1)
        else:
            arr.append(arr[-1]-1)
    if max(arr)>=3:
        print(n-2)
    else:
        print(-1)